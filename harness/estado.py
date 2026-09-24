"""Leitura e escrita do estado do harness no disco.

O estado é texto versionado no git: um JSONL por tipo em `data/` e uma pasta por
oportunidade em `oportunidades/`, com `cartao.md` (frontmatter YAML + corpo) e dossiês.
Toda escrita passa por aqui para garantir schema, id único e referências válidas.
"""

from __future__ import annotations

import fcntl
import json
import re
import unicodedata
from collections.abc import Iterator
from contextlib import contextmanager
from copy import deepcopy
from datetime import date
from pathlib import Path

import yaml

from harness.esquemas import DIR_SCHEMAS_PADRAO, TIPOS_JSONL, erros_de_schema, tipo_registro
from harness.exceptions import (
    ArquivoCorrompido,
    IdDuplicado,
    RegistroInvalido,
    RegistroNaoEncontrado,
)
from harness.validacao import Cartao, Snapshot, referencias_quebradas

RAIZ_PADRAO = Path(__file__).resolve().parent.parent
DIR_OPORTUNIDADES = "oportunidades"
ARQUIVO_CARTAO = "cartao.md"
PADRAO_DOSSIE = "dossie-*.md"
ARQUIVO_CONTRATO = "contrato.json"
DELIMITADOR_FRONTMATTER = "---"
PARTES_DO_CARTAO = 3  # texto antes do frontmatter (vazio), frontmatter, corpo
TAMANHO_MAXIMO_SLUG = 40
CAMPOS_IMUTAVEIS = frozenset({"id", "historico"})
CAMPOS_IMUTAVEIS_CARTAO = frozenset({"id", "criado_em"})
ARQUIVO_TRAVA = "data/.trava"
TITULO_HISTORICO = "## Histórico"


class Repositorio:
    """Acesso ao estado do harness numa raiz de repositório."""

    def __init__(self, raiz: Path = RAIZ_PADRAO, dir_schemas: Path = DIR_SCHEMAS_PADRAO) -> None:
        """Aponta o repositório para uma raiz (a do projeto, por padrão)."""
        self.raiz = raiz
        self.dir_schemas = dir_schemas

    # ---------- leitura ----------

    def ler(self, tipo: str) -> list[dict]:
        """Lê todos os registros de um tipo JSONL, na ordem do arquivo.

        Raises:
            ArquivoCorrompido: se alguma linha não for JSON de objeto.
        """
        caminho = self._arquivo(tipo)
        if not caminho.exists():
            return []
        registros = []
        for numero, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), start=1):
            if not linha.strip():
                continue
            try:
                registro = json.loads(linha)
            except json.JSONDecodeError as erro:
                raise ArquivoCorrompido(
                    f"{caminho.name}:{numero}: JSON inválido ({erro})"
                ) from erro
            if not isinstance(registro, dict):
                raise ArquivoCorrompido(f"{caminho.name}:{numero}: linha não é um objeto JSON")
            registros.append(registro)
        return registros

    def obter(self, tipo: str, id_registro: str) -> dict:
        """Devolve um registro pelo id.

        Raises:
            RegistroNaoEncontrado: se o id não existir.
        """
        if tipo == "cartao":
            return self._cartao_por_id(id_registro).campos
        for registro in self.ler(tipo):
            if registro.get("id") == id_registro:
                return registro
        raise RegistroNaoEncontrado(f"{tipo} {id_registro} não encontrado")

    def ler_cartoes(self) -> list[Cartao]:
        """Lê os cartões de todas as pastas de oportunidade.

        Raises:
            ArquivoCorrompido: se algum cartão não tiver frontmatter YAML válido.
        """
        pasta_raiz = self.raiz / DIR_OPORTUNIDADES
        if not pasta_raiz.exists():
            return []
        return [_ler_cartao(caminho) for caminho in sorted(pasta_raiz.glob(f"*/{ARQUIVO_CARTAO}"))]

    def ler_dossies(self) -> dict[str, str]:
        """Lê o texto de todos os dossiês, indexado pelo caminho relativo à raiz."""
        pasta_raiz = self.raiz / DIR_OPORTUNIDADES
        return {
            str(caminho.relative_to(self.raiz)): caminho.read_text(encoding="utf-8")
            for caminho in sorted(pasta_raiz.glob(f"*/{PADRAO_DOSSIE}"))
        }

    def ler_contratos(self) -> dict[str, dict]:
        """Lê os contratos de validação, indexados pelo nome da pasta da oportunidade.

        Raises:
            ArquivoCorrompido: se algum contrato não for JSON de objeto.
        """
        contratos = {}
        for caminho in sorted((self.raiz / DIR_OPORTUNIDADES).glob(f"*/{ARQUIVO_CONTRATO}")):
            try:
                contrato = json.loads(caminho.read_text(encoding="utf-8"))
            except json.JSONDecodeError as erro:
                raise ArquivoCorrompido(f"{caminho}: JSON inválido ({erro})") from erro
            if not isinstance(contrato, dict):
                raise ArquivoCorrompido(f"{caminho}: contrato não é um objeto JSON")
            contratos[caminho.parent.name] = contrato
        return contratos

    def pasta_da_oportunidade(self, id_cartao: str) -> Path:
        """Caminho absoluto da pasta de uma oportunidade.

        Raises:
            RegistroNaoEncontrado: se o cartão não existir.
        """
        return self.raiz / DIR_OPORTUNIDADES / self._cartao_por_id(id_cartao).pasta

    def snapshot(self) -> Snapshot:
        """Carrega todo o estado em memória para validação ou relatórios."""
        return Snapshot(
            registros={tipo: self.ler(tipo) for tipo in TIPOS_JSONL},
            cartoes=self.ler_cartoes(),
            dossies=self.ler_dossies(),
            contratos=self.ler_contratos(),
        )

    def proximo_id(self, tipo: str, hoje: date) -> str:
        """Calcula o próximo id livre de um tipo (f-2026-0007, OP-0003...)."""
        descricao = tipo_registro(tipo)
        if descricao.anual:
            prefixo = f"{descricao.prefixo}-{hoje.year}-"
            existentes = {registro.get("id", "") for registro in self.ler(tipo)}
        else:
            prefixo = f"{descricao.prefixo}-"
            existentes = {cartao.campos.get("id", "") for cartao in self.ler_cartoes()}
        numeros = [
            int(id_existente.removeprefix(prefixo))
            for id_existente in existentes
            if id_existente.startswith(prefixo) and id_existente.removeprefix(prefixo).isdigit()
        ]
        return f"{prefixo}{max(numeros, default=0) + 1:04d}"

    # ---------- escrita ----------

    def adicionar(self, tipo: str, registro: dict, hoje: date) -> dict:
        """Valida e grava um registro novo num JSONL, atribuindo id se faltar.

        Args:
            tipo: Tipo JSONL (fato, sinal, veredito, teste).
            registro: O registro; `id` é opcional.
            hoje: Data usada para gerar o id.

        Returns:
            O registro gravado, com id.

        Raises:
            RegistroInvalido: se falhar no schema ou tiver referência quebrada.
            IdDuplicado: se o id informado já existir.
        """
        with self._trava():
            novo = deepcopy(registro)
            novo.setdefault("id", self.proximo_id(tipo, hoje))
            if novo["id"] in {existente.get("id") for existente in self.ler(tipo)}:
                raise IdDuplicado(f"{tipo} {novo['id']} já existe")
            self._exigir_valido(tipo, novo)
            caminho = self._arquivo(tipo)
            caminho.parent.mkdir(parents=True, exist_ok=True)
            with caminho.open("a", encoding="utf-8") as arquivo:
                arquivo.write(json.dumps(novo, ensure_ascii=False) + "\n")
            return novo

    def atualizar(
        self, tipo: str, id_registro: str, mudancas: dict, motivo: str, hoje: date
    ) -> dict:
        """Aplica mudanças a um registro JSONL guardando os valores antigos no histórico.

        Correção nunca sobrescreve em silêncio: cada campo alterado vira uma entrada em
        `historico` (quando o schema do tipo tem histórico) com data, valor anterior e motivo.

        Raises:
            RegistroNaoEncontrado: se o id não existir.
            RegistroInvalido: se o resultado falhar no schema ou tentar mudar id/histórico.
        """
        proibidos = CAMPOS_IMUTAVEIS & mudancas.keys()
        if proibidos:
            raise RegistroInvalido(tipo, [f"campo não pode ser alterado: {sorted(proibidos)}"])
        with self._trava():
            return self._atualizar_sob_trava(tipo, id_registro, mudancas, motivo, hoje)

    def _atualizar_sob_trava(
        self, tipo: str, id_registro: str, mudancas: dict, motivo: str, hoje: date
    ) -> dict:
        registros = self.ler(tipo)
        indice = next(
            (i for i, registro in enumerate(registros) if registro.get("id") == id_registro), None
        )
        if indice is None:
            raise RegistroNaoEncontrado(f"{tipo} {id_registro} não encontrado")
        atualizado = deepcopy(registros[indice])
        for campo, valor in mudancas.items():
            if tipo == "fato" and atualizado.get(campo) != valor:
                atualizado.setdefault("historico", []).append(
                    {
                        "data": hoje.isoformat(),
                        "campo": campo,
                        "valor_anterior": atualizado.get(campo),
                        "motivo": motivo,
                    }
                )
            atualizado[campo] = valor
        self._exigir_valido(tipo, atualizado)
        registros[indice] = atualizado
        linhas = [json.dumps(registro, ensure_ascii=False) for registro in registros]
        self._arquivo(tipo).write_text("\n".join(linhas) + "\n", encoding="utf-8")
        return atualizado

    def criar_cartao(self, campos: dict, corpo: str, hoje: date) -> Path:
        """Cria a pasta e o `cartao.md` de uma oportunidade nova.

        Args:
            campos: Frontmatter do cartão; `id`, `criado_em` e `atualizado_em` são opcionais.
            corpo: Texto markdown abaixo do frontmatter.
            hoje: Data de criação.

        Returns:
            Caminho do `cartao.md` criado.

        Raises:
            RegistroInvalido: se o frontmatter falhar no schema ou nas referências.
            IdDuplicado: se o id já existir.
        """
        with self._trava():
            novo = deepcopy(campos)
            novo.setdefault("id", self.proximo_id("cartao", hoje))
            novo.setdefault("criado_em", hoje.isoformat())
            novo.setdefault("atualizado_em", hoje.isoformat())
            if novo["id"] in {cartao.campos.get("id") for cartao in self.ler_cartoes()}:
                raise IdDuplicado(f"cartão {novo['id']} já existe")
            self._exigir_valido("cartao", novo)
            pasta = self.raiz / DIR_OPORTUNIDADES / f"{novo['id']}-{_slug(novo['titulo'])}"
            pasta.mkdir(parents=True)
            caminho = pasta / ARQUIVO_CARTAO
            caminho.write_text(_montar_cartao(novo, corpo), encoding="utf-8")
            return caminho

    def gravar_contrato(self, contrato: dict) -> Path:
        """Grava o contrato de validação de uma oportunidade. Só pode ser gravado uma vez.

        O contrato registra a régua antes de a evidência chegar; reescrevê-lo depois
        permitiria mover a régua para caber no resultado.

        Raises:
            RegistroNaoEncontrado: se a oportunidade não existir.
            IdDuplicado: se a oportunidade já tiver contrato.
            RegistroInvalido: se o contrato falhar no schema.
        """
        with self._trava():
            caminho = (
                self.pasta_da_oportunidade(contrato.get("oportunidade", "")) / ARQUIVO_CONTRATO
            )
            if caminho.exists():
                raise IdDuplicado(f"{contrato['oportunidade']} já tem contrato; ele não muda")
            self._exigir_valido("contrato", contrato)
            caminho.write_text(
                json.dumps(contrato, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            return caminho

    def atualizar_cartao(self, id_cartao: str, mudancas: dict, nota: str, hoje: date) -> dict:
        """Altera o frontmatter de um cartão e registra a mudança na seção Histórico.

        Args:
            id_cartao: Id da oportunidade (OP-0001).
            mudancas: Campos do frontmatter a trocar (estagio, status, travas...).
            nota: Uma linha explicando a mudança, anexada ao histórico com a data.
            hoje: Data da mudança; vira também `atualizado_em`.

        Returns:
            O frontmatter atualizado.

        Raises:
            RegistroNaoEncontrado: se o cartão não existir.
            RegistroInvalido: se o resultado falhar no schema ou tentar mudar id/criado_em.
        """
        proibidos = CAMPOS_IMUTAVEIS_CARTAO & mudancas.keys()
        if proibidos:
            raise RegistroInvalido("cartao", [f"campo não pode ser alterado: {sorted(proibidos)}"])
        with self._trava():
            cartao = self._cartao_por_id(id_cartao)
            campos = {**cartao.campos, **mudancas, "atualizado_em": hoje.isoformat()}
            self._exigir_valido("cartao", campos)
            corpo = _anexar_historico(cartao.corpo, f"- {hoje.isoformat()}: {nota}")
            caminho = self.raiz / DIR_OPORTUNIDADES / cartao.pasta / ARQUIVO_CARTAO
            caminho.write_text(_montar_cartao(campos, corpo), encoding="utf-8")
            return campos

    # ---------- internos ----------

    @contextmanager
    def _trava(self) -> Iterator[None]:
        """Serializa escritas: subagentes em paralelo não podem gerar o mesmo id."""
        caminho = self.raiz / ARQUIVO_TRAVA
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open("w") as arquivo:
            fcntl.flock(arquivo, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(arquivo, fcntl.LOCK_UN)

    def _arquivo(self, tipo: str) -> Path:
        arquivo = tipo_registro(tipo).arquivo
        if arquivo is None:
            raise RegistroInvalido(tipo, ["cartões não ficam em JSONL; use criar_cartao"])
        return self.raiz / arquivo

    def _cartao_por_id(self, id_cartao: str) -> Cartao:
        for cartao in self.ler_cartoes():
            if cartao.campos.get("id") == id_cartao:
                return cartao
        raise RegistroNaoEncontrado(f"cartão {id_cartao} não encontrado")

    def _exigir_valido(self, tipo: str, registro: dict) -> None:
        erros = erros_de_schema(tipo, registro, self.dir_schemas)
        erros += referencias_quebradas(self.snapshot(), tipo, registro)
        if erros:
            raise RegistroInvalido(tipo, erros)


def _ler_cartao(caminho: Path) -> Cartao:
    texto = caminho.read_text(encoding="utf-8")
    partes = texto.split(f"{DELIMITADOR_FRONTMATTER}\n", 2)
    if len(partes) != PARTES_DO_CARTAO or partes[0].strip():
        raise ArquivoCorrompido(f"{caminho}: cartão sem frontmatter delimitado por '---'")
    try:
        campos = yaml.safe_load(partes[1]) or {}
    except yaml.YAMLError as erro:
        raise ArquivoCorrompido(f"{caminho}: frontmatter YAML inválido ({erro})") from erro
    if not isinstance(campos, dict):
        raise ArquivoCorrompido(f"{caminho}: frontmatter não é um mapeamento")
    return Cartao(pasta=caminho.parent.name, campos=_datas_como_texto(campos), corpo=partes[2])


def _datas_como_texto(campos: dict) -> dict:
    """YAML converte 2026-09-24 em date; o schema espera texto ISO."""
    return {
        chave: valor.isoformat() if isinstance(valor, date) else valor
        for chave, valor in campos.items()
    }


def _montar_cartao(campos: dict, corpo: str) -> str:
    frontmatter = yaml.safe_dump(campos, allow_unicode=True, sort_keys=False)
    return f"{DELIMITADOR_FRONTMATTER}\n{frontmatter}{DELIMITADOR_FRONTMATTER}\n{corpo}"


def _anexar_historico(corpo: str, linha: str) -> str:
    if TITULO_HISTORICO not in corpo:
        corpo = f"{corpo.rstrip()}\n\n{TITULO_HISTORICO}\n"
    return f"{corpo.rstrip()}\n{linha}\n"


def _slug(titulo: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-")
    return slug[:TAMANHO_MAXIMO_SLUG].rstrip("-") or "oportunidade"

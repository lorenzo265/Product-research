"""Coletor do PNCP (lentes 11, 4 e 6): compras públicas cujo objeto menciona um tema.

Compra pública é demanda com dinheiro por construção: todo registro tem valor estimado e
órgão comprador. A API de consulta não tem busca por texto, então o coletor pagina uma
janela curta de datas por modalidade e filtra o objeto localmente.
"""

from __future__ import annotations

import json
import unicodedata
from collections import Counter
from collections.abc import Callable
from dataclasses import asdict, dataclass
from datetime import date
from urllib.parse import urlencode

from harness.exceptions import HarnessError
from harness.verificacao import Pagina, baixar_com_curl

URL_CONSULTA = "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao"
TAMANHO_PAGINA = 50
MODALIDADES_PADRAO = (6, 8)  # 6 = pregão eletrônico, 8 = dispensa
URL_PNCP_EDITAL = "https://pncp.gov.br/app/editais/{cnpj}/{ano}/{sequencial}"
TENTATIVAS_POR_PAGINA = 2


@dataclass(frozen=True)
class Compra:
    """Uma contratação publicada no PNCP cujo objeto casou com os termos."""

    controle: str
    objeto: str
    valor_estimado: float | None
    orgao: str
    uf: str
    municipio: str
    modalidade: str
    publicada_em: str
    url: str

    def como_dict(self) -> dict:
        """Representação serializável."""
        return asdict(self)


@dataclass(frozen=True)
class ConsultaPncp:
    """O que procurar no PNCP.

    Attributes:
        inicio: Primeiro dia da janela de publicação.
        fim: Último dia (a API recusa janelas acima de 365 dias; use janelas curtas).
        termos: Palavras procuradas no objeto da compra, sem diferenciar acento e caixa.
        modalidades: Códigos de modalidade do PNCP.
        max_paginas: Teto de páginas por modalidade, para limitar tempo e carga na API.
    """

    inicio: date
    fim: date
    termos: tuple[str, ...]
    modalidades: tuple[int, ...] = MODALIDADES_PADRAO
    max_paginas: int = 20


@dataclass(frozen=True)
class ResultadoPncp:
    """Compras encontradas, registros lidos e páginas que falharam (coleta parcial)."""

    compras: list[Compra]
    lidos: int
    falhas: list[str]


def coletar_compras(
    consulta: ConsultaPncp, baixar: Callable[[str], Pagina] = baixar_com_curl
) -> ResultadoPncp:
    """Percorre as páginas da janela e devolve as compras que mencionam algum termo.

    Args:
        consulta: Janela, termos, modalidades e teto de páginas.
        baixar: Função de download (injetável para testes).

    Returns:
        Compras, registros lidos e falhas. Se uma página falhar depois de nova tentativa, a
        modalidade para ali e o que já foi lido é mantido: coleta parcial declarada, não
        perdida.

    Raises:
        HarnessError: se nenhum termo for informado.
    """
    termos_normalizados = [_normalizar(termo) for termo in consulta.termos]
    if not termos_normalizados:
        raise HarnessError("informe ao menos um termo")
    compras, lidos, falhas = [], 0, []
    for modalidade in consulta.modalidades:
        for numero in range(1, consulta.max_paginas + 1):
            try:
                pagina = _baixar_pagina(consulta, modalidade, numero, baixar)
            except HarnessError as erro:
                falhas.append(str(erro))
                break
            registros = pagina.get("data") or []
            lidos += len(registros)
            compras += [
                _compra(registro)
                for registro in registros
                if any(
                    t in _normalizar(registro.get("objetoCompra") or "")
                    for t in termos_normalizados
                )
            ]
            if not pagina.get("paginasRestantes"):
                break
    return ResultadoPncp(compras, lidos, falhas)


def resumir(compras: list[Compra]) -> dict:
    """Totais para registrar como fato: quantidade, valor estimado somado e UFs."""
    valores = [c.valor_estimado for c in compras if c.valor_estimado is not None]
    return {
        "compras": len(compras),
        "valor_estimado_total": round(sum(valores), 2),
        "orgaos_distintos": len({c.orgao for c in compras}),
        "por_uf": dict(Counter(c.uf for c in compras).most_common()),
    }


def _baixar_pagina(consulta: ConsultaPncp, modalidade: int, numero: int, baixar) -> dict:
    parametros = {
        "dataInicial": consulta.inicio.strftime("%Y%m%d"),
        "dataFinal": consulta.fim.strftime("%Y%m%d"),
        "codigoModalidadeContratacao": modalidade,
        "pagina": numero,
        "tamanhoPagina": TAMANHO_PAGINA,
    }
    url = f"{URL_CONSULTA}?{urlencode(parametros)}"
    for _ in range(TENTATIVAS_POR_PAGINA):
        resposta = baixar(url)
        if resposta.ok:
            break
    if not resposta.ok:
        raise HarnessError(
            f"PNCP inacessível (modalidade {modalidade}, página {numero}): {resposta.erro}"
        )
    if not resposta.texto.strip():
        return {}  # a API devolve corpo vazio quando não há registros na janela
    try:
        return json.loads(resposta.texto)
    except json.JSONDecodeError as erro:
        raise HarnessError(f"PNCP devolveu JSON inválido: {erro}") from erro


def _compra(registro: dict) -> Compra:
    unidade = registro.get("unidadeOrgao") or {}
    orgao = registro.get("orgaoEntidade") or {}
    url = URL_PNCP_EDITAL.format(
        cnpj=orgao.get("cnpj", ""),
        ano=registro.get("anoCompra", ""),
        sequencial=registro.get("sequencialCompra", ""),
    )
    return Compra(
        controle=registro.get("numeroControlePNCP") or "",
        objeto=(registro.get("objetoCompra") or "").strip(),
        valor_estimado=registro.get("valorTotalEstimado"),
        orgao=orgao.get("razaoSocial") or "",
        uf=unidade.get("ufSigla") or "",
        municipio=unidade.get("municipioNome") or "",
        modalidade=registro.get("modalidadeNome") or "",
        publicada_em=(registro.get("dataPublicacaoPncp") or "")[:10],
        url=url,
    )


def _normalizar(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.casefold()

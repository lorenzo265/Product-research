"""Testes do Repositorio contra um diretório temporário (tocam o filesystem)."""

import json
import shutil
from datetime import date
from pathlib import Path

import pytest

from harness.estado import Repositorio
from harness.exceptions import (
    ArquivoCorrompido,
    IdDuplicado,
    RegistroInvalido,
    RegistroNaoEncontrado,
)
from tests.fabricas import CARTAO, FATO, SINAL, novo

HOJE = date(2026, 9, 24)
SCHEMAS = Path(__file__).resolve().parents[2] / "schemas"


@pytest.fixture
def repo(tmp_path):
    shutil.copytree(SCHEMAS, tmp_path / "schemas")
    return Repositorio(raiz=tmp_path, dir_schemas=tmp_path / "schemas")


def _sem_id(registro):
    copia = novo(registro)
    del copia["id"]
    return copia


def test_adicionar_atribui_id_sequencial_do_ano(repo):
    primeiro = repo.adicionar("fato", _sem_id(FATO), HOJE)
    segundo = repo.adicionar("fato", _sem_id(FATO), HOJE)

    assert (primeiro["id"], segundo["id"]) == ("f-2026-0001", "f-2026-0002")


def test_adicionar_grava_uma_linha_json_por_registro(repo):
    repo.adicionar("fato", _sem_id(FATO), HOJE)

    linhas = (repo.raiz / "data/fatos.jsonl").read_text(encoding="utf-8").splitlines()

    assert json.loads(linhas[0])["alegacao"] == FATO["alegacao"]


def test_adicionar_rejeita_registro_fora_do_schema(repo):
    with pytest.raises(RegistroInvalido):
        repo.adicionar("fato", novo(FATO, tipo="palpite"), HOJE)

    assert repo.ler("fato") == []


def test_adicionar_rejeita_referencia_quebrada(repo):
    with pytest.raises(RegistroInvalido, match="f-2026-0001"):
        repo.adicionar("sinal", SINAL, HOJE)


def test_adicionar_rejeita_id_repetido(repo):
    repo.adicionar("fato", FATO, HOJE)

    with pytest.raises(IdDuplicado):
        repo.adicionar("fato", FATO, HOJE)


def test_atualizar_fato_guarda_valor_anterior_no_historico(repo):
    repo.adicionar("fato", FATO, HOJE)

    atualizado = repo.atualizar("fato", "f-2026-0001", {"valor": 149}, "preço mudou", HOJE)

    assert atualizado["valor"] == 149
    assert atualizado["historico"] == [
        {"data": "2026-09-24", "campo": "valor", "valor_anterior": 139, "motivo": "preço mudou"}
    ]
    assert repo.obter("fato", "f-2026-0001")["valor"] == 149


def test_atualizar_nao_permite_trocar_id(repo):
    repo.adicionar("fato", FATO, HOJE)

    with pytest.raises(RegistroInvalido, match="não pode ser alterado"):
        repo.atualizar("fato", "f-2026-0001", {"id": "f-2026-0009"}, "x", HOJE)


def test_atualizar_id_inexistente_falha(repo):
    with pytest.raises(RegistroNaoEncontrado):
        repo.atualizar("fato", "f-2026-0404", {"valor": 1}, "x", HOJE)


def test_criar_cartao_cria_pasta_com_id_e_slug_e_le_de_volta(repo):
    campos = _sem_id(CARTAO)

    caminho = repo.criar_cartao(campos, "\n## Dor\n", HOJE)

    assert caminho.parent.name == "OP-0001-conciliacao-para-escritorios-contabeis"
    assert repo.obter("cartao", "OP-0001")["titulo"] == CARTAO["titulo"]


def test_cartao_criado_passa_na_validacao_completa(repo):
    from harness.validacao import ERRO, validar

    repo.criar_cartao(_sem_id(CARTAO), "", HOJE)
    repo.adicionar("fato", FATO, HOJE)
    repo.adicionar("sinal", novo(SINAL, oportunidade="OP-0001"), HOJE)

    erros = [p for p in validar(repo.snapshot(), HOJE, repo.dir_schemas) if p.nivel == ERRO]

    assert erros == []


def test_linha_corrompida_e_reportada_com_numero(repo):
    (repo.raiz / "data").mkdir()
    (repo.raiz / "data/fatos.jsonl").write_text('{"id": "f-2026-0001"}\n{quebrado\n')

    with pytest.raises(ArquivoCorrompido, match="fatos.jsonl:2"):
        repo.ler("fato")


def test_cartao_sem_frontmatter_e_corrompido(repo):
    pasta = repo.raiz / "oportunidades/OP-0001-x"
    pasta.mkdir(parents=True)
    (pasta / "cartao.md").write_text("# sem frontmatter\n")

    with pytest.raises(ArquivoCorrompido, match="frontmatter"):
        repo.ler_cartoes()


def test_atualizar_cartao_muda_frontmatter_e_anota_historico(repo):
    repo.criar_cartao(_sem_id(CARTAO), "\n## Dor\n", HOJE)

    campos = repo.atualizar_cartao("OP-0001", {"estagio": "veredito"}, "kill barato passou", HOJE)

    assert campos["estagio"] == "veredito"
    cartao = repo.ler_cartoes()[0]
    assert cartao.campos["estagio"] == "veredito"
    assert "- 2026-09-24: kill barato passou" in cartao.corpo


def test_atualizar_cartao_rejeita_estagio_invalido(repo):
    repo.criar_cartao(_sem_id(CARTAO), "", HOJE)

    with pytest.raises(RegistroInvalido):
        repo.atualizar_cartao("OP-0001", {"estagio": "sonho"}, "x", HOJE)


def test_escritas_em_paralelo_nao_repetem_id(repo):
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=8) as executor:
        ids = list(
            executor.map(lambda _: repo.adicionar("fato", _sem_id(FATO), HOJE)["id"], range(16))
        )

    assert len(set(ids)) == 16


def test_atualizar_sinal_guarda_valor_anterior_e_motivo(repo):
    repo.adicionar("fato", FATO, HOJE)
    repo.adicionar("sinal", novo(SINAL, recorrencia="assinatura mensal"), HOJE)

    atualizado = repo.atualizar(
        "sinal", "s-2026-0001", {"recorrencia": None}, "modelo de cobrança", HOJE
    )

    assert atualizado["historico"] == [
        {
            "data": "2026-09-24",
            "campo": "recorrencia",
            "valor_anterior": "assinatura mensal",
            "motivo": "modelo de cobrança",
        }
    ]

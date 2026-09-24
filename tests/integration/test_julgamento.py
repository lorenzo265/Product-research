"""Montagem da entrada cega do juiz e contrato gravado uma vez."""

import json
import shutil
from datetime import date
from pathlib import Path

import pytest

from harness.estado import Repositorio
from harness.exceptions import HarnessError, IdDuplicado
from harness.julgamento import TETO_PALAVRAS_MEMORANDO, montar_pacote_juiz
from tests.fabricas import CARTAO, novo

HOJE = date(2026, 9, 24)
SCHEMAS = Path(__file__).resolve().parents[2] / "schemas"

CONTRATO = {
    "oportunidade": "OP-0001",
    "criado_em": "2026-09-24",
    "trilha": "M",
    "pacote": "pacote-micro-saas",
    "pergunta_neutralizada": "Escritórios contábeis pagam por conciliação automatizada?",
    "tese_de_terceiro": "Um terceiro propõe micro-SaaS de conciliação para escritórios.",
    "premissas_criticas": ["escritórios fazem conciliação à mão"],
    "condicoes_barreira": ["o sócio paga R$150/mês"],
    "alegacoes_kill": [
        {
            "alegacao": "não há ferramenta dominante",
            "dano_se_falsa": "alto",
            "como_verificar": "busca",
        }
    ],
    "taxa_base": {"p": 0.1, "classe_referencia": "micro-SaaS B2B BR", "justificativa": "R-03"},
}


@pytest.fixture
def repo(tmp_path):
    shutil.copytree(SCHEMAS, tmp_path / "schemas")
    repositorio = Repositorio(raiz=tmp_path, dir_schemas=tmp_path / "schemas")
    campos = novo(CARTAO)
    del campos["id"]
    repositorio.criar_cartao(campos, "", HOJE)
    return repositorio


def _preparar_oportunidade(
    repo, memorando_favor="Pontos a favor (f-2026-0001).", memorando_contra="Pontos contra."
):
    pasta = repo.pasta_da_oportunidade("OP-0001")
    repo.gravar_contrato(CONTRATO)
    (pasta / "dossie-mercado.md").write_text("# Dossiê\n")
    (pasta / "memorandos").mkdir()
    (pasta / "memorandos/a-favor.md").write_text(memorando_favor)
    (pasta / "memorandos/contra.md").write_text(memorando_contra)
    return pasta


def test_contrato_nao_pode_ser_regravado(repo):
    repo.gravar_contrato(CONTRATO)

    with pytest.raises(IdDuplicado):
        repo.gravar_contrato(novo(CONTRATO, trilha="S"))


def test_pacote_do_juiz_lista_so_os_arquivos_permitidos_e_sem_conviccao(repo):
    pasta = _preparar_oportunidade(repo)

    pacote = montar_pacote_juiz(repo.raiz, pasta, HOJE, semente=1)

    entrada = pacote.entrada.read_text()
    assert "Tese submetida por um terceiro" in entrada
    assert "dossie-mercado.md" in entrada
    assert "cartao.md" not in entrada
    assert str(pacote.entrada.relative_to(repo.raiz)) in pacote.mensagem


def test_memorandos_viram_a_e_b_com_direcao_declarada(repo):
    pasta = _preparar_oportunidade(repo)

    pacote = montar_pacote_juiz(repo.raiz, pasta, HOJE, semente=1)

    ordem = json.loads((pacote.pasta / "ordem.json").read_text())
    assert sorted(ordem.values()) == ["a-favor.md", "contra.md"]
    entrada = pacote.entrada.read_text()
    assert "Memorando A (argumenta" in entrada and "Memorando B (argumenta" in entrada


def test_sorteio_muda_a_ordem_com_a_semente(repo):
    pasta = _preparar_oportunidade(repo)
    ordens = set()
    for semente in range(10):
        pacote = montar_pacote_juiz(repo.raiz, pasta, HOJE, semente=semente)
        ordens.add(json.loads((pacote.pasta / "ordem.json").read_text())["A"])

    assert ordens == {"a-favor.md", "contra.md"}


def test_memorando_longo_e_cortado_no_teto(repo):
    pasta = _preparar_oportunidade(
        repo, memorando_favor="palavra " * (TETO_PALAVRAS_MEMORANDO + 50)
    )

    pacote = montar_pacote_juiz(repo.raiz, pasta, HOJE, semente=1)

    textos = [p.read_text() for p in pacote.pasta.glob("memorando-*.md")]
    assert any(f"[truncado em {TETO_PALAVRAS_MEMORANDO} palavras]" in t for t in textos)


def test_sem_memorandos_nao_monta(repo):
    pasta = repo.pasta_da_oportunidade("OP-0001")
    repo.gravar_contrato(CONTRATO)
    (pasta / "dossie-mercado.md").write_text("# Dossiê\n")

    with pytest.raises(HarnessError, match="memorandos faltando"):
        montar_pacote_juiz(repo.raiz, pasta, HOJE)

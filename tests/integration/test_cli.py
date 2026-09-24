"""A CLI grava, valida e bloqueia hooks como prometido."""

import io
import json
import shutil
from pathlib import Path

import pytest

from harness.__main__ import SAIDA_BLOQUEIO_HOOK, SAIDA_ERRO, SAIDA_OK, main
from tests.fabricas import FATO, SINAL, novo

SCHEMAS = Path(__file__).resolve().parents[2] / "schemas"


@pytest.fixture
def raiz(tmp_path):
    shutil.copytree(SCHEMAS, tmp_path / "schemas")
    return tmp_path


def _rodar(raiz, *argv, stdin=""):
    import sys

    entrada_original = sys.stdin
    sys.stdin = io.StringIO(stdin)
    try:
        return main(["--raiz", str(raiz), "--hoje", "2026-09-24", *argv])
    finally:
        sys.stdin = entrada_original


def test_adicionar_imprime_id_gerado(raiz, capsys):
    registro = novo(FATO)
    del registro["id"]

    codigo = _rodar(raiz, "adicionar", "fato", json.dumps(registro))

    assert codigo == SAIDA_OK
    assert capsys.readouterr().out.strip() == "f-2026-0001"


def test_adicionar_invalido_sai_com_erro_e_explica(raiz, capsys):
    codigo = _rodar(raiz, "adicionar", "sinal", json.dumps(SINAL))

    assert codigo == SAIDA_ERRO
    assert "f-2026-0001" in capsys.readouterr().err


def test_validar_em_hook_bloqueia_com_exit_2_quando_estado_invalido(raiz, capsys):
    (raiz / "data").mkdir()
    (raiz / "data/sinais.jsonl").write_text(json.dumps(SINAL) + "\n")
    evento = {"tool_input": {"file_path": str(raiz / "data/sinais.jsonl")}}

    codigo = _rodar(raiz, "validar", "--hook", stdin=json.dumps(evento))

    assert codigo == SAIDA_BLOQUEIO_HOOK
    assert "referência a fato inexistente" in capsys.readouterr().err


def test_validar_em_hook_ignora_arquivo_fora_do_estado(raiz):
    (raiz / "data").mkdir()
    (raiz / "data/sinais.jsonl").write_text(json.dumps(SINAL) + "\n")
    evento = {"tool_input": {"file_path": str(raiz / "docs/notas.md")}}

    assert _rodar(raiz, "validar", "--hook", stdin=json.dumps(evento)) == SAIDA_OK


def test_validar_em_stop_repetido_nao_prende_o_agente(raiz):
    (raiz / "data").mkdir()
    (raiz / "data/sinais.jsonl").write_text(json.dumps(SINAL) + "\n")

    codigo = _rodar(raiz, "validar", "--hook", stdin=json.dumps({"stop_hook_active": True}))

    assert codigo == SAIDA_OK


def test_novo_cartao_cria_pasta(raiz, capsys):
    campos = {
        "titulo": "Teste de cartão",
        "trilha": "S",
        "estagio": "oportunidade",
        "status": "ativa",
        "pergunta_neutralizada": "Existe demanda paga por X no segmento Y?",
        "quem_sofre": "a",
        "quem_paga": "b",
        "workaround": "c",
        "lentes": [10],
        "sinais": [],
        "travas": [],
        "proximo_passo": "kill barato",
        "revisar_em": "2026-10-24",
    }

    codigo = _rodar(raiz, "novo-cartao", json.dumps(campos))

    assert codigo == SAIDA_OK
    assert capsys.readouterr().out.strip() == "oportunidades/OP-0001-teste-de-cartao/cartao.md"


def test_atualizar_cartao_pela_cli(raiz, capsys):
    campos = {
        "titulo": "Cartão",
        "trilha": "M",
        "estagio": "oportunidade",
        "status": "ativa",
        "pergunta_neutralizada": "Existe demanda paga por X no segmento Y?",
        "quem_sofre": "a",
        "quem_paga": "b",
        "workaround": "c",
        "lentes": [1],
        "sinais": [],
        "travas": [],
        "proximo_passo": "kill barato",
        "revisar_em": "2026-10-24",
    }
    _rodar(raiz, "novo-cartao", json.dumps(campos))
    capsys.readouterr()

    codigo = _rodar(
        raiz, "atualizar", "cartao", "OP-0001", '{"estagio": "kill_barato"}', "--motivo", "início"
    )

    assert codigo == SAIDA_OK
    assert '"estagio": "kill_barato"' in capsys.readouterr().out

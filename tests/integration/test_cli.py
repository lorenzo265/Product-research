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


@pytest.mark.parametrize(
    "caminho",
    [
        "/repo/data/fatos.jsonl",
        "/repo/oportunidades/OP-0001-x/cartao.md",
        "/repo/oportunidades/OP-0001-x/contrato.json",
    ],
)
def test_proteger_estado_bloqueia_edicao_direta(raiz, caminho, capsys):
    evento = {"tool_name": "Edit", "tool_input": {"file_path": caminho}}

    codigo = _rodar(raiz, "proteger-estado", stdin=json.dumps(evento))

    assert codigo == SAIDA_BLOQUEIO_HOOK
    assert "python3 -m harness" in capsys.readouterr().err


@pytest.mark.parametrize(
    "caminho",
    ["/repo/oportunidades/OP-0001-x/dossie-mercado.md", "/repo/docs/decisoes.md"],
)
def test_proteger_estado_libera_arquivos_de_trabalho(raiz, caminho):
    evento = {"tool_name": "Write", "tool_input": {"file_path": caminho}}

    assert _rodar(raiz, "proteger-estado", stdin=json.dumps(evento)) == SAIDA_OK


def test_registrar_veredito_encolhe_p_e_liga_ao_cartao(raiz, capsys):
    from tests.fabricas import CARTAO, FATO, VEREDITO

    cartao = novo(CARTAO)
    del cartao["id"], cartao["criado_em"], cartao["atualizado_em"]
    _rodar(raiz, "novo-cartao", json.dumps(cartao))
    _rodar(raiz, "adicionar", "fato", json.dumps(FATO))
    capsys.readouterr()
    veredito = novo(VEREDITO, p_sucesso_bruta=0.6)
    for campo in ("id", "oportunidade", "data"):
        del veredito[campo]

    codigo = _rodar(raiz, "registrar-veredito", "OP-0001", json.dumps(veredito))

    saida = capsys.readouterr().out
    assert codigo == SAIDA_OK
    assert saida.startswith("v-2026-0001 · ITERAR · p_sucesso=")
    _rodar(raiz, "obter", "cartao", "OP-0001")
    assert '"v-2026-0001"' in capsys.readouterr().out


def test_registrar_veredito_que_substitui_marca_o_anterior(raiz, capsys):
    from tests.fabricas import CARTAO, FATO, VEREDITO

    cartao = novo(CARTAO)
    del cartao["id"], cartao["criado_em"], cartao["atualizado_em"]
    _rodar(raiz, "novo-cartao", json.dumps(cartao))
    _rodar(raiz, "adicionar", "fato", json.dumps(FATO))
    veredito = novo(VEREDITO)
    for campo in ("id", "oportunidade", "data"):
        del veredito[campo]
    _rodar(raiz, "registrar-veredito", "OP-0001", json.dumps(veredito))
    capsys.readouterr()

    codigo = _rodar(
        raiz,
        "registrar-veredito",
        "OP-0001",
        json.dumps(veredito),
        "--substitui",
        "v-2026-0001",
        "--motivo",
        "fato citado corrigido depois do veredito",
    )

    assert codigo == SAIDA_OK
    capsys.readouterr()
    _rodar(raiz, "obter", "veredito", "v-2026-0001")
    anterior = json.loads(capsys.readouterr().out)
    assert anterior["substituido_por"] == "v-2026-0002"
    assert _rodar(raiz, "validar") == SAIDA_OK


def test_substituir_sem_motivo_e_recusado(raiz):
    from tests.fabricas import VEREDITO

    veredito = novo(VEREDITO)
    for campo in ("id", "oportunidade", "data"):
        del veredito[campo]

    codigo = _rodar(
        raiz, "registrar-veredito", "OP-0001", json.dumps(veredito), "--substitui", "v-2026-0001"
    )

    assert codigo != SAIDA_OK

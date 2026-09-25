from harness.radar import medir_sinais, montar_fila
from harness.validacao import Snapshot
from tests.fabricas import FATO, SINAL, novo

FATO_RESUMO = novo(
    FATO,
    id="f-2026-0002",
    fonte={**FATO["fonte"], "leitura": "resumo_de_busca", "tier": 3},
)


def _snapshot(sinais, fatos=(FATO, FATO_RESUMO)):
    return Snapshot(registros={"sinal": list(sinais), "fato": list(fatos)})


def test_cifra_lida_na_pagina_vem_antes_de_cifra_de_resumo_de_busca():
    cifra_resumo = novo(
        SINAL,
        id="s-2026-0001",
        fatos=["f-2026-0002"],
        cifra={"valor": 1000, "unidade": "BRL/mes", "fato": "f-2026-0002"},
    )
    cifra_integral = novo(
        SINAL,
        id="s-2026-0002",
        cifra={"valor": 10, "unidade": "BRL/mes", "fato": "f-2026-0001"},
    )

    fila = medir_sinais(_snapshot([cifra_resumo, cifra_integral]))

    assert [m.sinal["id"] for m in fila] == ["s-2026-0002", "s-2026-0001"]
    assert fila[1].cifra and not fila[1].cifra_integral


def test_sem_cifra_ordena_por_recorrencia_e_depois_por_leitura_integral():
    so_resumo = novo(SINAL, id="s-2026-0001", fatos=["f-2026-0002"])
    integral = novo(SINAL, id="s-2026-0002")
    recorrente = novo(SINAL, id="s-2026-0003", fatos=["f-2026-0002"], recorrencia="semanal")

    fila = medir_sinais(_snapshot([so_resumo, integral, recorrente]))

    assert [m.sinal["id"] for m in fila] == ["s-2026-0003", "s-2026-0002", "s-2026-0001"]
    assert (fila[1].integrais, fila[1].tier1) == (1, 1)


def test_filtra_por_status_e_todos_inclui_descartados():
    descartado = novo(SINAL, id="s-2026-0002", status="descartado")

    assert [m.sinal["id"] for m in medir_sinais(_snapshot([SINAL, descartado]))] == ["s-2026-0001"]
    assert len(medir_sinais(_snapshot([SINAL, descartado]), status=None)) == 2


def test_tabela_marca_setor_com_mais_de_uma_lente_e_escapa_barra_vertical():
    outra_lente = novo(SINAL, id="s-2026-0002", lente=8, setor="Contabilidade ", dor="a | b c d e")

    tabela = montar_fila(medir_sinais(_snapshot([SINAL, outra_lente])))

    assert "- contabilidade: lentes 5, 8" in tabela
    assert "a / b c d e" in tabela


def test_fila_vazia_diz_que_nao_ha_sinais():
    assert montar_fila([]) == "Nenhum sinal com esse status."


def test_sinal_inverso_sai_da_fila_e_vai_para_lista_a_parte():
    inverso = novo(
        SINAL,
        id="s-2026-0002",
        sentido="mercado_servido",
        setor="self-storage",
        dor="player local com 250 clientes já cobra por boleto",
    )

    tabela = montar_fila(medir_sinais(_snapshot([SINAL, inverso])))
    fila, lista = tabela.split("Mercado já servido")

    assert "s-2026-0001" in fila and "s-2026-0002" not in fila
    assert "s-2026-0002 · lente 5 · self-storage" in lista

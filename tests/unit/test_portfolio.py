from datetime import date

from harness.portfolio import montar_painel
from harness.validacao import Cartao, Snapshot
from tests.fabricas import CARTAO, TESTE, novo

HOJE = date(2026, 9, 24)


def _snapshot(cartoes, testes=()):
    return Snapshot(
        registros={"teste": list(testes)},
        cartoes=[Cartao(pasta=f"{c['id']}-x", campos=c, corpo="") for c in cartoes],
    )


def test_painel_agrupa_por_trilha():
    cartoes = [CARTAO, novo(CARTAO, id="OP-0002", titulo="Agente de cobrança", trilha="S")]

    painel = montar_painel(_snapshot(cartoes), HOJE)

    assert "## M · Micro-SaaS" in painel
    assert "## S · Serviço com IA" in painel
    assert painel.index("OP-0001") < painel.index("Agente de cobrança")


def test_painel_lista_revisao_vencida_e_teste_sem_decisao():
    cartao = novo(CARTAO, revisar_em="2026-09-01")

    painel = montar_painel(_snapshot([cartao], testes=[TESTE]), HOJE)

    assert "Revisão vencida: OP-0001" in painel
    assert "Teste sem decisão: t-2026-0001" in painel


def test_cadaver_sai_da_tabela_e_vai_para_a_lista_com_motivo():
    cadaver = novo(CARTAO, status="cadaver", motivo_morte="2 de 3 alegações caíram")

    painel = montar_painel(_snapshot([cadaver]), HOJE)

    assert "## M · Micro-SaaS" not in painel
    assert "OP-0001 · Conciliação para escritórios contábeis: 2 de 3 alegações caíram" in painel

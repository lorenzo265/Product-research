from datetime import date

import pytest

from harness.calibracao import (
    MINIMO_PARA_AJUSTAR_REGUAS,
    Previsao,
    calibrar,
    vencidas_sem_resultado,
)


def _previsao(p, resultado, prazo="2026-12-31"):
    return Previsao("v-2026-0001", "M", "algo acontece", p, prazo, resultado)


def test_sem_previsoes_resolvidas_nao_calcula_nada():
    relatorio = calibrar([_previsao(0.7, None)])

    assert relatorio.resolvidas == 0
    assert relatorio.brier is None


def test_brier_de_previsoes_perfeitas_e_zero():
    relatorio = calibrar([_previsao(0.99, True), _previsao(0.01, False)])

    assert relatorio.brier == pytest.approx(0.0001)


def test_chutar_meio_a_meio_nao_tem_habilidade():
    relatorio = calibrar([_previsao(0.5, True), _previsao(0.5, False)])

    assert relatorio.brier == pytest.approx(0.25)
    assert relatorio.skill_score == pytest.approx(0.0)


def test_intervalo_de_confianca_contem_o_brier():
    previsoes = [_previsao(0.8, i % 3 != 0) for i in range(30)]

    relatorio = calibrar(previsoes)

    minimo, maximo = relatorio.intervalo_brier
    assert minimo <= relatorio.brier <= maximo


def test_poucas_previsoes_nao_liberam_ajuste_de_reguas():
    previsoes = [_previsao(0.7, True) for _ in range(MINIMO_PARA_AJUSTAR_REGUAS - 1)]

    assert calibrar(previsoes).pode_ajustar_reguas is False


def test_calibracao_por_faixa_usa_os_niveis_do_analista():
    previsoes = [_previsao(0.8, True), _previsao(0.8, False), _previsao(0.2, False)]

    faixas = {faixa.nivel: faixa for faixa in calibrar(previsoes).faixas}

    assert faixas["PROVAVEL"].quantidade == 2
    assert faixas["PROVAVEL"].frequencia_observada == pytest.approx(0.5)
    assert faixas["IMPROVAVEL"].quantidade == 1


def test_previsao_vencida_sem_resultado_aparece_para_resolver():
    previsoes = [_previsao(0.6, None, prazo="2026-09-01"), _previsao(0.6, None)]

    vencidas = vencidas_sem_resultado(previsoes, date(2026, 9, 24))

    assert [p.prazo for p in vencidas] == ["2026-09-01"]


def test_encolher_puxa_o_juiz_para_a_taxa_base():
    from harness.calibracao import encolher

    encolhida = encolher(0.8, 0.1)

    assert 0.1 < encolhida < 0.8


def test_encolher_com_fator_um_mantem_o_juiz():
    from harness.calibracao import encolher

    assert encolher(0.8, 0.1, fator=1.0) == pytest.approx(0.8)

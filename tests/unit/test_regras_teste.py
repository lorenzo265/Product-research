import pytest

from harness.regras_teste import fronteiras_bayes, fronteiras_sprt, prob_taxa_acima


def test_zero_em_quinze_deixa_pouca_chance_de_taxa_acima_de_dez_por_cento():
    assert prob_taxa_acima(0, 15, 0.10) == pytest.approx(0.9**16, abs=1e-9)


def test_tres_depositos_em_vinte_atingem_go_com_alvo_de_dez_por_cento():
    fronteira = fronteiras_bayes(0.10, 20)[-1]

    assert fronteira.go_a_partir_de is not None
    assert fronteira.go_a_partir_de <= 3


def test_bayes_nunca_da_go_e_kill_para_o_mesmo_resultado():
    for fronteira in fronteiras_bayes(0.10, 30):
        if fronteira.go_a_partir_de is not None and fronteira.kill_ate is not None:
            assert fronteira.kill_ate < fronteira.go_a_partir_de


def test_sprt_de_pre_venda_tem_fronteiras_crescentes_com_a_amostra():
    fronteiras = fronteiras_sprt(0.003, 0.01, [500, 1000])

    assert fronteiras[0].go_a_partir_de < fronteiras[1].go_a_partir_de
    assert fronteiras[1].kill_ate is not None


def test_sprt_com_poucos_visitantes_ainda_nao_pode_matar():
    fronteira = fronteiras_sprt(0.003, 0.01, [50])[0]

    assert fronteira.kill_ate is None


def test_sprt_rejeita_taxas_invertidas():
    with pytest.raises(ValueError):
        fronteiras_sprt(0.05, 0.03, [100])

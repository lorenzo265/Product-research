import json

import pytest

from harness.coletores.yc import baixar_empresas, filtrar_candidatos
from harness.exceptions import HarnessError
from harness.verificacao import Pagina


def _empresa(**campos):
    base = {
        "name": "Acme",
        "one_liner": "Invoicing for accountants",
        "long_description": "",
        "industry": "B2B",
        "industries": ["B2B", "Finance and Accounting"],
        "subindustry": "B2B -> Finance and Accounting",
        "tags": ["Fintech"],
        "team_size": 5,
        "batch": "Winter 2024",
        "status": "Active",
        "regions": ["United States of America", "America / Canada"],
        "all_locations": "San Francisco, CA, USA",
        "website": "https://acme.example",
        "url": "https://www.ycombinator.com/companies/acme",
    }
    return {**base, **campos}


def test_mantem_empresa_ativa_sem_presenca_no_brasil():
    assert [c.nome for c in filtrar_candidatos([_empresa()])] == ["Acme"]


@pytest.mark.parametrize(
    "campos",
    [
        {"status": "Inactive"},
        {"all_locations": "São Paulo, SP, Brazil"},
        {"regions": ["Latin America"]},
    ],
)
def test_descarta_inativa_ou_com_presenca_no_brasil(campos):
    assert filtrar_candidatos([_empresa(**campos)]) == []


def test_america_latina_pode_ser_incluida_quando_pedido():
    empresas = [_empresa(regions=["Latin America"], all_locations="Mexico City, Mexico")]

    assert len(filtrar_candidatos(empresas, incluir_america_latina=True)) == 1


def test_filtra_por_termo_industria_e_time():
    empresas = [
        _empresa(name="Grande", team_size=200),
        _empresa(name="Consumo", industry="Consumer", industries=["Consumer"]),
        _empresa(name="Outra coisa", one_liner="Robots", tags=[], subindustry="Industrials"),
        _empresa(name="Certa"),
    ]

    nomes = [
        c.nome
        for c in filtrar_candidatos(empresas, termos=["invoic"], industria="B2B", time_maximo=50)
    ]

    assert nomes == ["Certa"]


def test_ordena_do_menor_time_para_o_maior():
    empresas = [_empresa(name="B", team_size=9), _empresa(name="A", team_size=2)]

    assert [c.nome for c in filtrar_candidatos(empresas)] == ["A", "B"]


def test_baixar_rejeita_resposta_que_nao_e_lista():
    with pytest.raises(HarnessError):
        baixar_empresas(lambda url: Pagina(ok=True, texto=json.dumps({"erro": 1})))


def test_baixar_explica_pagina_inacessivel():
    with pytest.raises(HarnessError, match="inacessível"):
        baixar_empresas(lambda url: Pagina(ok=False, texto="", erro="curl saiu com 6"))

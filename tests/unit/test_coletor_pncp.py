import json
from datetime import date

import pytest

from harness.coletores.pncp import ConsultaPncp, coletar_compras, resumir
from harness.exceptions import HarnessError
from harness.verificacao import Pagina


def _registro(objeto, valor=1000.0, uf="PR", orgao="MUNICIPIO X"):
    return {
        "objetoCompra": objeto,
        "valorTotalEstimado": valor,
        "unidadeOrgao": {"ufSigla": uf, "municipioNome": "Cidade"},
        "orgaoEntidade": {"cnpj": "123", "razaoSocial": orgao},
        "modalidadeNome": "Dispensa",
        "dataPublicacaoPncp": "2026-09-15T00:00:21",
        "numeroControlePNCP": f"123-1-{objeto[:5]}/2026",
        "anoCompra": 2026,
        "sequencialCompra": 7,
    }


def _consulta(*termos, max_paginas=20):
    return ConsultaPncp(date(2026, 9, 15), date(2026, 9, 16), termos, (8,), max_paginas)


def _baixador(paginas):
    chamadas = []

    def baixar(url):
        chamadas.append(url)
        return Pagina(ok=True, texto=json.dumps(paginas[len(chamadas) - 1]))

    baixar.chamadas = chamadas
    return baixar


def test_filtra_objeto_por_termo_sem_diferenciar_acento():
    pagina = {
        "data": [
            _registro("Sistema de emissão de NOTA FISCAL eletrônica"),
            _registro("Brinquedos"),
        ],
        "paginasRestantes": 0,
    }

    resultado = coletar_compras(_consulta("nota fiscal"), baixar=_baixador([pagina]))

    assert resultado.lidos == 2
    assert [c.objeto for c in resultado.compras] == ["Sistema de emissão de NOTA FISCAL eletrônica"]


def test_para_quando_nao_ha_mais_paginas_e_respeita_teto():
    baixar = _baixador([{"data": [_registro("x")], "paginasRestantes": 5}] * 3)

    coletar_compras(_consulta("x", max_paginas=3), baixar=baixar)

    assert len(baixar.chamadas) == 3


def test_resumo_soma_valores_e_conta_orgaos():
    pagina = {
        "data": [
            _registro("nota fiscal", 100.0, "PR", "A"),
            _registro("nota fiscal", 50.0, "SP", "B"),
        ],
        "paginasRestantes": 0,
    }
    compras = coletar_compras(_consulta("nota"), baixar=_baixador([pagina])).compras

    assert resumir(compras) == {
        "compras": 2,
        "valor_estimado_total": 150.0,
        "orgaos_distintos": 2,
        "por_uf": {"PR": 1, "SP": 1},
    }


def test_corpo_vazio_significa_janela_sem_registros():
    def baixar(url):
        return Pagina(ok=True, texto="")

    resultado = coletar_compras(_consulta("x"), baixar=baixar)

    assert (resultado.compras, resultado.lidos, resultado.falhas) == ([], 0, [])


def test_falha_no_meio_mantem_o_que_ja_foi_lido_e_declara_a_falha():
    respostas = [
        Pagina(ok=True, texto=json.dumps({"data": [_registro("x")], "paginasRestantes": 3})),
        Pagina(ok=False, texto="", erro="curl saiu com 22"),
        Pagina(ok=False, texto="", erro="curl saiu com 22"),
    ]

    resultado = coletar_compras(_consulta("x"), baixar=lambda url: respostas.pop(0))

    assert resultado.lidos == 1
    assert len(resultado.compras) == 1
    assert "PNCP inacessível" in resultado.falhas[0]


def test_falha_passageira_e_superada_na_segunda_tentativa():
    respostas = [
        Pagina(ok=False, texto="", erro="curl saiu com 22"),
        Pagina(ok=True, texto=json.dumps({"data": [_registro("x")], "paginasRestantes": 0})),
    ]

    resultado = coletar_compras(_consulta("x"), baixar=lambda url: respostas.pop(0))

    assert (resultado.lidos, resultado.falhas) == (1, [])


def test_sem_termo_e_erro():
    with pytest.raises(HarnessError):
        coletar_compras(ConsultaPncp(date(2026, 9, 15), date(2026, 9, 16), ()))

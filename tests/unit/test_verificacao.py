from harness.verificacao import Pagina, conferir_trecho
from tests.fabricas import FATO, novo


def _baixador(conteudo, ok=True):
    return lambda url: Pagina(ok=ok, texto=conteudo, erro=None if ok else "curl saiu com 22")


def test_trecho_presente_no_html_e_encontrado_ignorando_tags_e_espacos():
    html = "<html><body><p>Plano   Básico</p> <b>R$ 139/mês</b></body></html>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "Plano Básico R$ 139/mês"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_trecho_ausente_da_pagina_falha():
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "Plano Básico R$ 139/mês"

    resultado = conferir_trecho(fato, _baixador("<p>Plano Básico R$ 169/mês</p>"))

    assert resultado.trecho_encontrado is False


def test_pagina_inacessivel_nao_conta_como_falha_do_trecho():
    resultado = conferir_trecho(novo(FATO), _baixador("", ok=False))

    assert resultado.trecho_encontrado is None
    assert "inacessível" in resultado.detalhe


def test_trecho_de_resumo_de_busca_nao_e_conferido_na_pagina():
    fato = novo(FATO)
    fato["fonte"]["leitura"] = "resumo_de_busca"

    resultado = conferir_trecho(fato, _baixador("qualquer coisa"))

    assert resultado.trecho_encontrado is None


def test_texto_de_script_nao_conta_como_texto_visivel():
    html = "<script>var x = 'Plano Básico R$ 139/mês';</script><p>outra coisa</p>"

    resultado = conferir_trecho(novo(FATO), _baixador(html))

    assert resultado.trecho_encontrado is False

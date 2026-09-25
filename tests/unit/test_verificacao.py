from harness.verificacao import Pagina, conferir_trecho, decodificar
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


def test_pagina_em_latin1_e_decodificada_sem_quebrar():
    assert decodificar("Contábil".encode("latin-1")) == "Contábil"


def test_pagina_em_utf8_e_decodificada_como_utf8():
    assert decodificar("Contábil".encode()) == "Contábil"


def test_trecho_com_elisao_confere_cada_parte():
    html = "<p>A startup tem mais de 14 mil escritórios parceiros.</p><p>Outro texto.</p>"
    html += "<p>O run rate indicava R$ 44 milhões nos próximos 12 meses.</p>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "mais de 14 mil escritórios parceiros ... R$ 44 milhões nos"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_trecho_com_uma_parte_que_nao_esta_na_pagina_falha():
    html = "<p>A startup tem mais de 14 mil escritórios parceiros.</p>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = (
        "mais de 14 mil escritórios parceiros ... 23,000 final clients"
    )

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is False


def test_trecho_transcrito_sem_acentos_e_encontrado():
    html = "<p>O custo dos serviços contábeis no Brasil varia bastante.</p>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "O custo dos servicos contabeis no Brasil"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_espaco_antes_de_virgula_vindo_de_link_nao_quebra_a_conferencia():
    html = '<p>buscam <a href="/nfe">NF-e</a> , NFS-e e CT-e nas bases da SEFAZ</p>'
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "buscam NF-e, NFS-e e CT-e nas bases da SEFAZ"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_anotacao_do_coletor_entre_colchetes_separa_as_partes():
    html = "<h2>Produto</h2><p>busca automática de notas</p><p>relatório de crédito</p>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = (
        "[seção do produto] busca automática de notas [lista] relatório de crédito"
    )

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_trecho_tirado_de_json_ld_e_encontrado_no_texto_cru():
    html = '<script type="application/ld+json">{"name": "Calima Pro", "price": "399"}</script>'
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = '"name": "Calima Pro", "price": "399"'

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_aspas_que_o_coletor_omitiu_nao_quebram_a_conferencia():
    html = "<p>o ‘run rate’ da Omie indicava R$ 44 milhões</p>"
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "o run rate da Omie indicava R$ 44 milhões"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True


def test_trecho_de_aria_label_e_encontrado():
    html = '<div aria-label="Avaliado com 4,4 de 5 estrelas"><span>4,4</span></div>'
    fato = novo(FATO)
    fato["fonte"]["citacao_literal"] = "Avaliado com 4,4 de 5 estrelas"

    resultado = conferir_trecho(fato, _baixador(html))

    assert resultado.trecho_encontrado is True

"""Conferência mecânica de citações: o trecho literal está mesmo na página citada?

É a metade barata da verificação. A outra metade (o trecho sustenta a alegação?) é
julgamento e fica com o subagente verificador. Um resumo da WebFetch não serve aqui,
porque é texto reescrito por um modelo: a página é baixada com curl e comparada crua.
"""

from __future__ import annotations

import html
import re
import subprocess
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass

TEMPO_LIMITE_SEGUNDOS = 25
USER_AGENT = "harness-oportunidades/0.1 (pesquisa de mercado; contato via repositorio)"
TAMANHO_MINIMO_TRECHO = 12
PADRAO_TAGS = re.compile(r"<(script|style)[^>]*>.*?</\1>|<[^>]+>", re.IGNORECASE | re.DOTALL)
PADRAO_ESPACOS = re.compile(r"\s+")
PADRAO_ESPACO_ANTES_DE_PONTUACAO = re.compile(r"\s+([,.;:!?])")
# Elisões e anotações do coletor ("[tabela 3]", "[seção do produto]") separam as partes.
PADRAO_ELISAO = re.compile(r"\[[^\]]*\]|\(\.\.\.\)|\.\.\.|…")
ASPAS = "\"'“”‘’«»"
ASSINATURA_PDF = b"%PDF"
# Dados que a página declara sem mostrar como texto: JSON-LD e atributos descritivos.
# Script comum continua de fora (variável de JS não é o que a página diz).
PADRAO_JSON_LD = re.compile(
    r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", re.IGNORECASE | re.DOTALL
)
PADRAO_ATRIBUTO_DESCRITIVO = re.compile(
    r"\b(?:aria-label|alt|title|content)\s*=\s*(\"[^\"]*\"|'[^']*')", re.IGNORECASE
)


@dataclass(frozen=True)
class Pagina:
    """Resultado de baixar uma URL."""

    ok: bool
    texto: str
    erro: str | None = None


@dataclass(frozen=True)
class ConferenciaTrecho:
    """Resultado da conferência de um fato."""

    fato: str
    url: str
    trecho_encontrado: bool | None
    detalhe: str


Baixador = Callable[[str], Pagina]


def baixar_com_curl(url: str) -> Pagina:
    """Baixa uma URL com curl (respeita o proxy e o CA configurados no ambiente)."""
    comando = [
        "curl",
        "-sL",
        "--fail",
        "--compressed",
        "--max-time",
        str(TEMPO_LIMITE_SEGUNDOS),
        "-A",
        USER_AGENT,
        url,
    ]
    resultado = subprocess.run(comando, capture_output=True, check=False)  # noqa: S603
    if resultado.returncode != 0:
        return Pagina(ok=False, texto="", erro=f"curl saiu com {resultado.returncode}")
    if resultado.stdout.startswith(ASSINATURA_PDF):
        return _texto_de_pdf(resultado.stdout)
    return Pagina(ok=True, texto=decodificar(resultado.stdout))


def _texto_de_pdf(conteudo: bytes) -> Pagina:
    try:
        resultado = subprocess.run(  # noqa: S603
            ["pdftotext", "-layout", "-", "-"],  # noqa: S607
            input=conteudo,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return Pagina(ok=False, texto="", erro="PDF: instale pdftotext (poppler-utils)")
    if resultado.returncode != 0:
        return Pagina(ok=False, texto="", erro=f"pdftotext saiu com {resultado.returncode}")
    return Pagina(ok=True, texto=decodificar(resultado.stdout))


def decodificar(conteudo: bytes) -> str:
    """Decodifica a página sem quebrar: UTF-8 quando válido, senão Latin-1 (sites antigos)."""
    try:
        return conteudo.decode("utf-8")
    except UnicodeDecodeError:
        return conteudo.decode("latin-1")


def conferir_trecho(fato: dict, baixar: Baixador = baixar_com_curl) -> ConferenciaTrecho:
    """Confere se o `citacao_literal` de um fato aparece no texto da página da fonte.

    Args:
        fato: Registro de fato.
        baixar: Função que baixa a URL (injetável para testes offline).

    Returns:
        `trecho_encontrado` True/False quando a página foi lida; None quando não deu
        para conferir (sem trecho, trecho curto demais, leitura de resumo ou página
        inacessível), com o motivo em `detalhe`.
    """
    fonte = fato.get("fonte", {})
    url, trecho = fonte.get("url", ""), fonte.get("citacao_literal", "")
    if len(_normalizar(trecho)) < TAMANHO_MINIMO_TRECHO:
        return ConferenciaTrecho(fato["id"], url, None, "sem trecho literal conferível")
    if fonte.get("leitura") == "resumo_de_busca":
        return ConferenciaTrecho(fato["id"], url, None, "trecho veio do resumo de busca")
    pagina = baixar(url)
    if not pagina.ok:
        return ConferenciaTrecho(fato["id"], url, None, f"página inacessível: {pagina.erro}")
    textos = (
        _normalizar(_texto_visivel(pagina.texto)),
        _normalizar(_texto_declarado(pagina.texto)),
    )
    ausentes = [
        parte for parte in _partes_do_trecho(trecho) if not any(parte in texto for texto in textos)
    ]
    if not ausentes:
        return ConferenciaTrecho(fato["id"], url, True, "trecho encontrado na página")
    detalhe = f"trecho não está na página (primeira parte ausente: {ausentes[0][:60]!r})"
    return ConferenciaTrecho(fato["id"], url, False, detalhe)


def _partes_do_trecho(trecho: str) -> list[str]:
    """Separa o trecho nas elisões ("...", "[...]"): cada parte tem de estar na página."""
    partes = (_normalizar(parte) for parte in PADRAO_ELISAO.split(trecho))
    return [parte for parte in partes if len(parte) >= TAMANHO_MINIMO_TRECHO]


def _texto_visivel(conteudo: str) -> str:
    return html.unescape(PADRAO_TAGS.sub(" ", conteudo))


def _texto_declarado(conteudo: str) -> str:
    blocos = PADRAO_JSON_LD.findall(conteudo)
    blocos += [valor[1:-1] for valor in PADRAO_ATRIBUTO_DESCRITIVO.findall(conteudo)]
    return html.unescape(" ".join(blocos))


def _normalizar(texto: str) -> str:
    """Compara sem depender de caixa, acentos, aspas ou espaçamento.

    Acentos saem porque coletores às vezes transcrevem sem eles ("servicos contabeis"),
    e isso não muda o que a fonte diz.
    """
    texto = unicodedata.normalize("NFKD", texto).casefold()
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.translate(str.maketrans("", "", ASPAS))
    texto = PADRAO_ESPACO_ANTES_DE_PONTUACAO.sub(r"\1", texto)
    return PADRAO_ESPACOS.sub(" ", texto).strip()

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
        "--max-time",
        str(TEMPO_LIMITE_SEGUNDOS),
        "-A",
        USER_AGENT,
        url,
    ]
    resultado = subprocess.run(comando, capture_output=True, text=True, check=False)  # noqa: S603
    if resultado.returncode != 0:
        return Pagina(ok=False, texto="", erro=f"curl saiu com {resultado.returncode}")
    return Pagina(ok=True, texto=resultado.stdout)


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
    encontrado = _normalizar(trecho) in _normalizar(_texto_visivel(pagina.texto))
    detalhe = "trecho encontrado na página" if encontrado else "trecho não está na página"
    return ConferenciaTrecho(fato["id"], url, encontrado, detalhe)


def _texto_visivel(conteudo: str) -> str:
    return html.unescape(PADRAO_TAGS.sub(" ", conteudo))


def _normalizar(texto: str) -> str:
    """Compara sem depender de caixa, acentos compostos, aspas tipográficas ou espaços."""
    texto = unicodedata.normalize("NFKC", texto).casefold()
    texto = texto.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    return PADRAO_ESPACOS.sub(" ", texto).strip()

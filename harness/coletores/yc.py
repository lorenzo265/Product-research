"""Coletor da lente 7 (arbitragem): empresas da YC ativas e sem presença no Brasil.

Fonte: diretório público da Y Combinator espelhado diariamente pelo projeto yc-oss
(JSON estático). O coletor não grava fatos: devolve candidatos para o batedor da lente 7
checar, um a um, se já existe equivalente brasileiro e qual barreira de localização há.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from dataclasses import asdict, dataclass

from harness.exceptions import HarnessError
from harness.verificacao import Pagina, baixar_com_curl

URL_EMPRESAS = "https://yc-oss.github.io/api/companies/all.json"
STATUS_ATIVO = "Active"
MARCAS_DE_BRASIL = ("brazil", "brasil", "são paulo", "sao paulo", "rio de janeiro")
MARCA_AMERICA_LATINA = "latin america"


@dataclass(frozen=True)
class Candidato:
    """Empresa candidata a arbitragem."""

    nome: str
    descricao: str
    industria: str
    subindustria: str
    time: int | None
    turma: str
    site: str
    url_yc: str
    regioes: tuple[str, ...]

    def como_dict(self) -> dict:
        """Representação serializável."""
        return {**asdict(self), "regioes": list(self.regioes)}


def baixar_empresas(baixar: Callable[[str], Pagina] = baixar_com_curl) -> list[dict]:
    """Baixa o diretório completo do yc-oss.

    Raises:
        HarnessError: se a página não abrir ou não for uma lista JSON.
    """
    pagina = baixar(URL_EMPRESAS)
    if not pagina.ok:
        raise HarnessError(f"yc-oss inacessível: {pagina.erro}")
    try:
        empresas = json.loads(pagina.texto)
    except json.JSONDecodeError as erro:
        raise HarnessError(f"yc-oss devolveu JSON inválido: {erro}") from erro
    if not isinstance(empresas, list):
        raise HarnessError("yc-oss devolveu algo que não é uma lista de empresas")
    return empresas


def filtrar_candidatos(
    empresas: Iterable[dict],
    termos: Iterable[str] = (),
    industria: str | None = None,
    time_maximo: int | None = None,
    incluir_america_latina: bool = False,
) -> list[Candidato]:
    """Filtra empresas ativas sem presença no Brasil, por termos, indústria e tamanho.

    Args:
        empresas: Registros do yc-oss.
        termos: Palavras que precisam aparecer na descrição, tags ou subindústria (qualquer uma).
        industria: Indústria exata do diretório (ex.: "B2B", "Fintech"); None aceita todas.
        time_maximo: Tamanho máximo do time; times pequenos indicam produto replicável.
        incluir_america_latina: Se False, exclui quem já declara presença na América Latina.

    Returns:
        Candidatos, do menor time para o maior.
    """
    termos_normalizados = [termo.casefold() for termo in termos]
    candidatos = []
    for empresa in empresas:
        if empresa.get("status") != STATUS_ATIVO or _tem_presenca_no_brasil(empresa):
            continue
        regioes = tuple(empresa.get("regions") or ())
        if not incluir_america_latina and any(
            r.casefold() == MARCA_AMERICA_LATINA for r in regioes
        ):
            continue
        if industria and industria not in (empresa.get("industries") or [empresa.get("industry")]):
            continue
        time = empresa.get("team_size")
        if time_maximo is not None and (time is None or time > time_maximo):
            continue
        if termos_normalizados and not _menciona(empresa, termos_normalizados):
            continue
        candidatos.append(
            Candidato(
                nome=empresa.get("name", ""),
                descricao=empresa.get("one_liner") or "",
                industria=empresa.get("industry") or "",
                subindustria=empresa.get("subindustry") or "",
                time=time,
                turma=empresa.get("batch") or "",
                site=empresa.get("website") or "",
                url_yc=empresa.get("url") or "",
                regioes=regioes,
            )
        )
    return sorted(candidatos, key=lambda c: (c.time is None, c.time or 0, c.nome))


def _tem_presenca_no_brasil(empresa: dict) -> bool:
    texto = " ".join([empresa.get("all_locations") or "", *(empresa.get("regions") or [])])
    return any(marca in texto.casefold() for marca in MARCAS_DE_BRASIL)


def _menciona(empresa: dict, termos: list[str]) -> bool:
    texto = " ".join(
        [
            empresa.get("one_liner") or "",
            empresa.get("long_description") or "",
            empresa.get("subindustry") or "",
            *(empresa.get("tags") or []),
        ]
    ).casefold()
    return any(termo in texto for termo in termos)

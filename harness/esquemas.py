"""Tipos de registro do harness e validação contra os JSON Schemas de `schemas/`."""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import cache
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from harness.exceptions import TipoDesconhecido

DIR_SCHEMAS_PADRAO = Path(__file__).resolve().parent.parent / "schemas"


@dataclass(frozen=True)
class TipoRegistro:
    """Descreve onde um tipo de registro mora e como seus ids são formados.

    Attributes:
        nome: Nome do tipo (fato, sinal, veredito, teste, cartao).
        arquivo: Caminho do JSONL relativo à raiz, ou None para cartões (um arquivo por pasta).
        schema: Nome do arquivo de schema em `schemas/`.
        prefixo: Prefixo do id (f, s, v, t, OP).
        anual: Se o id carrega o ano (f-2026-0001) ou não (OP-0001).
    """

    nome: str
    arquivo: str | None
    schema: str
    prefixo: str
    anual: bool


TIPOS: dict[str, TipoRegistro] = {
    "fato": TipoRegistro("fato", "data/fatos.jsonl", "fato.schema.json", "f", anual=True),
    "sinal": TipoRegistro("sinal", "data/sinais.jsonl", "sinal.schema.json", "s", anual=True),
    "veredito": TipoRegistro(
        "veredito", "data/vereditos.jsonl", "veredito.schema.json", "v", anual=True
    ),
    "teste": TipoRegistro("teste", "data/testes.jsonl", "teste.schema.json", "t", anual=True),
    "cartao": TipoRegistro("cartao", None, "cartao.schema.json", "OP", anual=False),
}

TIPOS_JSONL = tuple(nome for nome, tipo in TIPOS.items() if tipo.arquivo is not None)


def tipo_registro(nome: str) -> TipoRegistro:
    """Devolve a descrição do tipo.

    Raises:
        TipoDesconhecido: se o nome não for um dos tipos do harness.
    """
    try:
        return TIPOS[nome]
    except KeyError:
        validos = ", ".join(TIPOS)
        raise TipoDesconhecido(f"tipo '{nome}' não existe; use um de: {validos}") from None


@cache
def _validador(nome_schema: str, dir_schemas: Path) -> Draft202012Validator:
    schema = json.loads((dir_schemas / nome_schema).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def erros_de_schema(tipo: str, registro: dict, dir_schemas: Path = DIR_SCHEMAS_PADRAO) -> list[str]:
    """Lista os erros de schema de um registro, em texto legível.

    Args:
        tipo: Nome do tipo do registro.
        registro: O registro a validar.
        dir_schemas: Pasta dos JSON Schemas.

    Returns:
        Uma mensagem por erro, com o caminho do campo; lista vazia se válido.
    """
    validador = _validador(tipo_registro(tipo).schema, dir_schemas)
    erros = sorted(validador.iter_errors(registro), key=lambda erro: list(erro.absolute_path))
    return [f"{_caminho(erro.absolute_path)}: {erro.message}" for erro in erros]


def _caminho(partes) -> str:
    texto = ".".join(str(parte) for parte in partes)
    return texto or "(raiz)"

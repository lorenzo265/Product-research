"""Roda o juiz como nos evals: diretório neutro, sem CLAUDE.md nem git, via `claude -p`.

O diretório neutro contém só o que a entrada do juiz lista (dossiê, fatos, memorandos,
contrato e referências do método). É o isolamento mais forte disponível: nenhum CLAUDE.md,
nenhum histórico de git com nome de oportunidade, nenhuma conversa.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

from harness.esquemas import DIR_SCHEMAS_PADRAO
from harness.julgamento import DIR_REFERENCIAS, montar_pacote_juiz

RAIZ = Path(__file__).resolve().parent.parent
ID_OPORTUNIDADE_EVAL = "OP-9001"
PASTA_OPORTUNIDADE_EVAL = f"{ID_OPORTUNIDADE_EVAL}-caso-de-eval"
FERRAMENTAS_PROIBIDAS = "Bash,Write,Edit,MultiEdit,NotebookEdit,WebSearch,WebFetch,Agent,Skill"
ORCAMENTO_USD_POR_EXECUCAO = "3"
CAMPOS_PREENCHIDOS_PELA_CLI = ("id", "oportunidade", "data")
# Palavras-chave de schema que a saída estruturada pode não aceitar; a validação completa
# acontece depois, contra o schema original.
CHAVES_DE_LIMITE = (
    "minLength",
    "maxLength",
    "minimum",
    "maximum",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "pattern",
    "format",
    "minItems",
    "maxItems",
    "uniqueItems",
    "description",
    "title",
    "$id",
    "$schema",
)

Executor = Callable[..., subprocess.CompletedProcess]


@dataclass(frozen=True)
class ResultadoJuiz:
    """Uma execução do juiz."""

    veredito: dict | None
    custo_usd: float | None
    erro: str | None


def preparar_diretorio_neutro(
    caso: Path,
    destino: Path,
    hoje: date,
    tese_de_terceiro: str | None = None,
    semente: int | None = None,
) -> str:
    """Monta um repositório mínimo com o caso e devolve a mensagem para o juiz.

    Args:
        caso: Pasta do caso (contrato.json, fatos.jsonl, dossie-*.md, memorandos/).
        destino: Pasta vazia onde montar o diretório neutro.
        hoje: Data da rodada.
        tese_de_terceiro: Se dada, substitui a tese do contrato (usado nos braços do eval).
        semente: Semente do sorteio A/B.

    Returns:
        A mensagem exata a passar ao juiz.
    """
    shutil.copytree(RAIZ / DIR_REFERENCIAS, destino / DIR_REFERENCIAS)
    (destino / "data").mkdir(parents=True)
    shutil.copy(caso / "fatos.jsonl", destino / "data" / "fatos.jsonl")
    pasta = destino / "oportunidades" / PASTA_OPORTUNIDADE_EVAL
    pasta.mkdir(parents=True)
    for dossie in caso.glob("dossie-*.md"):
        shutil.copy(dossie, pasta / dossie.name)
    shutil.copytree(caso / "memorandos", pasta / "memorandos")
    contrato = json.loads((caso / "contrato.json").read_text(encoding="utf-8"))
    contrato["oportunidade"] = ID_OPORTUNIDADE_EVAL
    if tese_de_terceiro is not None:
        contrato["tese_de_terceiro"] = tese_de_terceiro
    (pasta / "contrato.json").write_text(
        json.dumps(contrato, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return montar_pacote_juiz(destino, pasta, hoje, semente=semente).mensagem


def carregar_agente(nome: str) -> tuple[dict, str]:
    """Lê frontmatter e corpo de `.claude/agents/<nome>.md`."""
    texto = (RAIZ / ".claude" / "agents" / f"{nome}.md").read_text(encoding="utf-8")
    _, frontmatter, corpo = texto.split("---\n", 2)
    return yaml.safe_load(frontmatter), corpo.strip()


def schema_saida_juiz() -> dict:
    """Schema do veredito sem os campos que a CLI preenche e sem limites numéricos."""
    schema = json.loads((DIR_SCHEMAS_PADRAO / "veredito.schema.json").read_text(encoding="utf-8"))
    schema["required"] = [c for c in schema["required"] if c not in CAMPOS_PREENCHIDOS_PELA_CLI]
    for campo in CAMPOS_PREENCHIDOS_PELA_CLI:
        schema["properties"].pop(campo, None)
    return _sem_limites(schema)


def rodar_juiz(
    diretorio: Path, mensagem: str, executar: Executor = subprocess.run
) -> ResultadoJuiz:
    """Executa o juiz com o prompt, modelo e esforço do `.claude/agents/juiz.md`."""
    frontmatter, corpo = carregar_agente("juiz")
    comando = [
        "claude",
        "-p",
        mensagem,
        "--system-prompt",
        corpo,
        "--model",
        str(frontmatter["model"]),
        "--effort",
        str(frontmatter.get("effort", "high")),
        "--disallowedTools",
        FERRAMENTAS_PROIBIDAS,
        "--output-format",
        "json",
        "--json-schema",
        json.dumps(schema_saida_juiz(), ensure_ascii=False),
        "--no-session-persistence",
        "--max-budget-usd",
        ORCAMENTO_USD_POR_EXECUCAO,
    ]
    processo = executar(comando, cwd=diretorio, capture_output=True, text=True, check=False)
    try:
        saida = json.loads(processo.stdout)
    except json.JSONDecodeError:
        return ResultadoJuiz(None, None, f"saída não é JSON: {processo.stderr[-500:]}")
    custo = saida.get("total_cost_usd")
    if saida.get("is_error"):
        return ResultadoJuiz(None, custo, str(saida.get("result"))[:500])
    veredito = saida.get("structured_output") or _json_do_texto(saida.get("result", ""))
    if veredito is None:
        return ResultadoJuiz(None, custo, "juiz não devolveu JSON")
    return ResultadoJuiz(veredito, custo, None)


def _json_do_texto(texto: str) -> dict | None:
    limpo = texto.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        valor = json.loads(limpo)
    except json.JSONDecodeError:
        return None
    return valor if isinstance(valor, dict) else None


def _sem_limites(no: object) -> object:
    if isinstance(no, dict):
        return {k: _sem_limites(v) for k, v in no.items() if k not in CHAVES_DE_LIMITE}
    if isinstance(no, list):
        return [_sem_limites(item) for item in no]
    return no

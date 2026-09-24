"""Eval E3 · roteamento: cada pedido em linguagem natural vai para o comando certo?

Roda cada pedido com `claude -p` na raiz do repositório (com CLAUDE.md, skills e hooks do
projeto), para depois da primeira rodada de ferramentas e lê qual skill foi chamada.
Também marca disparo de skills sincronizadas do claude.ai com nome parecido (A-06).

Aprova quando cada pedido acerta em pelo menos 2 de 3 execuções, nenhum quase-acerto
dispara comando em mais de 1 de 3, e não há disparo das skills sincronizadas.

Uso:
    python3 -m evals.roteamento --repeticoes 1
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import date

from evals.juiz_isolado import RAIZ

CASOS = RAIZ / "evals" / "roteamento.json"
DIR_RESULTADOS = RAIZ / "evals" / "resultados"
SKILLS_SINCRONIZADAS = ("pesquisador-de-mercado", "analista-imparcial")
ORCAMENTO_USD = "1"


def skill_chamada(pedido: str) -> tuple[str | None, float | None]:
    """Primeira skill que a sessão principal chama para o pedido, e o custo."""
    comando = [
        "claude",
        "-p",
        pedido,
        "--max-turns",
        "1",
        "--output-format",
        "stream-json",
        "--verbose",
        "--no-session-persistence",
        "--max-budget-usd",
        ORCAMENTO_USD,
    ]
    processo = subprocess.run(comando, cwd=RAIZ, capture_output=True, text=True, check=False)
    skill, custo = None, None
    for linha in processo.stdout.splitlines():
        try:
            evento = json.loads(linha)
        except json.JSONDecodeError:
            continue
        if evento.get("type") == "result":
            custo = evento.get("total_cost_usd")
        if skill is None and evento.get("type") == "assistant":
            for bloco in evento.get("message", {}).get("content", []):
                if bloco.get("type") == "tool_use" and bloco.get("name") == "Skill":
                    skill = bloco.get("input", {}).get("skill")
                    break
    return skill, custo


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada; devolve 0 se o roteamento aprova."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--repeticoes", type=int, default=1)
    args = parser.parse_args(argv)
    casos = json.loads(CASOS.read_text(encoding="utf-8"))
    resultados, custo_total, aprovado = [], 0.0, True
    for caso in casos:
        chamadas = []
        for _ in range(args.repeticoes):
            skill, custo = skill_chamada(caso["pedido"])
            chamadas.append(skill)
            custo_total += custo or 0
        acertos = sum(1 for s in chamadas if (s or None) == caso["esperado"])
        sincronizadas = [s for s in chamadas if s and any(n in s for n in SKILLS_SINCRONIZADAS)]
        ok = acertos * 3 >= 2 * args.repeticoes and not sincronizadas
        aprovado &= ok
        resultados.append({**caso, "chamadas": chamadas, "acertos": acertos, "ok": ok})
        marca = "OK " if ok else "ERR"
        print(f"{marca} {caso['esperado'] or '—':12} {Counter(chamadas)} · {caso['pedido']}")
    DIR_RESULTADOS.mkdir(exist_ok=True)
    arquivo = DIR_RESULTADOS / f"{date.today().isoformat()}-roteamento.json"
    relatorio = {
        "aprovado": aprovado,
        "custo_total_usd": round(custo_total, 2),
        "casos": resultados,
    }
    arquivo.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    acertou = sum(r["ok"] for r in resultados)
    print(
        f"{acertou}/{len(resultados)} ok · custo US${custo_total:.2f} · {arquivo.relative_to(RAIZ)}"
    )
    return 0 if aprovado else 1


if __name__ == "__main__":
    sys.exit(main())

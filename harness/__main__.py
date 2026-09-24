"""CLI do harness: `python3 -m harness <comando>`.

Comandos:
    validar       valida todo o estado (use --hook dentro de hooks do Claude Code)
    novo-id       mostra o próximo id livre de um tipo
    adicionar     grava um registro novo (JSON como argumento ou via stdin)
    atualizar     altera campos de um registro, guardando histórico
    obter         mostra um registro pelo id
    novo-cartao   cria a pasta e o cartão de uma oportunidade
    portfolio     painel de todas as oportunidades e pendências
    calibracao    Brier, intervalo e calibração por faixa das previsões resolvidas
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from harness.calibracao import calibrar, extrair_previsoes, vencidas_sem_resultado
from harness.estado import DIR_OPORTUNIDADES, Repositorio
from harness.exceptions import HarnessError
from harness.portfolio import montar_painel
from harness.validacao import ERRO, validar

SAIDA_OK = 0
SAIDA_ERRO = 1
SAIDA_BLOQUEIO_HOOK = 2  # só exit 2 bloqueia e devolve a mensagem ao Claude Code
PASTAS_DE_ESTADO = ("data/", f"{DIR_OPORTUNIDADES}/")

CORPO_CARTAO_PADRAO = """
## Dor

## Evidência até aqui

## Hipóteses rivais

## Histórico
"""


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada da CLI; devolve o código de saída."""
    args = _parser().parse_args(argv)
    repositorio = Repositorio(raiz=Path(args.raiz)) if args.raiz else Repositorio()
    hoje = date.fromisoformat(args.hoje) if args.hoje else date.today()
    try:
        return args.executar(args, repositorio, hoje)
    except HarnessError as erro:
        print(f"erro: {erro}", file=sys.stderr)
        return SAIDA_ERRO


def _cmd_validar(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    evento = _ler_evento_de_hook() if args.hook else {}
    if args.hook and not _evento_toca_estado(evento):
        return SAIDA_OK
    try:
        problemas = validar(repositorio.snapshot(), hoje)
        mensagens_de_erro = [str(problema) for problema in problemas if problema.nivel == ERRO]
    except HarnessError as erro:
        problemas, mensagens_de_erro = [], [f"[erro] {erro}"]

    if args.hook:
        if not mensagens_de_erro or evento.get("stop_hook_active"):
            return SAIDA_OK
        print("Estado do harness inválido; corrija antes de seguir:", file=sys.stderr)
        print("\n".join(mensagens_de_erro), file=sys.stderr)
        return SAIDA_BLOQUEIO_HOOK

    for linha in mensagens_de_erro + [str(p) for p in problemas if p.nivel != ERRO]:
        print(linha)
    avisos = len(problemas) - len(mensagens_de_erro) if problemas else 0
    print(f"{len(mensagens_de_erro)} erro(s), {avisos} aviso(s)")
    return SAIDA_ERRO if mensagens_de_erro else SAIDA_OK


def _cmd_novo_id(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    print(repositorio.proximo_id(args.tipo, hoje))
    return SAIDA_OK


def _cmd_adicionar(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    registro = repositorio.adicionar(args.tipo, _json_do_argumento(args.json), hoje)
    print(registro["id"])
    return SAIDA_OK


def _cmd_atualizar(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    mudancas = _json_do_argumento(args.json)
    if args.tipo == "cartao":
        atualizado = repositorio.atualizar_cartao(args.id, mudancas, args.motivo, hoje)
    else:
        atualizado = repositorio.atualizar(args.tipo, args.id, mudancas, args.motivo, hoje)
    print(json.dumps(atualizado, ensure_ascii=False, indent=2))
    return SAIDA_OK


def _cmd_obter(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    print(json.dumps(repositorio.obter(args.tipo, args.id), ensure_ascii=False, indent=2))
    return SAIDA_OK


def _cmd_novo_cartao(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    corpo = Path(args.corpo).read_text(encoding="utf-8") if args.corpo else CORPO_CARTAO_PADRAO
    caminho = repositorio.criar_cartao(_json_do_argumento(args.json), corpo, hoje)
    print(caminho.relative_to(repositorio.raiz))
    return SAIDA_OK


def _cmd_portfolio(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    print(montar_painel(repositorio.snapshot(), hoje))
    return SAIDA_OK


def _cmd_calibracao(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    previsoes = extrair_previsoes(repositorio.snapshot())
    if args.trilha:
        previsoes = [previsao for previsao in previsoes if previsao.trilha == args.trilha]
    relatorio = calibrar(previsoes)
    print(f"Previsões resolvidas: {relatorio.resolvidas}")
    if relatorio.brier is not None:
        intervalo = relatorio.intervalo_brier
        faixa = f" (IC95% {intervalo[0]:.3f}–{intervalo[1]:.3f})" if intervalo else ""
        print(f"Brier: {relatorio.brier:.3f}{faixa}")
        if relatorio.skill_score is not None:
            print(f"Skill score vs. frequência observada: {relatorio.skill_score:+.2f}")
        for nivel in relatorio.faixas:
            print(
                f"  {nivel.nivel}: n={nivel.quantidade} "
                f"p média={nivel.p_media:.2f} observado={nivel.frequencia_observada:.2f}"
            )
    if not relatorio.pode_ajustar_reguas:
        print("Amostra insuficiente para ajustar réguas por calibração.")
    for previsao in vencidas_sem_resultado(previsoes, hoje):
        print(f"Resolver: {previsao.veredito} · {previsao.texto} (prazo {previsao.prazo})")
    return SAIDA_OK


def _json_do_argumento(texto: str | None) -> dict:
    bruto = sys.stdin.read() if texto in (None, "-") else texto
    try:
        valor = json.loads(bruto)
    except json.JSONDecodeError as erro:
        raise HarnessError(f"JSON inválido: {erro}") from erro
    if not isinstance(valor, dict):
        raise HarnessError("o JSON precisa ser um objeto")
    return valor


def _ler_evento_de_hook() -> dict:
    if sys.stdin.isatty():
        return {}
    bruto = sys.stdin.read().strip()
    if not bruto:
        return {}
    try:
        evento = json.loads(bruto)
    except json.JSONDecodeError:
        return {}  # entrada que não é evento de hook: valida tudo, como fora de hook
    return evento if isinstance(evento, dict) else {}


def _evento_toca_estado(evento: dict) -> bool:
    """Eventos de edição só disparam validação se o arquivo for de estado."""
    caminho = (evento.get("tool_input") or {}).get("file_path")
    if not caminho:
        return True
    return any(pasta in caminho for pasta in PASTAS_DE_ESTADO)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python3 -m harness", description=__doc__.split("\n")[0])
    parser.add_argument("--hoje", help="data de referência ISO (padrão: hoje)")
    parser.add_argument("--raiz", help="raiz do repositório de estado (padrão: este repo)")
    sub = parser.add_subparsers(required=True, metavar="comando")

    validar_ = sub.add_parser("validar", help="valida todo o estado")
    validar_.add_argument("--hook", action="store_true", help="modo hook do Claude Code")
    validar_.set_defaults(executar=_cmd_validar)

    novo_id = sub.add_parser("novo-id", help="próximo id livre de um tipo")
    novo_id.add_argument("tipo")
    novo_id.set_defaults(executar=_cmd_novo_id)

    adicionar = sub.add_parser("adicionar", help="grava um registro novo")
    adicionar.add_argument("tipo")
    adicionar.add_argument("json", nargs="?", help="registro em JSON; omita ou use - para stdin")
    adicionar.set_defaults(executar=_cmd_adicionar)

    atualizar = sub.add_parser("atualizar", help="altera campos guardando histórico")
    atualizar.add_argument("tipo")
    atualizar.add_argument("id")
    atualizar.add_argument("json", nargs="?", help="campos a mudar em JSON; omita para stdin")
    atualizar.add_argument("--motivo", required=True)
    atualizar.set_defaults(executar=_cmd_atualizar)

    obter = sub.add_parser("obter", help="mostra um registro")
    obter.add_argument("tipo")
    obter.add_argument("id")
    obter.set_defaults(executar=_cmd_obter)

    novo_cartao = sub.add_parser("novo-cartao", help="cria uma oportunidade")
    novo_cartao.add_argument("json", nargs="?", help="frontmatter em JSON; omita para stdin")
    novo_cartao.add_argument("--corpo", help="arquivo markdown com o corpo do cartão")
    novo_cartao.set_defaults(executar=_cmd_novo_cartao)

    portfolio = sub.add_parser("portfolio", help="painel do portfólio")
    portfolio.set_defaults(executar=_cmd_portfolio)

    calibracao = sub.add_parser("calibracao", help="calibração das previsões")
    calibracao.add_argument("--trilha", choices=["G", "M", "S"])
    calibracao.set_defaults(executar=_cmd_calibracao)
    return parser


if __name__ == "__main__":
    sys.exit(main())

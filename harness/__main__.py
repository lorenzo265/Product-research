"""CLI do harness: `python3 -m harness <comando>`.

Comandos:
    validar       valida todo o estado (use --hook dentro de hooks do Claude Code)
    novo-id       mostra o próximo id livre de um tipo
    adicionar     grava um registro novo (JSON como argumento ou via stdin)
    atualizar     altera campos de um registro, guardando histórico
    obter         mostra um registro pelo id
    novo-cartao   cria a pasta e o cartão de uma oportunidade
    contrato      grava (uma vez) o contrato de validação de uma oportunidade
    pacote-juiz   monta a entrada cega do juiz e imprime a mensagem a entregar a ele
    registrar-veredito  grava o JSON do juiz (encolhe p, liga ao cartão)
    conferir-trecho  baixa a fonte e confere se o trecho literal está nela
    regra-teste   tabela de GO/KILL de um teste com comprador (SPRT ou Beta-Binomial)
    coletar-yc    lente 7: empresas da YC ativas sem presença no Brasil (candidatos)
    coletar-pncp  lentes 11/4/6: compras públicas cujo objeto menciona os termos
    portfolio     painel de todas as oportunidades e pendências
    proteger-estado  hook PreToolUse: bloqueia edição direta de arquivos de estado
    calibracao    Brier, intervalo e calibração por faixa das previsões resolvidas
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

from harness.calibracao import calibrar, encolher, extrair_previsoes, vencidas_sem_resultado
from harness.coletores.pncp import ConsultaPncp, coletar_compras, resumir
from harness.coletores.yc import baixar_empresas, filtrar_candidatos
from harness.estado import DIR_OPORTUNIDADES, Repositorio
from harness.exceptions import HarnessError
from harness.julgamento import montar_pacote_juiz
from harness.portfolio import montar_painel
from harness.regras_teste import fronteiras_bayes, fronteiras_sprt
from harness.validacao import ERRO, validar
from harness.verificacao import conferir_trecho

DIR_COLETAS = "cache/coletas"  # fora do git: coleta bruta não é estado
PADRAO_ID_FATO = re.compile(r"\bf-\d{4}-\d{4}\b")
SAIDA_OK = 0
SAIDA_ERRO = 1
SAIDA_BLOQUEIO_HOOK = 2  # só exit 2 bloqueia e devolve a mensagem ao Claude Code
PASTAS_DE_ESTADO = ("data/", f"{DIR_OPORTUNIDADES}/")
# Arquivos que só mudam pela CLI, que valida schema, ids e referências antes de gravar.
PADRAO_ARQUIVO_PROTEGIDO = re.compile(
    r"(^|/)data/[^/]+\.jsonl$|(^|/)oportunidades/[^/]+/(cartao\.md|contrato\.json)$"
)
FERRAMENTAS_DE_EDICAO = ("Write", "Edit", "MultiEdit", "NotebookEdit")

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


def _cmd_contrato(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    contrato = _json_do_argumento(args.json)
    contrato.setdefault("criado_em", hoje.isoformat())
    caminho = repositorio.gravar_contrato(contrato)
    print(caminho.relative_to(repositorio.raiz))
    return SAIDA_OK


def _cmd_pacote_juiz(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    pasta = repositorio.pasta_da_oportunidade(args.id)
    pacote = montar_pacote_juiz(repositorio.raiz, pasta, hoje, semente=args.semente)
    print(pacote.mensagem)
    return SAIDA_OK


def _cmd_registrar_veredito(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    veredito = _json_do_argumento(args.json)
    veredito.update(oportunidade=args.id, data=hoje.isoformat())
    bruta = veredito.get("p_sucesso_bruta")
    if bruta is not None and "p_sucesso" not in veredito:
        veredito["p_sucesso"] = encolher(bruta, veredito["base_rate"]["p"])
    gravado = repositorio.adicionar("veredito", veredito, hoje)
    cartao = repositorio.obter("cartao", args.id)
    repositorio.atualizar_cartao(
        args.id,
        {
            "vereditos": [*cartao.get("vereditos", []), gravado["id"]],
            "travas": gravado["travas"],
        },
        f"veredito {gravado['id']} ({gravado['modo']}): {gravado['recomendacao']}",
        hoje,
    )
    p_final = gravado.get("p_sucesso")
    sufixo = f" · p_sucesso={p_final} (bruta {bruta})" if p_final is not None else ""
    print(f"{gravado['id']} · {gravado['recomendacao']}{sufixo}")
    return SAIDA_OK


def _cmd_conferir_trecho(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    fatos = {fato["id"]: fato for fato in repositorio.ler("fato")}
    ids = list(args.ids)
    if args.oportunidade:
        pasta = repositorio.pasta_da_oportunidade(args.oportunidade)
        textos = " ".join(arquivo.read_text(encoding="utf-8") for arquivo in pasta.rglob("*.md"))
        ids += sorted(set(PADRAO_ID_FATO.findall(textos)))
    desconhecidos = [id_fato for id_fato in ids if id_fato not in fatos]
    if desconhecidos:
        raise HarnessError(f"fatos inexistentes: {', '.join(desconhecidos)}")
    for id_fato in dict.fromkeys(ids):
        resultado = conferir_trecho(fatos[id_fato])
        marca = {True: "OK", False: "FALHOU", None: "?"}[resultado.trecho_encontrado]
        print(f"{marca}\t{resultado.fato}\t{resultado.detalhe}\t{resultado.url}")
    return SAIDA_OK


def _cmd_proteger_estado(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    evento = _ler_evento_de_hook()
    caminho = (evento.get("tool_input") or {}).get("file_path", "")
    if evento.get("tool_name") not in FERRAMENTAS_DE_EDICAO:
        return SAIDA_OK
    if not PADRAO_ARQUIVO_PROTEGIDO.search(caminho):
        return SAIDA_OK
    print(
        f"{caminho} é estado do harness e só muda pela CLI, que valida antes de gravar. "
        "Use python3 -m harness adicionar/atualizar/novo-cartao/contrato "
        "(veja python3 -m harness --help).",
        file=sys.stderr,
    )
    return SAIDA_BLOQUEIO_HOOK


def _cmd_regra_teste(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    if args.tipo == "sequencial":
        if args.p0 is None or args.p1 is None:
            raise HarnessError("sequencial precisa de --p0 e --p1")
        tamanhos = args.tamanhos or [100, 200, 300, 500, 750, 1000]
        fronteiras = fronteiras_sprt(args.p0, args.p1, tamanhos)
        print(f"SPRT p0={args.p0} p1={args.p1} (alfa 5%, beta 20%)")
    else:
        if args.alvo is None or args.n_max is None:
            raise HarnessError("bayes precisa de --alvo e --n-max")
        fronteiras = fronteiras_bayes(args.alvo, args.n_max)
        print(f"Beta-Binomial: GO se P(taxa > {args.alvo}) >= 0.8; KILL se <= 0.2")
    print("n\tGO com sucessos >=\tKILL com sucessos <=")
    for fronteira in fronteiras:
        go = "—" if fronteira.go_a_partir_de is None else fronteira.go_a_partir_de
        kill = "—" if fronteira.kill_ate is None else fronteira.kill_ate
        print(f"{fronteira.n}\t{go}\t{kill}")
    return SAIDA_OK


def _cmd_coletar_yc(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    candidatos = filtrar_candidatos(
        baixar_empresas(),
        termos=args.termos or (),
        industria=args.industria,
        time_maximo=args.time_max,
        incluir_america_latina=args.incluir_latam,
    )
    destino = repositorio.raiz / DIR_COLETAS / f"yc-{hoje.isoformat()}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        json.dumps([c.como_dict() for c in candidatos], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for candidato in candidatos[: args.limite]:
        print(f"{candidato.nome}\t{candidato.time}\t{candidato.turma}\t{candidato.descricao}")
    print(
        f"{len(candidatos)} candidatos (mostrando {min(args.limite, len(candidatos))}) · "
        f"lista completa em {destino.relative_to(repositorio.raiz)}"
    )
    return SAIDA_OK


def _cmd_coletar_pncp(args: argparse.Namespace, repositorio: Repositorio, hoje: date) -> int:
    consulta = ConsultaPncp(
        inicio=date.fromisoformat(args.de),
        fim=date.fromisoformat(args.ate),
        termos=tuple(args.termos),
        modalidades=tuple(args.modalidades),
        max_paginas=args.max_paginas,
    )
    resultado = coletar_compras(consulta)
    compras, lidos = resultado.compras, resultado.lidos
    destino = repositorio.raiz / DIR_COLETAS / f"pncp-{hoje.isoformat()}-{args.de}-{args.ate}.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    resumo = resumir(compras)
    conteudo = {
        "consulta": vars(args) | {"executar": None},
        "resumo": resumo,
        "compras": [c.como_dict() for c in compras],
    }
    destino.write_text(
        json.dumps(conteudo, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8"
    )
    for compra in compras[: args.limite]:
        valor = f"R${compra.valor_estimado:,.2f}" if compra.valor_estimado is not None else "—"
        print(f"{compra.publicada_em}\t{compra.uf}\t{valor}\t{compra.objeto[:110]}")
    for falha in resultado.falhas:
        print(f"coleta parcial: {falha}")
    print(f"{lidos} compras lidas · {json.dumps(resumo, ensure_ascii=False)}")
    print(f"lista completa em {destino.relative_to(repositorio.raiz)}")
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

    contrato = sub.add_parser("contrato", help="grava o contrato de validação (uma vez)")
    contrato.add_argument("json", nargs="?", help="contrato em JSON; omita para stdin")
    contrato.set_defaults(executar=_cmd_contrato)

    pacote = sub.add_parser("pacote-juiz", help="monta a entrada cega do juiz")
    pacote.add_argument("id", help="id da oportunidade (OP-0001)")
    pacote.add_argument("--semente", type=int, help="semente do sorteio A/B")
    pacote.set_defaults(executar=_cmd_pacote_juiz)

    registrar = sub.add_parser("registrar-veredito", help="grava o veredito do juiz")
    registrar.add_argument("id", help="id da oportunidade (OP-0001)")
    registrar.add_argument("json", nargs="?", help="JSON do juiz; omita para stdin")
    registrar.set_defaults(executar=_cmd_registrar_veredito)

    conferir = sub.add_parser("conferir-trecho", help="confere trechos literais na fonte")
    conferir.add_argument("ids", nargs="*", help="ids de fatos")
    conferir.add_argument("--oportunidade", help="confere todos os fatos citados nos .md da OP")
    conferir.set_defaults(executar=_cmd_conferir_trecho)

    proteger = sub.add_parser("proteger-estado", help="hook PreToolUse de proteção do estado")
    proteger.set_defaults(executar=_cmd_proteger_estado)

    regra = sub.add_parser("regra-teste", help="tabela de GO/KILL de um teste com comprador")
    regra.add_argument("tipo", choices=["sequencial", "bayes"])
    regra.add_argument("--p0", type=float, help="sequencial: taxa que significa 'não funciona'")
    regra.add_argument("--p1", type=float, help="sequencial: taxa que significa 'funciona'")
    regra.add_argument("--tamanhos", type=int, nargs="*", help="sequencial: amostras a listar")
    regra.add_argument("--alvo", type=float, help="bayes: taxa mínima de interesse")
    regra.add_argument("--n-max", type=int, help="bayes: contatos máximos")
    regra.set_defaults(executar=_cmd_regra_teste)

    yc = sub.add_parser("coletar-yc", help="lente 7: candidatos da YC sem presença no Brasil")
    yc.add_argument("--termos", nargs="*", help="palavras na descrição ou tags (qualquer uma)")
    yc.add_argument("--industria", help='indústria exata, ex.: "B2B", "Fintech", "Healthcare"')
    yc.add_argument("--time-max", type=int, help="tamanho máximo do time")
    yc.add_argument("--incluir-latam", action="store_true", help="manter quem já está na LatAm")
    yc.add_argument("--limite", type=int, default=30, help="quantos mostrar no terminal")
    yc.set_defaults(executar=_cmd_coletar_yc)

    pncp = sub.add_parser("coletar-pncp", help="compras públicas por tema (PNCP)")
    pncp.add_argument("--de", required=True, help="data inicial ISO")
    pncp.add_argument("--ate", required=True, help="data final ISO (janelas curtas)")
    pncp.add_argument("--termos", nargs="+", required=True, help="palavras no objeto da compra")
    pncp.add_argument(
        "--modalidades",
        nargs="*",
        type=int,
        default=[6, 8],
        help="6 = pregão eletrônico, 8 = dispensa",
    )
    pncp.add_argument(
        "--max-paginas", type=int, default=20, help="teto por modalidade (50 por página)"
    )
    pncp.add_argument("--limite", type=int, default=20, help="quantas mostrar no terminal")
    pncp.set_defaults(executar=_cmd_coletar_pncp)

    portfolio = sub.add_parser("portfolio", help="painel do portfólio")
    portfolio.set_defaults(executar=_cmd_portfolio)

    calibracao = sub.add_parser("calibracao", help="calibração das previsões")
    calibracao.add_argument("--trilha", choices=["G", "M", "S"])
    calibracao.set_defaults(executar=_cmd_calibracao)
    return parser


if __name__ == "__main__":
    sys.exit(main())

"""Painel do portfólio: todas as oportunidades por trilha e estágio, e o que está pendente."""

from __future__ import annotations

from datetime import date

from harness.calibracao import extrair_previsoes, vencidas_sem_resultado
from harness.validacao import Cartao, Snapshot

ORDEM_ESTAGIOS = (
    "oportunidade",
    "kill_barato",
    "veredito",
    "oferta",
    "teste",
    "construir",
    "lancar",
    "aprender",
)
NOMES_TRILHAS = {"G": "G · Grandes problemas", "M": "M · Micro-SaaS", "S": "S · Serviço com IA"}
STATUS_EM_ANDAMENTO = ("ativa", "pausada")


def montar_painel(snapshot: Snapshot, hoje: date) -> str:
    """Monta o painel em markdown.

    Args:
        snapshot: Estado carregado.
        hoje: Data de referência para revisões e previsões vencidas.

    Returns:
        Markdown com contagens, oportunidades em andamento por trilha, pendências e cadáveres.
    """
    em_andamento = [c for c in snapshot.cartoes if c.campos.get("status") in STATUS_EM_ANDAMENTO]
    cadaveres = [c for c in snapshot.cartoes if c.campos.get("status") == "cadaver"]
    lancadas = [c for c in snapshot.cartoes if c.campos.get("status") == "lancada"]

    linhas = [
        f"# Portfólio · {hoje.isoformat()}",
        "",
        f"**{len(em_andamento)}** em andamento · **{len(lancadas)}** lançadas · "
        f"**{len(cadaveres)}** cadáveres · **{len(snapshot.de('sinal'))}** sinais · "
        f"**{len(snapshot.de('fato'))}** fatos",
        "",
    ]
    linhas += _secao_pendencias(snapshot, em_andamento, hoje)
    for trilha, nome in NOMES_TRILHAS.items():
        cartoes = [c for c in em_andamento if c.campos.get("trilha") == trilha]
        if cartoes:
            linhas += [f"## {nome}", "", *_tabela(cartoes), ""]
    if cadaveres:
        linhas += ["## Cadáveres", ""]
        linhas += [
            f"- {c.campos['id']} · {c.campos['titulo']}: {c.campos.get('motivo_morte')}"
            for c in cadaveres
        ]
        linhas.append("")
    return "\n".join(linhas)


def _secao_pendencias(snapshot: Snapshot, em_andamento: list[Cartao], hoje: date) -> list[str]:
    revisoes = [c for c in em_andamento if date.fromisoformat(str(c.campos["revisar_em"])) < hoje]
    previsoes = vencidas_sem_resultado(extrair_previsoes(snapshot), hoje)
    testes_abertos = [t for t in snapshot.de("teste") if t.get("decisao") is None]
    if not (revisoes or previsoes or testes_abertos):
        return []
    linhas = ["## Pendências", ""]
    linhas += [
        f"- Revisão vencida: {c.campos['id']} · {c.campos['titulo']} "
        f"(desde {c.campos['revisar_em']})"
        for c in revisoes
    ]
    linhas += [
        f"- Previsão para resolver: {p.veredito} · {p.texto} (prazo {p.prazo})" for p in previsoes
    ]
    linhas += [
        f"- Teste sem decisão: {t['id']} · {t['oportunidade']} · {t['hipotese']}"
        for t in testes_abertos
    ]
    return [*linhas, ""]


def _tabela(cartoes: list[Cartao]) -> list[str]:
    ordenados = sorted(cartoes, key=lambda c: ORDEM_ESTAGIOS.index(c.campos["estagio"]))
    linhas = [
        "| Id | Oportunidade | Estágio | Travas | Próximo passo | Revisar em |",
        "|---|---|---|---|---|---|",
    ]
    for cartao in ordenados:
        campos = cartao.campos
        travas = "; ".join(campos.get("travas", [])) or "—"
        linhas.append(
            f"| {campos['id']} | {campos['titulo']} | {campos['estagio']} | {travas} | "
            f"{campos['proximo_passo']} | {campos['revisar_em']} |"
        )
    return linhas

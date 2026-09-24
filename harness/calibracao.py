"""Calibração: quão bem as probabilidades dos vereditos batem com o que aconteceu.

Com poucas previsões resolvidas o Brier é quase só ruído (erro padrão ~0,03 com n=30),
por isso o relatório sempre traz intervalo de confiança e só libera ajuste de réguas a
partir de `MINIMO_PARA_AJUSTAR_REGUAS` previsões resolvidas.
"""

from __future__ import annotations

import math
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date

from harness.validacao import FAIXAS_NIVEL, Snapshot

MINIMO_PARA_AJUSTAR_REGUAS = 100
Z_95 = 1.96
# Fração do desvio (em log-odds) entre juiz e taxa-base que é mantida. Modelos atuais saem
# superconfiantes; até haver ~100 previsões resolvidas, encolhemos em direção à taxa-base.
FATOR_ENCOLHIMENTO_PADRAO = 0.7


@dataclass(frozen=True)
class Previsao:
    """Uma previsão datada tirada de um veredito."""

    veredito: str
    trilha: str
    texto: str
    p: float
    prazo: str
    resultado: bool | None


@dataclass(frozen=True)
class FaixaCalibracao:
    """Previsões resolvidas que caíram numa faixa de probabilidade."""

    nivel: str
    quantidade: int
    p_media: float
    frequencia_observada: float


@dataclass(frozen=True)
class RelatorioCalibracao:
    """Resultado da calibração de um conjunto de previsões resolvidas.

    Attributes:
        resolvidas: Quantidade de previsões com resultado.
        brier: Brier médio (0 é perfeito; 0,25 é chutar 50% sempre).
        intervalo_brier: Intervalo de 95% do Brier médio.
        brier_referencia: Brier de quem previsse sempre a frequência observada.
        skill_score: 1 - brier/brier_referencia; > 0 significa melhor que a referência.
        faixas: Calibração por faixa de nível do analista.
        pode_ajustar_reguas: Se já há amostra para mexer em réguas por calibração.
    """

    resolvidas: int
    brier: float | None
    intervalo_brier: tuple[float, float] | None
    brier_referencia: float | None
    skill_score: float | None
    faixas: list[FaixaCalibracao]
    pode_ajustar_reguas: bool


def encolher(p_bruta: float, taxa_base: float, fator: float = FATOR_ENCOLHIMENTO_PADRAO) -> float:
    """Puxa uma probabilidade em direção à taxa-base, em log-odds.

    Args:
        p_bruta: Probabilidade do juiz, entre 0 e 1 exclusivos.
        taxa_base: Probabilidade da classe de referência, entre 0 e 1 exclusivos.
        fator: Fração do desvio mantida (1 mantém o juiz; 0 devolve a taxa-base).

    Returns:
        A probabilidade encolhida, arredondada em 3 casas.
    """
    log_odds = _logit(taxa_base) + fator * (_logit(p_bruta) - _logit(taxa_base))
    return round(1 / (1 + math.exp(-log_odds)), 3)


def _logit(p: float) -> float:
    return math.log(p / (1 - p))


def extrair_previsoes(snapshot: Snapshot) -> list[Previsao]:
    """Achata as previsões de todos os vereditos."""
    return [
        Previsao(
            veredito=veredito["id"],
            trilha=veredito["trilha"],
            texto=previsao["previsao"],
            p=previsao["p"],
            prazo=previsao["prazo"],
            resultado=previsao["resultado"],
        )
        for veredito in snapshot.de("veredito")
        for previsao in veredito.get("previsoes", [])
    ]


def vencidas_sem_resultado(previsoes: Iterable[Previsao], hoje: date) -> list[Previsao]:
    """Previsões cujo prazo passou e ainda não foram resolvidas."""
    return [
        previsao
        for previsao in previsoes
        if previsao.resultado is None and date.fromisoformat(previsao.prazo) < hoje
    ]


def calibrar(previsoes: Iterable[Previsao]) -> RelatorioCalibracao:
    """Calcula Brier, intervalo, skill score e calibração por faixa das previsões resolvidas."""
    resolvidas = [previsao for previsao in previsoes if previsao.resultado is not None]
    n = len(resolvidas)
    if n == 0:
        return RelatorioCalibracao(0, None, None, None, None, [], pode_ajustar_reguas=False)

    erros = [(previsao.p - float(previsao.resultado)) ** 2 for previsao in resolvidas]
    brier = sum(erros) / n
    frequencia = sum(float(previsao.resultado) for previsao in resolvidas) / n
    referencia = frequencia * (1 - frequencia)
    return RelatorioCalibracao(
        resolvidas=n,
        brier=brier,
        intervalo_brier=_intervalo_da_media(erros),
        brier_referencia=referencia,
        skill_score=1 - brier / referencia if referencia > 0 else None,
        faixas=_faixas(resolvidas),
        pode_ajustar_reguas=n >= MINIMO_PARA_AJUSTAR_REGUAS,
    )


def _intervalo_da_media(valores: list[float]) -> tuple[float, float] | None:
    n = len(valores)
    if n < 2:  # noqa: PLR2004 - variância amostral exige duas observações
        return None
    media = sum(valores) / n
    variancia = sum((valor - media) ** 2 for valor in valores) / (n - 1)
    margem = Z_95 * math.sqrt(variancia / n)
    return max(0.0, media - margem), media + margem


def _faixas(resolvidas: list[Previsao]) -> list[FaixaCalibracao]:
    faixas = []
    for nivel, (minimo, maximo) in FAIXAS_NIVEL.items():
        dentro = [
            previsao
            for previsao in resolvidas
            if minimo <= previsao.p < maximo or (maximo == 1.0 and previsao.p == maximo)
        ]
        if dentro:
            faixas.append(
                FaixaCalibracao(
                    nivel=nivel,
                    quantidade=len(dentro),
                    p_media=sum(previsao.p for previsao in dentro) / len(dentro),
                    frequencia_observada=sum(float(previsao.resultado) for previsao in dentro)
                    / len(dentro),
                )
            )
    return faixas

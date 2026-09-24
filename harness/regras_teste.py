"""Regras de decisão dos testes com comprador, calculadas antes do teste começar.

Dois casos:
- tráfego web: teste sequencial de Wald (SPRT) entre p0 ("não funciona") e p1 ("funciona");
- poucas contas B2B: posterior Beta-Binomial com prior uniforme, GO se P(taxa > alvo) for
  alta e KILL se for baixa.

As funções devolvem, para cada tamanho de amostra, quantos sucessos bastam para GO e até
quantos significam KILL, para que a tabela entre no Test Card antes dos dados.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

ALFA_PADRAO = 0.05  # chance de GO quando a taxa real é p0
BETA_PADRAO = 0.20  # chance de KILL quando a taxa real é p1
PROBABILIDADE_GO = 0.8
PROBABILIDADE_KILL = 0.2


@dataclass(frozen=True)
class Fronteira:
    """Limites de decisão para uma amostra de tamanho `n`.

    Attributes:
        n: Tamanho da amostra até aqui.
        go_a_partir_de: Sucessos que já decidem GO (None se ainda impossível).
        kill_ate: Sucessos que ainda decidem KILL (None se KILL já impossível).
    """

    n: int
    go_a_partir_de: int | None
    kill_ate: int | None


def fronteiras_sprt(
    p0: float, p1: float, tamanhos: list[int], alfa: float = ALFA_PADRAO, beta: float = BETA_PADRAO
) -> list[Fronteira]:
    """Fronteiras do teste sequencial de Wald para uma taxa binária.

    Args:
        p0: Taxa que significa "não funciona" (ex.: 0,003 para pré-venda).
        p1: Taxa que significa "funciona" (ex.: 0,01).
        tamanhos: Tamanhos de amostra para os quais listar as fronteiras.
        alfa: Erro tipo I aceito (GO quando a taxa real é p0).
        beta: Erro tipo II aceito (KILL quando a taxa real é p1).

    Returns:
        Uma fronteira por tamanho pedido.
    """
    if not 0 < p0 < p1 < 1:
        raise ValueError("é preciso 0 < p0 < p1 < 1")
    limite_go = math.log((1 - beta) / alfa)
    limite_kill = math.log(beta / (1 - alfa))
    ganho_sucesso = math.log(p1 / p0)
    perda_fracasso = math.log((1 - p1) / (1 - p0))
    fronteiras = []
    for n in tamanhos:
        # LLR(k) = k*ganho + (n-k)*perda, crescente em k.
        k_go = math.ceil((limite_go - n * perda_fracasso) / (ganho_sucesso - perda_fracasso))
        k_kill = math.floor((limite_kill - n * perda_fracasso) / (ganho_sucesso - perda_fracasso))
        fronteiras.append(
            Fronteira(
                n=n,
                go_a_partir_de=k_go if 0 <= k_go <= n else None,
                kill_ate=k_kill if k_kill >= 0 else None,
            )
        )
    return fronteiras


def prob_taxa_acima(sucessos: int, n: int, alvo: float) -> float:
    """P(taxa > alvo) com prior uniforme Beta(1,1), depois de `sucessos` em `n`."""
    a, b = sucessos + 1, n - sucessos + 1
    # P(X <= alvo) para Beta(a, b) com a, b inteiros = P(Binomial(a+b-1, alvo) >= a).
    total = a + b - 1
    cdf = sum(
        math.comb(total, j) * alvo**j * (1 - alvo) ** (total - j) for j in range(a, total + 1)
    )
    return 1 - cdf


def fronteiras_bayes(
    alvo: float,
    n_max: int,
    prob_go: float = PROBABILIDADE_GO,
    prob_kill: float = PROBABILIDADE_KILL,
) -> list[Fronteira]:
    """Fronteiras Beta-Binomial para funis de contas pequenos.

    Args:
        alvo: Taxa mínima que interessa (ex.: 0,10 de depósitos por decisor contatado).
        n_max: Número máximo de contatos do teste.
        prob_go: GO quando P(taxa > alvo) atinge este valor.
        prob_kill: KILL quando P(taxa > alvo) cai a este valor ou abaixo.

    Returns:
        Uma fronteira para cada n de 1 a `n_max`.
    """
    fronteiras = []
    for n in range(1, n_max + 1):
        probabilidades = [prob_taxa_acima(k, n, alvo) for k in range(n + 1)]
        go = next((k for k, p in enumerate(probabilidades) if p >= prob_go), None)
        kills = [k for k, p in enumerate(probabilidades) if p <= prob_kill]
        fronteiras.append(Fronteira(n=n, go_a_partir_de=go, kill_ate=max(kills) if kills else None))
    return fronteiras

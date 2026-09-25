"""Fila do radar: sinais ordenados pela força mecânica da evidência, sem julgar nenhum."""

from __future__ import annotations

from dataclasses import dataclass

from harness.validacao import Snapshot

TAMANHO_MAXIMO_DOR = 90


@dataclass(frozen=True)
class ForcaDoSinal:
    """Contagens que o /radar usa para ordenar sinais. Não é nota: é fila de trabalho.

    Attributes:
        sinal: Registro do sinal.
        cifra: O sinal tem dinheiro associado.
        cifra_integral: O fato da cifra foi lido na página, e não num resumo de busca.
        recorrencia: O sinal descreve recorrência.
        fatos: Quantos fatos sustentam o sinal.
        integrais: Quantos desses fatos têm leitura integral.
        tier1: Quantos desses fatos vêm de fonte Tier 1.
    """

    sinal: dict
    cifra: bool
    cifra_integral: bool
    recorrencia: bool
    fatos: int
    integrais: int
    tier1: int

    def chave(self) -> tuple:
        """Ordem da fila: cifra lida na página, cifra, recorrência, leitura integral, Tier 1."""
        return (
            self.cifra_integral,
            self.cifra,
            self.recorrencia,
            self.integrais,
            self.tier1,
            self.fatos,
        )


def medir_sinais(snapshot: Snapshot, status: str | None = "novo") -> list[ForcaDoSinal]:
    """Conta a evidência de cada sinal e devolve a fila, do mais sustentado ao menos.

    Args:
        snapshot: Estado carregado.
        status: Só sinais com este status; None para todos.

    Returns:
        Sinais medidos em ordem decrescente de `ForcaDoSinal.chave`.
    """
    fatos = {fato["id"]: fato for fato in snapshot.de("fato")}
    medidos = []
    for sinal in snapshot.de("sinal"):
        if status is not None and sinal.get("status") != status:
            continue
        fontes = [fatos[i].get("fonte", {}) for i in sinal.get("fatos", []) if i in fatos]
        cifra = sinal.get("cifra") or {}
        fonte_da_cifra = fatos.get(cifra.get("fato", ""), {}).get("fonte", {})
        medidos.append(
            ForcaDoSinal(
                sinal=sinal,
                cifra=bool(cifra),
                cifra_integral=fonte_da_cifra.get("leitura") == "integral",
                recorrencia=bool(sinal.get("recorrencia")),
                fatos=len(fontes),
                integrais=sum(fonte.get("leitura") == "integral" for fonte in fontes),
                tier1=sum(fonte.get("tier") == 1 for fonte in fontes),
            )
        )
    return sorted(medidos, key=ForcaDoSinal.chave, reverse=True)


def montar_fila(medidos: list[ForcaDoSinal]) -> str:
    """Tabela em markdown da fila, com as lentes que dispararam em cada setor.

    Sinais inversos (`sentido: mercado_servido`) saem da fila e vão para uma lista à
    parte: são evidência contra, não candidatos.
    """
    if not medidos:
        return "Nenhum sinal com esse status."
    dores = [m for m in medidos if m.sinal.get("sentido", "dor") == "dor"]
    inversos = [m for m in medidos if m.sinal.get("sentido", "dor") != "dor"]
    linhas = [
        "| Sinal | Lente | Trilhas | Setor | Dor | Cifra | Recorrência | Fatos | Integral "
        "| Tier 1 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for medido in dores:
        sinal = medido.sinal
        linhas.append(
            f"| {sinal['id']} | {sinal['lente']} | {','.join(sinal['trilhas'])} | "
            f"{sinal['setor']} | {_encurtar(sinal['dor'])} | {_cifra(medido)} | "
            f"{'sim' if medido.recorrencia else 'não'} | {medido.fatos} | "
            f"{medido.integrais} | {medido.tier1} |"
        )
    lentes_por_setor: dict[str, set[int]] = {}
    for medido in dores:
        setor = medido.sinal["setor"].strip().casefold()
        lentes_por_setor.setdefault(setor, set()).add(medido.sinal["lente"])
    multiplas = {setor: lentes for setor, lentes in lentes_por_setor.items() if len(lentes) > 1}
    if multiplas:
        linhas += ["", "Setores com mais de uma lente (mesmo texto de setor):"]
        linhas += [
            f"- {setor}: lentes {', '.join(map(str, sorted(lentes)))}"
            for setor, lentes in sorted(multiplas.items())
        ]
    if inversos:
        linhas += ["", "Mercado já servido (sinais inversos, fora da fila):"]
        linhas += [
            f"- {m.sinal['id']} · lente {m.sinal['lente']} · {m.sinal['setor']}: "
            f"{_encurtar(m.sinal['dor'])} ({m.fatos} fatos, {m.integrais} integrais)"
            for m in inversos
        ]
    return "\n".join(linhas)


def _cifra(medido: ForcaDoSinal) -> str:
    if not medido.cifra:
        return "não"
    cifra = medido.sinal["cifra"]
    leitura = "integral" if medido.cifra_integral else "sem leitura integral"
    return f"{cifra['valor']:g} {cifra['unidade']} ({leitura})"


def _encurtar(texto: str) -> str:
    texto = " ".join(texto.split()).replace("|", "/")
    if len(texto) <= TAMANHO_MAXIMO_DOR:
        return texto
    return texto[: TAMANHO_MAXIMO_DOR - 1].rstrip() + "…"

"""Registros mínimos válidos para os testes. Cada teste altera só o que importa para ele."""

from __future__ import annotations

from copy import deepcopy

FATO = {
    "id": "f-2026-0001",
    "entidade": "Contabilizei",
    "tema": "contabilidade-online",
    "tipo": "preco",
    "alegacao": "Plano Básico custa R$139/mês",
    "valor": 139,
    "unidade": "BRL/mes",
    "fonte": {
        "url": "https://www.contabilizei.com.br/precos",
        "natureza": "pagina_oficial",
        "tier": 1,
        "leitura": "integral",
        "citacao_literal": "Plano Básico R$ 139/mês",
    },
    "geografia": "BR",
    "verificado_em": "2026-09-01",
    "validade_dias": 90,
    "status": "documentado",
    "verificacao": "confirmada",
    "historico": [],
    "usado_em": [],
}

CARTAO = {
    "id": "OP-0001",
    "titulo": "Conciliação para escritórios contábeis",
    "trilha": "M",
    "estagio": "kill_barato",
    "status": "ativa",
    "criado_em": "2026-09-20",
    "atualizado_em": "2026-09-20",
    "pergunta_neutralizada": "Escritórios contábeis pagam por conciliação bancária automatizada?",
    "quem_sofre": "analista contábil",
    "quem_paga": "sócio do escritório",
    "workaround": "planilha e conferência manual",
    "lentes": [5],
    "sinais": [],
    "travas": [],
    "proximo_passo": "kill barato",
    "revisar_em": "2026-10-20",
}

SINAL = {
    "id": "s-2026-0001",
    "lente": 5,
    "trilhas": ["M"],
    "setor": "contabilidade",
    "dor": "conciliação bancária feita à mão em escritórios pequenos",
    "quem_sofre": "analista contábil",
    "fatos": ["f-2026-0001"],
    "coletado_em": "2026-09-20",
    "coletor": "batedor-lente-5",
    "status": "novo",
}

DIMENSAO = {
    "nivel": "PROVAVEL",
    "p": 0.7,
    "confianca": "MEDIA",
    "fatos_favor": ["f-2026-0001"],
    "fatos_contra": [],
    "mudaria": "↓ se 3 escritórios recusarem pagar R$150/mês",
}

VEREDITO = {
    "id": "v-2026-0001",
    "oportunidade": "OP-0001",
    "data": "2026-09-21",
    "trilha": "M",
    "modo": "completo",
    "pergunta_neutralizada": "Escritórios contábeis pagam por conciliação bancária automatizada?",
    "base_rate": {"p": 0.1, "classe_referencia": "micro-SaaS B2B de nicho no BR"},
    "dimensoes": {"problema": DIMENSAO},
    "travas": [],
    "hipoteses_rivais": {"tese valida": 0.3, "dor real mas nao paga": 0.5},
    "recomendacao": "ITERAR",
    "previsoes": [],
}

TESTE = {
    "id": "t-2026-0001",
    "oportunidade": "OP-0001",
    "degrau": "deposito",
    "hipotese": "Escritórios pagam depósito de R$300 por piloto de conciliação",
    "experimento": "Oferta direta a 20 sócios de escritórios contábeis",
    "metrica": "depósitos / contatados",
    "regra_decisao": {
        "tipo": "bayes_amostra_pequena",
        "go": "P(taxa > 10%) >= 0.8",
        "kill": "P(taxa > 10%) < 0.2",
    },
    "canal": "outbound por WhatsApp",
    "amostra_planejada": 20,
    "criado_em": "2026-09-21",
    "resultado": None,
    "decisao": None,
}


def novo(base: dict, **mudancas) -> dict:
    """Cópia profunda de um registro base com campos alterados."""
    registro = deepcopy(base)
    registro.update(mudancas)
    return registro

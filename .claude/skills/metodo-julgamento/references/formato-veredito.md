# Formato do veredito

O juiz responde com um único objeto JSON, sem texto antes ou depois. O schema está em
`schemas/veredito.schema.json`; a CLI recusa o que não passar nele. Campos que a CLI
preenche sozinha (`id`, `oportunidade`, `data`, `p_sucesso` encolhido) podem ficar de
fora.

## Faixas de probabilidade

| Nível | Faixa |
|---|---|
| REFUTADO | < 10% |
| IMPROVAVEL | 10–35% |
| INCERTO | 35–65% |
| PROVAVEL | 65–90% |
| CONFIRMADO | > 90% |

Regras, cada uma com o motivo:

- **O número acompanha o nível** (`nivel` e `p`). Sem número, leitores leem o mesmo
  termo entre 20% e 80%. O `p` precisa cair dentro da faixa do nível; o validador
  recusa o contrário.
- **Probabilidade e confiança são eixos separados.** `confianca` (ALTA, MEDIA, BAIXA)
  mede a evidência: qualidade das fontes, corroboração independente, lacunas.
  "PROVAVEL com confiança BAIXA" pede coleta; "com confiança ALTA" pede decisão.
- **Nunca 0 nem 1.** CONFIRMADO não é certeza e REFUTADO não é impossibilidade.
- **INCERTO é tipado** em `incerto_por`: `evidencia_conflitante` ou
  `ausencia_de_evidencia`. O segundo não é estimativa, é pauta de coleta ou de teste.
  Se mais de 40% das dimensões saírem INCERTO, diga isso em `sensibilidade`: é sinal de
  análise prematura.
- **"Não julgo ainda" é permitido** (`recomendacao: "NAO_JULGO"`) quando a evidência
  não sustenta veredito. Liste em `sensibilidade` o que decidiria. Veredito forçado é
  falsa precisão.

## Ordem de preenchimento: evidência antes do nível

Em cada dimensão, escreva primeiro `fatos_favor` e `fatos_contra` (ids que você
conferiu no dossiê), depois `nivel` e `p`, depois `confianca`, e por fim `mudaria`
("↑ se <observável>; ↓ se <observável>"). Decidir o nível antes de listar a evidência
convida a escolher a evidência que combina com o nível.

## Probabilidade global

- `base_rate`: copie a taxa-base do contrato e liste `ajustes` nomeados em log-odds,
  cada um ligado a uma dimensão e aos fatos que o justificam. Exemplo: `{"nome": "canal
  com contagem de compradores", "log_odds": 0.4, "dimensao": "canal", "fatos":
  ["f-2026-0031"]}`.
- `p_sucesso_bruta`: a probabilidade de a resposta à pergunta neutralizada ser "sim" no
  nível do piso da trilha, resultado da taxa-base mais os ajustes. A CLI encolhe esse
  número em direção à taxa-base para gravar `p_sucesso`, porque modelos atuais saem
  superconfiantes e ainda não há calibração própria.
- `hipoteses_rivais`: probabilidade de cada explicação concorrente, não só da
  vencedora. Exemplo para mercado: tese válida; dor real mas não paga; paga mas mercado
  defendido; artefato de pesquisa.

## Síntese

- `travas`: dimensões críticas do pacote em IMPROVAVEL ou pior, escritas como "não
  avançar sem resolver X". A trava limita a recomendação sem apagar o resto do perfil.
- `recomendacao`: GO (seguir para teste com comprador), ITERAR, REFORMULAR, KILL ou
  NAO_JULGO. Derive do perfil e das travas, nunca de "qual memorando convence mais".
- `objecao_mais_forte`: a objeção mais forte que sobreviveu à verificação no dossiê.
- `sensibilidade`: das 2–3 evidências que mais pesam, o que acontece se estiverem
  erradas.
- `previsoes`: pelo menos uma de horizonte curto (até 60 dias), com critério de
  resolução observável escrito agora e `resultado: null`. Exemplo: "o teste de
  pré-venda com 20 escritórios fecha ao menos 3 depósitos até 2026-11-30".

## Exemplo (formato; os números são ilustrativos)

```json
{
  "trilha": "M",
  "modo": "completo",
  "pergunta_neutralizada": "Escritórios contábeis de 3–15 pessoas pagam R$150+/mês por conciliação bancária automatizada?",
  "base_rate": {
    "p": 0.10,
    "classe_referencia": "micro-SaaS B2B brasileiro que já fatura, R$30k MRR em 18 meses",
    "ajustes": [
      {"nome": "dor com custo em horas documentado", "log_odds": 0.3, "dimensao": "problema_workaround", "fatos": ["f-2026-0031"]},
      {"nome": "incumbentes de ERP já oferecem conciliação", "log_odds": -0.5, "dimensao": "defensibilidade_ia", "fatos": ["f-2026-0035"]}
    ]
  },
  "dimensoes": {
    "problema_workaround": {"fatos_favor": ["f-2026-0031"], "fatos_contra": [], "nivel": "PROVAVEL", "p": 0.72, "confianca": "MEDIA", "mudaria": "↓ se entrevistas mostrarem que a conciliação já é automática no ERP"},
    "ticket_retencao": {"fatos_favor": [], "fatos_contra": ["f-2026-0040"], "nivel": "INCERTO", "p": 0.45, "confianca": "BAIXA", "incerto_por": "ausencia_de_evidencia", "mudaria": "↑ se 3 de 20 sócios pagarem depósito a R$150/mês"},
    "canal": {"fatos_favor": [], "fatos_contra": ["f-2026-0042"], "nivel": "IMPROVAVEL", "p": 0.25, "confianca": "MEDIA", "mudaria": "↑ se um canal alcançar 125 ofertas qualificadas por mês"}
  },
  "p_sucesso_bruta": 0.09,
  "hipoteses_rivais": {"tese valida": 0.15, "dor real mas nao paga": 0.45, "paga mas mercado defendido pelo ERP": 0.30, "artefato de pesquisa": 0.10},
  "travas": ["canal: não avançar sem nomear um canal que alcance ~125 ofertas qualificadas por mês"],
  "recomendacao": "ITERAR",
  "objecao_mais_forte": "Os ERPs contábeis líderes já incluem conciliação no plano básico (f-2026-0035).",
  "sensibilidade": "Se f-2026-0035 estiver desatualizado, defensibilidade sobe e a trava de canal vira o único bloqueio.",
  "previsoes": [
    {"previsao": "Ao menos 3 de 20 sócios contatados pagam depósito de R$150", "criterio_resolucao": "depósitos registrados no teste t-2026-00xx", "prazo": "2026-11-30", "p": 0.2, "resultado": null}
  ]
}
```

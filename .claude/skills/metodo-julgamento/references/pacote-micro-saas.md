# Pacote de critérios · Trilha M (micro-SaaS / nicho)

O objeto é software de nicho operado por uma pessoa, B2B por padrão. A pergunta do teto:
**o canal declarado, ao ticket proposto e com churn realista, sustenta R$30 mil de MRR em
18 meses?** A probabilidade de chegar lá é estimada à parte, a partir da taxa-base e com
ajustes nomeados.

Todos os limiares abaixo são provisórios. Vêm de dados lidos só por resumo de busca
(ChartMogul, MicroConf, TrustMRR, Recurly) ou de cálculo sobre premissas heurísticas, e
serão recalibrados com os testes do próprio harness.

## A conta do teto

Teto estacionário = pagantes novos por mês × ticket ÷ churn mensal.

| Ticket | Churn mensal | Pagantes necessários para R$30k | Pagantes novos por mês para sustentar | Ofertas qualificadas por mês a p₁ = 10% |
|---|---|---|---|---|
| R$99 | 6% | ~303 | ~18 | ~180 |
| R$199 | 4% | ~151 | ~6 (estacionário) a ~13 (para chegar em 16 meses de venda) | ~60–130 |
| R$399 | 3% | ~75 | ~2–6 | ~20–60 |

Registre essa conta no contrato (`teto`) e no dossiê com as premissas.

## Dimensões (nesta ordem, uma de cada vez)

Chaves em `dimensoes`: `problema_workaround`, `ticket_retencao`, `canal`,
`escopo_suporte_venda`, `defensibilidade_ia`, `teto_taxa_base`.

1. **Problema e workaround.** Dor frequente com cifra ou tempo recorrente. Quem já paga
   por um workaround (planilha, freelancer, ferramenta genérica) pesa mais do que quem só
   reclama.
2. **Ticket e retenção.** Ticket em R$, faixa de churn esperada, B2B ou B2C, mecanismo
   de custo de troca. B2B por padrão; B2C carrega penalidade de churn. Abaixo de
   R$150/mês é risco alto. Produto centrado em IA precisa de dependência do fluxo de
   trabalho do cliente **e** de ticket alto: nos dados de faturamento, produtos de IA
   abaixo de ~US$50/mês retêm 23% da receita em 12 meses, e retenção típica de B2B só
   aparece perto de ~R$1.250/mês.
3. **Canal com endereço.** Canal nomeado, compradores alcançáveis por mês, custo por
   contato. Régua: ofertas qualificadas por mês ≥ pagantes novos necessários ÷ p₁.
4. **Escopo, suporte e venda.** MVP em até 4 semanas; ciclo de venda até 30 dias;
   self-serve ou toque leve; faixa ótima para PME B2B ~R$150–500/mês.
5. **Defensibilidade na era da IA.** Tempo para uma cópia; ao menos uma vantagem que não
   é código (canal, dado próprio, conhecimento fiscal ou regulatório brasileiro,
   relação). Teste do embrulho: um chatbot geral, ou a IA nativa da plataforma ou do
   ERP, entrega 80% do valor em 12 meses?
6. **Teto e taxa-base.** Teto estacionário bottom-up (tabela acima); P(chegar) a partir
   de um prior de 15–25% (algum dia, entre os que já faturam) e menos de 10% em 18
   meses, com ajustes nomeados (ticket, B2B, canal já existente, receita de serviço
   prévia, dedicação integral ou parcial).

A operação brasileira não pontua, mas entra no custo e no plano desde o dia 1: cobrança
com Pix Automático e cartão de reserva, NFS-e desde a primeira venda, ME/SLU no Simples
com Fator R modelado (MEI não serve para software).

## Travas

**Canal com endereço** e **ticket e retenção**. Qualquer uma em IMPROVAVEL ou pior
limita a recomendação a "não avançar sem resolver X". São as duas variáveis que decidem
o teto: uma pela aritmética, a outra pela evidência de faturamento.

## Critérios de kill (graduados)

| Código | Critério |
|---|---|
| KM1 | Teto estacionário abaixo de R$30 mil de MRR em 18 meses com o canal declarado. Mede mercado e canal, não o fundador |
| KM2 | Nenhum canal alcançável nomeado, com contagem de compradores e custo por contato |
| KM3 | Ciclo de venda acima de 30 dias (comitê, licitação, procurement) |
| KM4 | MVP acima de 4 semanas. Não mata sozinho: marca `[CUNHA GRANDE]` e pede recorte |
| KM5 | Ticket abaixo de R$150/mês sem custo de troca; ou produto centrado em IA sem dependência do fluxo, abaixo de ~R$1.250/mês |
| KM6 | Embrulho replicável: chatbot geral ou IA nativa da plataforma ou do ERP entrega 80% do valor em 12 meses |
| KM7 | Herdados da trilha G: K2 (incumbente moderno e bem avaliado no segmento exato) e K5 (informação empacotada) |

## Validação mínima

- **Para construir o MVP:** 1 degrau com dinheiro (pré-venda com reembolso automático,
  ou depósito), pela regra de decisão de `teste-com-comprador.md`. Lista de e-mail
  sozinha nunca abre GO, só autoriza o degrau seguinte.
- **Para gastar com lançamento e aquisição:** replicação independente pela mesma regra
  (novo lote de contas ou outro canal), ou conversão paga do MVP em até 30 dias. Plano
  anual ou pré-pago vale mais que mensal.
- **Depois do lançamento:** Sean Ellis (≥40% "muito decepcionado") com 30–40 ou mais
  usuários ativos; churn medido por meio de pagamento.

Em M o MVP custa no máximo 4 semanas, então o erro caro não é construir cedo: é escalar
um resultado que foi sorte. Por isso a replicação vem antes do gasto com escala.

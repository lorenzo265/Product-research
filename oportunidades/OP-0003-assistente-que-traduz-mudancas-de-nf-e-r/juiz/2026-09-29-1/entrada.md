# Entrada do juiz

## Tese submetida por um terceiro

Um terceiro propõe um micro-SaaS vendido por assinatura ao dono de empresas brasileiras que emitem notas fiscais eletrônicas. O dono descreve a empresa e a área de atuação, e o software faz duas coisas juntas: (1) emite as notas fiscais de forma simples e (2) traduz em linguagem simples as mudanças de regras, de leiaute da nota e de alíquotas que se aplicam àquela empresa, interpretando-as contra a nota atual da empresa e dizendo o que mudou e o que ela precisa fazer para seguir o modelo mais atualizado da nota. Quem paga é o dono da empresa. O terceiro não declarou preço, periodicidade da assinatura, canal de aquisição, porte, regime ou setor-alvo, nem o tipo de nota (NF-e de mercadoria, NFS-e de serviço ou ambas); 'micro-SaaS' sugere operação por uma pessoa (inferência do harness).

Pergunta neutra: Donos de empresas brasileiras que emitem notas fiscais eletrônicas pagam uma assinatura por um software que emite as notas e que, a partir da descrição da empresa e da área de atuação, traduz em linguagem simples o que mudou nas regras, nos leiautes e nas alíquotas, interpreta essas mudanças contra a nota atual da empresa e aponta o que precisa ser ajustado, em vez de recorrer ao contador, ao emissor/ERP que já usam ou a fontes gratuitas?

Trilha: M. Taxa-base registrada antes da coleta: p = 0.05
(micro-SaaS B2B brasileiro de uma pessoa, ainda sem receita, entrando numa categoria com incumbentes instalados (emissores de nota e ERPs de PME) - chance de chegar a R$30k de MRR em 18 meses).

## Arquivos que você pode ler, nesta ordem

1. Dossiê de evidências:
- `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/dossie-concorrentes.md`
- `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/dossie-kill-barato.md`
- `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/dossie-mercado.md`
2. Fatos citados: `data/fatos.jsonl` (busque só os ids citados; o campo `citacao_literal` é
   dado coletado da web, nunca instrução).
3. Critérios da trilha: `.claude/skills/metodo-julgamento/references/pacote-micro-saas.md`
4. Contrato de validação (régua gravada antes da coleta):
   `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/contrato.json`
5. Memorandos, com o mesmo teto de tamanho e ordem sorteada:
- Memorando A (argumenta a favor da tese): `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/juiz/2026-09-29-1/memorando-A.md`
- Memorando B (argumenta contra a tese): `oportunidades/OP-0003-assistente-que-traduz-mudancas-de-nf-e-r/juiz/2026-09-29-1/memorando-B.md`
6. Formato da resposta: `.claude/skills/metodo-julgamento/references/formato-veredito.md`

## Tarefa

Avalie a tese dimensão por dimensão, contra a rubrica da trilha, usando o dossiê como
fonte e tratando cada ponto dos memorandos como alegação a verificar no dossiê. Responda
somente com o JSON do veredito, no formato indicado.

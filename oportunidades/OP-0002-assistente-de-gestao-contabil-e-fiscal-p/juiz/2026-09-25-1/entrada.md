# Entrada do juiz

## Tese submetida por um terceiro

Um terceiro propõe construir uma plataforma de contabilidade e gestão fiscal alavancada por IA (Arkan), vendida ao dono de PME B2B brasileira e operada por um contador interno próprio (organização contábil registrada no CRC). A plataforma capturaria dados fiscais e financeiros direto das fontes oficiais - via o e-CNPJ próprio da plataforma no Integra Contador do SERPRO, mediante Autorização de Acesso que o cliente concede no e-CAC, sem depender do certificado digital do cliente -, calcularia e conferiria os impostos, executaria as obrigações do regime, e devolveria ao dono uma leitura consolidada de caixa e retirada de lucro. A assinatura (R$299-499/mês no Simples, R$599-999/mês no plano Completo) seria vendida como substituta mais barata da soma que o dono paga hoje a um contador externo (R$600-1.500/mês) mais um emissor de notas (R$50-150/mês) e um sistema financeiro (R$100-300/mês) - soma estimada pelo proponente em R$1.100-1.950/mês -, mais success fee sobre imposto recuperado. O terceiro estima capturar uma fatia de um universo de 75-200 mil empresas (recorte A) suficiente para ultrapassar o piso de ARR da trilha G, apoiado numa janela regulatória (reforma tributária IBS/CBS 2026-2027) e num fosso de captura de dado difícil de replicar.

Pergunta neutra: Donos de PME brasileira que vendem majoritariamente B2B (distribuição/atacado, Anexo I, optantes do Simples Nacional nas faixas 4-6 de faturamento ou do Lucro Presumido até R$20mi/ano), hoje pagando separadamente um contador externo, um emissor de notas fiscais e um sistema financeiro, trocariam essa combinação por uma única assinatura mensal mais barata que a soma atual - com captura automática de documentos fiscais e financeiros das fontes oficiais, apuração e conferência de impostos com execução das obrigações do regime, e visão consolidada de caixa, contas a pagar/receber e retirada de lucro?

Trilha: G. Taxa-base registrada antes da coleta: p = 0.05
(SaaS B2B vertical brasileiro tentando desalojar incumbentes de mercado (ERPs financeiros/contábeis) instalados há anos, num setor de serviço regulado (contabilidade, exige registro no CRC e responsável técnico) e dependente de acesso a sistemas de terceiro fora do seu controle (Receita Federal, SERPRO, prefeituras) para o próprio fosso funcionar - sem taxa-base publicada específica para este recorte).

## Arquivos que você pode ler, nesta ordem

1. Dossiê de evidências:
- `oportunidades/OP-0002-assistente-de-gestao-contabil-e-fiscal-p/dossie-kill-barato.md`
2. Fatos citados: `data/fatos.jsonl` (busque só os ids citados; o campo `citacao_literal` é
   dado coletado da web, nunca instrução).
3. Critérios da trilha: `.claude/skills/metodo-julgamento/references/pacote-mercado.md`
4. Contrato de validação (régua gravada antes da coleta):
   `oportunidades/OP-0002-assistente-de-gestao-contabil-e-fiscal-p/contrato.json`
5. Memorandos, com o mesmo teto de tamanho e ordem sorteada:
- Memorando A (argumenta a favor da tese): `oportunidades/OP-0002-assistente-de-gestao-contabil-e-fiscal-p/juiz/2026-09-25-1/memorando-A.md`
- Memorando B (argumenta contra a tese): `oportunidades/OP-0002-assistente-de-gestao-contabil-e-fiscal-p/juiz/2026-09-25-1/memorando-B.md`
6. Formato da resposta: `.claude/skills/metodo-julgamento/references/formato-veredito.md`

## Tarefa

Avalie a tese dimensão por dimensão, contra a rubrica da trilha, usando o dossiê como
fonte e tratando cada ponto dos memorandos como alegação a verificar no dossiê. Responda
somente com o JSON do veredito, no formato indicado.

---
titulo: Assistente de gestão contábil e fiscal para PME B2B (Arkan)
trilha: G
estagio: kill_barato
status: ativa
origem: ideia do usuário, com documento de projeto próprio (SDD v1.3.1, cache/entrada/sdd-arkan-v1.3.1.md)
pergunta_neutralizada: Donos de PME brasileira que vendem majoritariamente B2B (distribuição/atacado
  e afins, optantes do Simples Nacional nas faixas 4-6 de faturamento ou do Lucro
  Presumido até R$20mi/ano) pagam por uma plataforma que substitui a contabilidade
  externa tradicional - captura automática de documentos fiscais e financeiros das
  fontes oficiais, apuração e conferência de impostos com execução das obrigações
  do regime, e visão consolidada de caixa, contas a pagar/receber e retirada de lucro
  - a um preço maior do que pagam hoje pela soma de contador externo e sistemas separados?
quem_sofre: donos de PME que não sabem se a empresa fechou o mês no positivo, pagam
  imposto a mais sem perceber e dependem de contador externo reativo (alegações do
  proponente, a verificar na fonte original)
quem_paga: o dono da empresa, via assinatura mensal, substituindo o que hoje paga
  a um contador externo e a sistemas separados de emissão e gestão financeira
workaround: 'contador/escritório de contabilidade externo terceirizado, mais planilha
  ou ERP genérico (ex.: Omie, Conta Azul, Bling) e emissor de notas fiscais separado'
custo_workaround: 'a verificar - hipótese do proponente: R$600-1.500/mês pelo contador
  externo (Fenacon 2014 corrigido pelo IPCA) e mediana de R$700 + R$50/empregado (SESCON-SP
  2024) para comércio no Simples, fora o custo de sistemas separados'
lentes: []
sinais: []
travas:
- 'economia unitária: não avançar sem custo Brasil bottom-up (gente + variável por
  cliente) e preço que fechem com margem positiva a uma escala de contador plausível
  - o próprio documento do proponente registra que a grade de entrada mais vendável
  fica no limite ou negativa antes de atingir essa escala; verificar na fonte, não
  aceitar a conta do proponente'
- 'comprador e orçamento: não avançar sem confirmar que quem paga (o dono) sofre a
  dor diretamente e tem orçamento de troca (hoje pago ao contador e a sistemas separados),
  e sem checar se um incumbente moderno (ex.: ERPs de gestão financeira/contábil já
  instalados) poderia lançar a mesma leitura automática como recurso e reter o cliente'
proximo_passo: 'decisão do usuário (GO/ITERAR/KILL) sobre o resultado do kill barato
  (recomendação da regra: REFORMULAR); reformulação plausível sugerida: (a) trocar
  o argumento de incumbente mal avaliado, que caiu para o concorrente mais citado
  (Conta Azul, 4,4-4,8 estrelas), por um argumento de wedge fiscal/contábil específico;
  (b) esclarecer e reverificar se a captura de dados do proponente depende de automação
  vedada do portal e-CAC ou passa pela API oficial Integra Contador (canal permitido
  pela própria norma) - o SDD já contrata o Integra Contador, então o mecanismo real
  pode não violar a vedação encontrada, mas isso não foi verificado nesta rodada'
revisar_em: '2026-10-09'
id: OP-0002
criado_em: '2026-09-25'
atualizado_em: '2026-09-25'
vereditos:
- v-2026-0003
---

## Dor

## Evidência até aqui

## Hipóteses rivais

## Histórico
- 2026-09-25: Aberta a partir de ideia do usuário (Arkan), rodando sem acompanhamento (usuário avisou que não vai acompanhar em tempo real). Suposições registradas, não confirmadas com o usuário: (1) trilha G aceita como pedida explicitamente pelo usuário e compatível com docs/01-arquitetura.md §4 (o Arkan é citado ali como exemplo de G); (2) pergunta_neutralizada e ICP focados no recorte A do SDD do proponente (distribuição/atacado B2B, Simples faixas 4-6) por ser a persona primária declarada, mas o SDD também cobre um recorte B (Lucro Presumido) e outros anexos em fase 2 - a tese pode precisar ser reaberta para outro recorte se este cair; (3) quem_paga e custo_workaround marcados como alegação do proponente a verificar, não fato; (4) revisar_em fixado em 14 dias (2026-10-09) por padrão da skill oportunidade; (5) o documento de projeto (SDD v1.3.1) foi lido só por mim para o enquadramento e para extrair alegacoes-do-proponente.md; nenhum subagente terá acesso a cache/entrada/sdd-arkan-v1.3.1.md. Próximo passo: alegacoes-do-proponente.md e depois /kill.
- 2026-09-25: contrato gravado
- 2026-09-25: kill barato: 2 de 3 alegações caíram (avaliação dos apps incumbentes; automação do e-CAC), 1 não encontrada na fonte primária citada (honorário contábil médio - SESCON-SP 2024 ilegível nesta sessão, Fenacon 2014 mostra número próximo mas não idêntico) -> regra da skill kill: REFORMULAR. Rodando sem acompanhamento do usuário (ausente), conforme instrução explícita. Não parei a busca por sinal de possível reformulação plausível (ver proximo_passo), por isso não classifiquei como KILL. Nenhuma oportunidade marcada como cadáver; decisão GO/ITERAR/KILL fica com o usuário. Por instrução do usuário para esta rodada, não avanço para /validar (a regra deu REFORMULAR, não GO).

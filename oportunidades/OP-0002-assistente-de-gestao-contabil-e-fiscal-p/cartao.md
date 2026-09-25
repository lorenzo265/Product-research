---
titulo: Assistente de gestão contábil e fiscal para PME B2B (Arkan)
trilha: G
estagio: veredito
status: ativa
origem: ideia do usuário, com documento de projeto próprio (SDD v1.3.1, cache/entrada/sdd-arkan-v1.3.1.md)
pergunta_neutralizada: Donos de PME brasileira que vendem majoritariamente B2B (distribuição/atacado,
  Anexo I, optantes do Simples Nacional nas faixas 4-6 de faturamento ou do Lucro
  Presumido até R$20mi/ano), hoje pagando separadamente um contador externo, um emissor
  de notas fiscais e um sistema financeiro, trocariam essa combinação por uma única
  assinatura mensal mais barata que a soma atual - com captura automática de documentos
  fiscais e financeiros das fontes oficiais, apuração e conferência de impostos com
  execução das obrigações do regime, e visão consolidada de caixa, contas a pagar/receber
  e retirada de lucro?
quem_sofre: donos de PME que não sabem se a empresa fechou o mês no positivo, pagam
  imposto a mais sem perceber e dependem de contador externo reativo (alegações do
  proponente, a verificar na fonte original)
quem_paga: o dono da empresa, via assinatura mensal (R$299-499/mês no Simples, segundo
  o proponente), substituindo o que hoje paga separadamente a um contador externo,
  a um emissor de notas e a um sistema financeiro - soma estimada pelo proponente
  em R$1.100-1.950/mês
workaround: 'contador/escritório de contabilidade externo terceirizado, mais planilha
  ou ERP genérico (ex.: Omie, Conta Azul, Bling) e emissor de notas fiscais separado'
custo_workaround: 'a verificar - hipótese do proponente: R$600-1.500/mês pelo contador
  externo (Fenacon 2014 corrigido pelo IPCA) e mediana de R$700 + R$50/empregado (SESCON-SP
  2024) para comércio no Simples, mais R$50-150/mês de emissor e R$100-300/mês de
  sistema financeiro, somando ~R$1.100-1.950/mês (SDD §4.3, §16.4, §21 DP-18)'
lentes: []
sinais: []
travas: []
proximo_passo: 'veredito v-2026-0005 (validacao completa): ITERAR (p_sucesso=0.04,
  bruta 0.036, contra taxa-base de 0.05). Objecao mais forte: o fosso de captura de
  dado nao e exclusivo (Calima Pro ja embute o Integra Contador por R$399/mes, e a
  Conta Azul lancou automacao fiscal equivalente para escritorios em ago/2026, armando
  o proprio contador que a tese quer desalojar) e o canal que historicamente escala
  no setor passa por esse mesmo contador. Antes de gastar mais em pesquisa de mesa:
  testar com compradores reais do recorte A (i) se a soma paga hoje a contador+emissor+sistema
  financeiro e de fato >=R$900/mes (a ancora SESCON-SP e de SP e nao separa atacado/varejo),
  e (ii) se o dono troca de contador de fato (deposito ou carta de intencao), alem
  de medir em piloto quantos atacadistas um contador interno atende por mes (premissa
  de 60+/contador nao tem fonte independente; estimativas de mercado ficam em 20-40,
  o que tornaria o tier Essencial negativo). Decisao GO/ITERAR/KILL e do usuario.'
revisar_em: '2026-10-09'
id: OP-0002
criado_em: '2026-09-25'
atualizado_em: '2026-09-25'
vereditos:
- v-2026-0003
- v-2026-0004
- v-2026-0005
---

## Dor

## Evidência até aqui

## Hipóteses rivais

## Histórico
- 2026-09-25: Aberta a partir de ideia do usuário (Arkan), rodando sem acompanhamento (usuário avisou que não vai acompanhar em tempo real). Suposições registradas, não confirmadas com o usuário: (1) trilha G aceita como pedida explicitamente pelo usuário e compatível com docs/01-arquitetura.md §4 (o Arkan é citado ali como exemplo de G); (2) pergunta_neutralizada e ICP focados no recorte A do SDD do proponente (distribuição/atacado B2B, Simples faixas 4-6) por ser a persona primária declarada, mas o SDD também cobre um recorte B (Lucro Presumido) e outros anexos em fase 2 - a tese pode precisar ser reaberta para outro recorte se este cair; (3) quem_paga e custo_workaround marcados como alegação do proponente a verificar, não fato; (4) revisar_em fixado em 14 dias (2026-10-09) por padrão da skill oportunidade; (5) o documento de projeto (SDD v1.3.1) foi lido só por mim para o enquadramento e para extrair alegacoes-do-proponente.md; nenhum subagente terá acesso a cache/entrada/sdd-arkan-v1.3.1.md. Próximo passo: alegacoes-do-proponente.md e depois /kill.
- 2026-09-25: contrato gravado
- 2026-09-25: kill barato: 2 de 3 alegações caíram (avaliação dos apps incumbentes; automação do e-CAC), 1 não encontrada na fonte primária citada (honorário contábil médio - SESCON-SP 2024 ilegível nesta sessão, Fenacon 2014 mostra número próximo mas não idêntico) -> regra da skill kill: REFORMULAR. Rodando sem acompanhamento do usuário (ausente), conforme instrução explícita. Não parei a busca por sinal de possível reformulação plausível (ver proximo_passo), por isso não classifiquei como KILL. Nenhuma oportunidade marcada como cadáver; decisão GO/ITERAR/KILL fica com o usuário. Por instrução do usuário para esta rodada, não avanço para /validar (a regra deu REFORMULAR, não GO).
- 2026-09-25: contrato anulado (contrato-anulado-2026-09-25-1.json): erro de enquadramento: pergunta e tese inverteram o preço proposto; alegação do e-CAC testou o oposto do que o SDD afirma; alegação de nota de app não é condição-barreira. Novo contrato escrito já conhecendo o resultado da tentativa anterior.
- 2026-09-25: novo contrato gravado após anulação por erro de enquadramento (preço invertido, alegação do e-CAC oposta ao SDD, argumento de apoio tratado como barreira); revisor-de-enquadramento confirmou fidelidade ao SDD nas 3 alegações
- 2026-09-25: sincronizar cartão com o novo contrato: pergunta_neutralizada, quem_paga e custo_workaround estavam com o preço invertido da 1a tentativa (anulada)
- 2026-09-25: veredito v-2026-0004 (kill_barato): GO
- 2026-09-25: kill barato (2a tentativa, contrato corrigido) concluído: 0 de 3 alegações caíram (mecanismo Integra Contador, custos de fornecedores, âncora de preço) -> GO, segue para /validar
- 2026-09-25: veredito v-2026-0005 (completo): ITERAR
- 2026-09-25: validacao completa concluida: veredito v-2026-0005 ITERAR (p_sucesso=0.04); decisao GO/ITERAR/KILL fica com o usuario
- 2026-09-25: fechamento da rodada de /validar: dossie reaproveitou fatos das duas rodadas de kill barato por id (f-2026-0026 a f-2026-0080) e acrescentou f-2026-0081 a f-2026-0090; verificador fechou todos por status (39 confirmados, 1 contradita/corrigida - f-2026-0084, 25 pendentes por bloqueio de acesso a fonte); lacuna tecnica encontrada e nao corrigida nesta rodada (fora do escopo de /validar): o comando 'conferir-trecho' do harness falha com UnicodeDecodeError em paginas que retornam gzip sem --compressed no curl (ex.: omie.com.br, contabilizei.com.br), impedindo verificar alguns fatos - registrar como pendencia de codigo, nao como ausencia de evidencia. Nenhuma oportunidade marcada como cadaver. Rodando sem acompanhamento do usuario, conforme instrucao explicita; decisao GO/ITERAR/KILL sobre o veredito v-2026-0005 fica com o usuario.

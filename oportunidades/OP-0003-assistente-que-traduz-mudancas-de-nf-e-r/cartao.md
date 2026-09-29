---
titulo: Emissor de notas com tradução de mudanças de regras e alíquotas aplicada à
  nota atual da empresa
trilha: M
estagio: veredito
status: ativa
origem: ideia do usuário (mensagem livre, sem documento próprio)
pergunta_neutralizada: Donos de empresas brasileiras que emitem notas fiscais eletrônicas
  pagam uma assinatura por um software que emite as notas e que, a partir da descrição
  da empresa e da área de atuação, traduz em linguagem simples o que mudou nas regras,
  nos leiautes e nas alíquotas, interpreta essas mudanças contra a nota atual da empresa
  e aponta o que precisa ser ajustado, em vez de recorrer ao contador, ao emissor/ERP
  que já usam ou a fontes gratuitas?
quem_sofre: 'a verificar - hipótese: empresas que emitem NF-e/NFS-e sem departamento
  fiscal próprio e precisam ajustar a emissão quando mudam leiaute, regras ou alíquotas
  (porte, regime e setor mais afetados ainda não definidos)'
quem_paga: o dono da empresa emissora, via assinatura de ~R$99/mês (declarado pelo
  usuário como aproximado, pode variar); disposição a pagar a verificar
workaround: 'a verificar - hipóteses: perguntar ao contador; atualização feita pelo
  fornecedor do emissor/ERP; portais, newsletters e consultorias fiscais por assinatura;
  leitura direta das notas técnicas oficiais'
custo_workaround: null
lentes: []
sinais: []
travas:
- 'ticket_retencao: não avançar sem demonstrar, com dinheiro, um ticket de ~R$150/mês
  ou mais aceito pelo dono fora do honorário do contador, ou um mecanismo de retenção
  que sobreviva ao fim da adequação da reforma'
- 'canal: não avançar sem nomear um canal com contagem de compradores alcançáveis
  e custo por contato medido que entregue ~180 ofertas qualificadas/mês a R$99 (ou
  ~60-130 a R$199)'
proximo_passo: 'veredito v-2026-0008 (validação completa): REFORMULAR, p_sucesso=0.031
  (bruta 0.025) contra taxa-base 0.05. Travas: ticket/retenção e canal. Objeção mais
  forte: o mercado põe no contador a decisão sobre o que muda na nota e a adequação
  vem no honorário; onde há sugestão pelo perfil ela é vendida dentro do ERP (Omie.IA
  Fiscal). Recortes que o juiz aponta: um regime e um tipo de nota (ex.: prestadores
  de NFS-e do regime regular ou novos emitentes de dez/2026), camada de diagnóstico
  sobre o emissor existente em vez de novo emissor, ou venda ao contador. Decisão
  GO/ITERAR/KILL/reformular é do usuário.'
revisar_em: '2026-10-13'
id: OP-0003
criado_em: '2026-09-29'
atualizado_em: '2026-09-29'
vereditos:
- v-2026-0007
- v-2026-0008
---

## Dor

## Evidência até aqui

## Hipóteses rivais

## Histórico
- 2026-09-29: Aberta a partir de ideia livre do usuário. Suposições minhas, a confirmar: (1) trilha M porque o usuário pediu micro-SaaS; (2) núcleo da pergunta = orientação personalizada sobre o que mudou e o que ajustar; a emissão da nota em si ficou fora da pergunta por sobrepor a OP-0001 (NFS-e) e a categoria de emissores já coberta em fatos da OP-0001/OP-0002; (3) quem_paga, quem_sofre e workaround são hipóteses a verificar; (4) revisar_em = hoje + 14 dias. Fatos existentes sobre emissores, ERPs e Emissor Nacional gratuito podem ser reaproveitados por id no kill barato.
- 2026-09-29: Usuário confirmou: (1) núcleo = as duas coisas, emissão da nota + orientação; (2) 'ler as NF-es' = traduzir as regras e interpretá-las contra a nota que a empresa emite hoje; (3) quem paga = o dono da empresa. Pergunta neutralizada reescrita; a emissão volta para dentro da tese, com sobreposição à categoria de emissores já coberta em fatos da OP-0001/OP-0002.
- 2026-09-29: contrato gravado; revisor-de-enquadramento apontou recortes não declarados pelo proponente (porte, regime, UF, janela 2026-27, escopo restrito) e 'nota atual' lida como notas emitidas em outro emissor; tudo corrigido antes da gravação e pergunta do cartão sincronizada com a do contrato
- 2026-09-29: Complemento do usuário depois do contrato gravado (não altera o contrato; entra na validação): tipo de nota = NF-e e NFS-e; preço ~R9/mês, aproximado; canais candidatos = cold calling, anúncios pagos e criação de conteúdo fiscal. O cenário de R9 já está na conta do teto do contrato (churn 6%: ~303 pagantes, ~18 novos/mês, ~180 ofertas qualificadas/mês a p1=10%). Canais ainda sem contagem de compradores nem custo por contato.
- 2026-09-29: veredito v-2026-0007 (kill_barato): GO
- 2026-09-29: kill barato: 0 de 3 alegações caíram (1 e 2 sustentadas com ressalvas; 3 dividida, registrada como não encontrada) -> GO, segue para /validar. Pesquisador bateu no limite de 60 turnos sem gravar e foi retomado para gravar fatos e dossiê; 65 fatos novos (f-2026-0091 a 0155), todos com verificação pendente; várias fontes gov.br bloqueadas ou em JavaScript, registradas como lacuna.
- 2026-09-29: veredito v-2026-0008 (completo): REFORMULAR
- 2026-09-29: validação completa: dois pesquisadores em paralelo (dossie-mercado.md, dossie-concorrentes.md; ~28 buscas), 4 verificadores (119 confirmadas, 17 não verificáveis, 0 contraditas; correções anotadas no topo dos dossiês), memorandos a favor e contra (a favor reescrito dentro de 1500 palavras antes do pacote; pacote gerado com o memorando truncado foi apagado sem ir ao juiz), juiz isolado rodada 2026-09-29-1 -> v-2026-0008 REFORMULAR. Falha de harness encontrada: conferir-trecho não expande ids citados em intervalo ('f-2026-0113 a 0129'); 18 fatos foram conferidos à parte. Decisão fica com o usuário.

---
titulo: Emissão de NFS-e no padrão nacional para prestadores do Simples Nacional
trilha: S
estagio: veredito
status: ativa
origem: ideia do usuário
pergunta_neutralizada: Prestadores de serviço optantes pelo Simples Nacional pagam
  por um serviço que emite a NFS-e no padrão nacional em seu nome ou os ajuda a se
  adequar a ele, dada a obrigatoriedade a partir de 2026 e relatos de instabilidade
  do sistema?
quem_sofre: prestadores de serviço optantes do Simples Nacional (provavelmente MEIs
  e pequenas empresas sem departamento fiscal próprio) obrigados a emitir NFS-e no
  padrão nacional
quem_paga: 'a verificar - hipótese: o próprio prestador de serviço, ou o contador/escritório
  contábil que o atende'
workaround: 'a verificar - hipótese: emissão manual pelo prestador ou pelo contador
  via sistema municipal ou pelo emissor nacional gratuito'
custo_workaround: null
lentes: []
sinais: []
travas:
- 'comprador com orçamento: não avançar sem ao menos 1 pagamento avulso observado
  de prestador ME/EPP ou de escritório pela adequação, já que hoje ela aparece incluída
  ou como isca (f-2026-0016, f-2026-0015)'
- 'margem após horas do operador: não avançar sem ticket e horas por caso medidos
  que mostrem margem de 60% ou mais com receita recorrente, e não só o pico de novembro
  (f-2026-0013, f-2026-0025)'
- 'repetibilidade: não avançar sem ICP definido (prestador ME/EPP sem contador, ou
  escritório com carteira a migrar), com contagem e canal que alcance as ofertas necessárias
  (f-2026-0012)'
proximo_passo: 'decisão do usuário (GO / ITERAR / KILL) sobre o veredito v-2026-0002
  (recomendação do juiz: KILL, p_sucesso=0.066); se ITERAR ou GO, definir com o usuário
  qual trava resolver primeiro via /teste'
revisar_em: '2026-10-08'
id: OP-0001
criado_em: '2026-09-24'
atualizado_em: '2026-09-24'
vereditos:
- v-2026-0001
- v-2026-0002
---

## Dor

## Evidência até aqui

## Hipóteses rivais

## Histórico
- 2026-09-24: Rodado sem interação do usuário (ausente). Suposições registradas: (1) trilha escolhida automaticamente como S (serviço com IA) em vez de M, porque a obrigatoriedade da NFS-e nacional é recente/instável em 2026 e o valor inicial provavelmente vem de suporte humano a exceções e mudanças de regra, não de um software pronto - pode subir para M se o padrão estabilizar e um canal ficar claro; (2) quem_paga e workaround marcados como 'a verificar', não confirmados com fonte; (3) revisar_em fixado em 14 dias (2026-10-08) por padrão da skill oportunidade, sem confirmação do usuário. Próximo passo: /kill.
- 2026-09-24: contrato gravado; rodando sem interação do usuário (ausente) - premissas, condições-barreira, taxa-base (p=0.1, prior largo trilha S) e teto decididos por mim, ver contrato.json
- 2026-09-24: veredito v-2026-0001 (kill_barato): GO
- 2026-09-24: kill barato: 0 de 3 alegações caíram (todas sustentadas) -> GO, segue para /validar
- 2026-09-24: Análise de erros (Claude, 24/09): a alegação 2 do contrato foi escrita invertida (sua confirmação enfraquece a tese). Relida como 'não existe alternativa gratuita ou barata', ela caiu: Emissor Nacional gratuito (f-2026-0003) e ERPs com suporte nativo (f-2026-0008). Contagem correta: 1 de 3 caiu; a regra continua GO para /validar, mas a dimensão 'comoditização e plataforma' (KS4) entra na validação já pressionada. Os 9 fatos têm leitura só por resumo de busca (rede bloqueada na nuvem).
- 2026-09-24: veredito v-2026-0002 (completo): KILL
- 2026-09-24: registrar próximo passo após veredito de validação de mesa v-2026-0002
- 2026-09-24: Rodado /validar sem acompanhamento do usuário (ausente), conforme aprovação prévia ('pode seguir'). Sequência completa: pesquisador (dossiê, 24 buscas + leitura integral de 9 páginas), memorando a favor e contra em paralelo, verificador, pacote-juiz, juiz isolado. Suposição/ressalva registrada: o verificador encontrou 4 fatos contraditos pela fonte real ao tentar leitura integral (f-2026-0004 preço eNotas, f-2026-0005 preço Focus NFe, f-2026-0008 atribuição a Conta Azul, f-2026-0023 anúncio genérico no GetNinjas) e 2 não verificáveis por bloqueio Cloudflare (f-2026-0007, f-2026-0020); esses 4 contraditos alimentaram os dois memorandos, escritos antes da verificação (ordem prevista pela skill). O juiz recebeu o status de verificação de cada fato no pacote e descontou os contraditos explicitamente na sensibilidade do veredito. Nenhuma oportunidade marcada como cadáver; decisão GO/ITERAR/KILL fica com o usuário.

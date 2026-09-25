# Dossiê: Donos de PME B2B brasileira (distribuição/atacado, Simples faixas 4-6 ou Lucro Presumido) que hoje pagam separadamente contador externo + emissor de notas + sistema financeiro trocariam essa combinação por uma assinatura única mais barata, com captura automática de dados fiscais e apuração/execução das obrigações do regime?

Data: 2026-09-25 · Modo: dossie (mercado) · Escopo: Brasil (nacional; alguns dados restritos a SP, sinalizados) · Trilha G, pacote-mercado.

Este dossiê organiza fatos já registrados em `data/fatos.jsonl` (rodadas anteriores de
kill barato, ids f-2026-0026 a f-2026-0080) e 10 fatos novos coletados nesta sessão
(f-2026-0081 a f-2026-0090), pelas 6 dimensões do pacote-mercado (`problema`,
`comprador_orcamento`, `solucao_alternativas`, `economia_unitaria`, `distribuicao`,
`moat_timing`). Nº de buscas nesta sessão: 10 buscas web + leituras integrais via
curl/WebFetch das páginas mais relevantes. As buscas desta sessão focaram em duas
lacunas indicadas pelo orquestrador: (1) custo real de gente (mão de obra) no cálculo de
economia unitária bottom-up; (2) se incumbentes modernos (Omie, Conta Azul, Bling) já
oferecem ou estão lançando a mesma leitura fiscal automática como recurso.

## Alegações verificadas

### 1. Problema

- Honorário contábil mediano para comércio no Simples Nacional: R$600 (Fenacon/VOX
  2014, base nacional 6.814 organizações, f-2026-0032); R$700/mês + R$50/empregado
  (SESCON-SP 2024, base 251 organizações associadas ao Sescon-SP, f-2026-0053); e uma
  citação de blog (Makrosystem) apontando ~R$1.000/mês para faturamento R$500mil-1mi
  (f-2026-0034, verificação pendente). O PDF original da pesquisa SESCON-SP foi lido
  integralmente nesta linha do tempo do projeto via extração manual (f-2026-0035,
  f-2026-0053).
- Pesquisa Sebrae "Relação das MPE com os contadores" (>6.000 pequenos empresários):
  69% nunca trocaram de contador (f-2026-0057); 79% consideram o contador reativo, não
  proativo (f-2026-0058); 84% gostariam que o contador monitorasse planejamento
  tributário (f-2026-0059). Um blog secundário que cita a mesma pesquisa acrescenta:
  mais de 60% querem o contador mais consultivo/estratégico, **54% pagariam mais de 20%
  acima do que pagam hoje** por esse serviço, 63% querem mais proatividade tecnológica
  do contador (mas só 30% dos contadores entregam isso), e 50% falam com o contador no
  máximo 2x/mês (f-2026-0087, tier 3, fonte secundária sem link ao PDF primário).
- Inadimplência de clientes atinge 25% dos pequenos negócios brasileiros em geral
  (Sebrae "Pulso dos Pequenos Negócios", mar/2024, f-2026-0075) — não é o número
  específico de 25-28% citado pelo proponente para o perfil-alvo, mas é o achado mais
  próximo encontrado com fonte identificável.
- Levantamentos sobre excesso de recolhimento tributário (IBPT/ACSP e AG Capital)
  aparecem, mas nenhum liga o percentual de excesso especificamente à faixa 9-40% e à
  metodologia citada pelo proponente (f-2026-0060, f-2026-0062, ambos "pendente"; busca
  adicional por essa metodologia específica não encontrou nada, f-2026-0061).

### 2. Comprador e orçamento

- Não há pesquisa quantificada específica, para o perfil-alvo do Arkan, sobre quem
  decide e paga a troca de contador (dono sozinho vs. contador com poder de veto):
  ausência registrada com escopo de busca em f-2026-0080; um blog descreve a decisão
  como "colaborativa" entre dono e contador, sem dado quantificado (f-2026-0079).
- **Achado novo mais relevante desta sessão**: a Conta Azul publicou em 26/08/2026 (post
  atualizado 31/08/2026) uma funcionalidade de "Automação Fiscal" gratuita até outubro
  de 2026, vendida a escritórios contábeis/BPOs, que busca automaticamente NF-e, NFS-e,
  NFC-e e CT-e nas bases da SEFAZ/prefeituras usando o certificado A1 da própria
  empresa-cliente, integra a sistemas contábeis (Domínio, SCI, Alterdata) e gera
  relatório de crédito de IBS/CBS por fornecedor (f-2026-0083, tier 1, leitura
  integral). *[Corrigido em 2026-09-25, após re-verificação da f-2026-0083: a versão
  anterior deste parágrafo atribuía ao produto também a apuração de DAS/DARF/DARE e as
  obrigações acessórias (EFD, DCTFWeb); na página, isso aparece só na seção genérica
  sobre sistemas de automação fiscal, não na lista das três funcionalidades do
  produto.]* O produto cobre a etapa de captura de documento fiscal e a integração ao
  sistema contábil do escritório; o mecanismo usa o certificado A1 da própria empresa
  (não a Autorização de Acesso sem certificado que o Arkan propõe) e é vendido a
  escritórios contábeis, não diretamente ao dono da PME.
- Omie IA Fiscal (app da própria loja de apps Omie) faz o oposto do que a Conta Azul
  anunciou: só sugere alíquotas/CST/textos legais para emissão de NF-e de produtos, sem
  captura de dado da Receita Federal, apuração consolidada ou execução de obrigação;
  não cobre serviços (NFS-e) (f-2026-0082, tier 1, leitura integral, R$199,90-1.299,90
  /mês por volume de produtos).
- Conta Azul (Regras Fiscais, plano Pro) e Bling (Natureza de Operação) já oferecem
  cálculo automático de imposto na emissão de nota, mas dependente de parametrização
  manual prévia — não é captura/apuração automática de dado consolidado direto da
  Receita Federal (f-2026-0084, leitura resumo_de_busca). *[Nota de 2026-09-25:
  f-2026-0084 está `contradita`: a parte da Conta Azul confere na fonte citada, mas o
  trecho sobre o Bling não está nessa página. Sobre o Bling, ver f-2026-0085.]*
- Não encontrei, especificamente para o Bling, nenhuma menção de captura automática de
  dado fiscal direto do e-CAC/Integra Contador; a página oficial de ajuda do módulo
  fiscal do Bling está bloqueada por Cloudflare e não foi lida (bloqueio não contornado,
  f-2026-0085).
- Avaliação dos apps móveis dos três incumbentes citados como referência de
  insatisfação: Omie iOS 2,3★/131 avaliações (f-2026-0026); Conta Azul de Bolso iOS
  4,8★/~4,6mil avaliações e Android 4,4★/~3,01mil avaliações (f-2026-0028, f-2026-0029)
  — nota alta, contradizendo a alegação do proponente de 2,2-2,3★ para os três
  incumbentes; Bling iOS sem avaliações suficientes e Android com nota só visível para
  segmento Tablet (3,2★/18 avaliações, extração incompleta) (f-2026-0027, f-2026-0030,
  f-2026-0031).

### 3. Solução × alternativas

- Concorrentes de preço baixo citados pelo proponente não competem no mesmo escopo:
  JIM+ (R$39,90/mês) é assistente de marketing/vendas da InfinitePay, sem qualquer
  funcionalidade de contabilidade ou apuração fiscal (f-2026-0054); ROIT START
  (R$499-1.897/mês, não R$250 como alegado) é ferramenta de preparação/simulação para a
  Reforma Tributária, não um serviço contínuo de apuração (f-2026-0055).
- Contabilizei (contabilidade online) tem planos a partir de R$139-195/mês
  (f-2026-0056, verificação pendente).
- Não encontrei nenhum caso nomeado de startup brasileira de contabilidade
  automatizada/fiscal B2B para PME que tenha fechado — só estatísticas genéricas de
  mortalidade de startups sem relação com o setor (f-2026-0077, ausência com escopo de
  busca detalhado).
- Comparável vencedor: Contabilizei captou US$20mi em 2019 (>10 mil clientes, 200
  funcionários à época, f-2026-0068) e hoje se descreve com mais de 100 mil clientes
  (f-2026-0069, agregador de busca sem data precisa).
- Sobre o mecanismo de captura via Integra Contador/e-CAC sem certificado do cliente
  (premissa central do Arkan): a norma vigente é a IN RFB 2.320/2026 (f-2026-0036,
  confirmada em fonte terciária), que segundo reportagens (não texto oficial lido
  integralmente) exige validação da autorização em até 30 dias (f-2026-0037) e **veda
  explicitamente mecanismos de automação/intermediação não oficializados** para
  outorgar/alterar/revogar autorizações (f-2026-0038, corroborado por duas fontes
  independentes em f-2026-0039). A documentação oficial do SERPRO confirma que a
  autenticação do Contratante na API usa o e-CNPJ do próprio Contratante via mTLS, sem
  exigir certificado do contribuinte-cliente para essa etapa (f-2026-0042); e que existe
  um mecanismo de Autorização/Procuração pelo qual o Autor do Pedido de Dados nem sempre
  é o Contratante (f-2026-0043). Um blog de fornecedor (e-Auditoria) descreve a
  Autorização de Acesso no e-CAC sem exigência de certificado do cliente PJ, usando
  login Gov.br + confirmação por app (f-2026-0041, tier 3, verificação pendente). Não
  foi possível ler o texto oficial primário da IN 2.320/2026 nesta linha de tempo do
  projeto (bloqueios de acesso, f-2026-0040).

### 4. Economia unitária

- **Achado novo desta sessão — custo de mão de obra**: um Contador (CBO 2522-10) em
  regime CLT custa em média R$9.430/mês para a empresa (salário + encargos CLT),
  com salário bruto médio de R$5.547,23/mês (piso R$4.246,62, teto R$9.423,34), segundo
  o Portal Salário/CAGED, 81.929 profissionais na amostra (f-2026-0081, tier 2, leitura
  integral via curl). Um Auxiliar Contábil (CBO 4131-10) custa R$4.448/mês para a
  empresa, salário médio R$2.616,37/mês, 164.807 profissionais na amostra (f-2026-0089).
  Dividindo o custo-empresa do contador sênior (R$9.430) por 60 clientes (premissa do
  proponente), o custo de mão de obra sozinho já fica em ~R$157/cliente/mês — acima da
  faixa de variável de R$63-112/cliente/mês declarada pelo proponente para
  Integra Contador + emissor de notas + back-office (que não inclui explicitamente esse
  custo de mão de obra na mesma linha). A base de encargos CLT fixa é 27,44%
  (FGTS+provisões), com custo total do empregador tipicamente entre 1,6x-1,8x o salário
  bruto (70%-180% acima do nominal); empresas do Simples Nacional não pagam INSS
  patronal separadamente, o que reduziria esse custo se a organização contábil operadora
  do Arkan optar pelo Simples (f-2026-0086, tier 3, agregado de calculadoras
  comerciais).
- Custos de fornecedores citados pelo proponente, verificados nas páginas oficiais:
  Focus NFe plano Growth R$548/mês, 4.000 notas + R$0,12/nota adicional (f-2026-0044,
  confirmado); Makro R$195-595/mês por licença/escritório, não por cliente
  (f-2026-0045, confirmado); Calima R$299-399/mês por escritório (f-2026-0046,
  confirmado); Integra Contador/SERPRO cobra por operação em faixas decrescentes de
  preço por volume (R$0,24-0,40 na faixa mais cara por unidade a R$0,06-0,12 na mais
  barata), compatível em ordem de grandeza com a faixa de R$2-4/cliente/mês citada pelo
  proponente, mas via tabela reproduzida por terceiro, não a página oficial da Loja
  SERPRO (renderizada em JS, não lida integralmente, f-2026-0047, pendente). O preço da
  Alterdata Contábil First não é publicado nem no site nem em agregadores checados
  (ausência verificada, f-2026-0048).
- Custos atuais da persona (workaround hoje): Nota Simples R$79,90-139,90/mês
  (f-2026-0049); Meu Emissor R$37,90/mês (f-2026-0050); Nibo R$208-479/mês mensal ou
  R$166-383/mês anual (f-2026-0051); Granatum a partir de R$239/mês (f-2026-0052,
  leitura por resumo de busca, página oficial de planos retornou 404).
- Não existe pesquisa formal (CFC, Sebrae, FENACON) sobre quantas empresas um
  contador/escritório consegue atender por profissional; os únicos números encontrados
  são estimativa informal de blog (20-40 empresas por contador sozinho; ~100
  CNPJs/escritório em média, sem pesquisa por trás, f-2026-0064) e a ausência formal
  registrada (f-2026-0065). **Achado novo**: a única evidência adicional de
  "produtividade com automação" encontrada é conteúdo de marca/publieditorial no portal
  Contábeis, patrocinado pelos próprios fornecedores de software de automação contábil
  "Escritório Inteligente" e "Integra Fácil", alegando 100-300 clientes por colaborador
  — sem metodologia, amostra ou caso verificável independente (f-2026-0088, tier 3,
  classificado como estimativa de vendor interessado).
- Não existe churn publicado por nenhum SaaS fiscal/contábil brasileiro nomeado
  (Omie, Conta Azul, Bling, JIM+, ROIT START, Contabilizei); a única menção é uma
  citação de agregador (sem fonte primária) de que a Conta Azul estaria no decil
  superior (<1%/mês) (f-2026-0066, ausência; f-2026-0067, dado de terceiro sem
  metodologia).
- **Achado novo — custo de estruturação legal**: seguro de Responsabilidade Civil
  Profissional para contadores custa a partir de ~R$50/mês (exemplo de R$4.193,27/ano
  parcelado, f-2026-0090, agregado de páginas comerciais de corretoras) — ordem de
  grandeza pequena frente ao custo do contador, não parecendo por si só inviabilizar a
  estruturação legal antes da primeira venda.

### 5. Distribuição

- Em 2019, a Omie operava canal via 115 franquias e >14.000 escritórios de contabilidade
  parceiros, atendendo 23.000 clientes finais, pagando comissão (royalty de 30% aos
  franqueados) sobre a mensalidade a quem indicou o cliente (f-2026-0070, f-2026-0071,
  ambos verificação pendente, dados de 2019, não atuais).
- Benchmarks agregados (sem metodologia/amostra divulgadas) de CAC por canal para SaaS
  B2B SMB no Brasil: outbound founder-led R$1-4mil; inbound/SEO R$800-3mil; referral
  R$500-2mil; CAC mediano SMB R$3-12mil, ARPA R$300-1.500/mês (f-2026-0076, tier 3).

### 6. Moat e timing

- Dimensionamento do universo: PAC/IBGE 2014 registra 197.950 empresas de comércio
  atacadista no Brasil (todos os regimes, todas as UFs, f-2026-0072); PAC/IBGE 2022
  mostra comércio atacadista com 1,9 milhão de pessoas ocupadas e 51% do faturamento
  total do comércio, R$3,7 trilhões (f-2026-0073). Não encontrei fonte externa (IBGE,
  Receita Federal, Sebrae) que confirme diretamente o recorte específico de 75-200 mil
  empresas do recorte A do proponente (Simples 4a-6a faixa, Anexo I, 6 UFs) — ausência
  verificada com escopo de busca detalhado (f-2026-0074).
- Não existe taxa-base publicada (estudo, associação, banco de dados de VC) para "SaaS
  B2B vertical brasileiro que desaloja incumbente de ERP fiscal/contábil e atinge
  R$16,7M de ARR" (f-2026-0078, ausência com escopo de busca).

## O que procurei e não encontrei

- Nota geral do app Omie no Google Play em formato de texto extraível (f-2026-0031).
- Texto oficial primário da IN RFB 2.320/2026 em fonte Tier 1 (gov.br/DOU) — só
  reportagens de imprensa especializada citando trechos (f-2026-0040).
- Preço público da Alterdata Contábil First (f-2026-0048).
- Pesquisa formal (CFC/Sebrae/FENACON) sobre quantas empresas um contador atende por
  profissional/mês (f-2026-0065).
- Churn publicado de qualquer SaaS fiscal/contábil brasileiro nomeado (f-2026-0066).
- Fonte externa independente que confirme o universo de 75-200 mil empresas do recorte
  A do proponente (f-2026-0074).
- Caso nomeado de startup brasileira de contabilidade automatizada B2B para PME que
  tenha fechado (f-2026-0077).
- Taxa-base publicada para SaaS B2B vertical fiscal/contábil brasileiro atingindo
  R$16,7M ARR (f-2026-0078).
- Pesquisa quantificada sobre quem decide/paga a troca de contador na PME-alvo — dono
  sozinho vs. contador com poder de veto (f-2026-0080).
- Captura automática de dado fiscal direto da Receita Federal/e-CAC/Integra Contador
  especificamente no Bling; a página oficial de ajuda do módulo fiscal do Bling está
  bloqueada por Cloudflare, bloqueio não contornado (f-2026-0085, nova nesta sessão).

## Lacunas e fatos vencidos

- Vários fatos têm `verificacao: "pendente"` (segunda leitura/confirmação cruzada ainda
  não feita): praticamente todos os fatos sobre custos de fornecedores, concorrência de
  preço baixo, dimensionamento do universo, comparáveis vencedores e distribuição por
  canal — a leitura inicial foi feita, mas não houve checagem cruzada por uma segunda
  fonte independente em todos os casos.
- A tabela oficial de preços do Integra Contador na Loja SERPRO é renderizada via
  JavaScript e não pôde ser lida integralmente nesta ou em sessões anteriores; o número
  usado (f-2026-0047) vem de reprodução por terceiro (Grupo Módulos), não da fonte
  primária.
- A leitura do PDF da pesquisa SESCON-SP 2024 foi feita por extração manual de fluxos
  comprimidos (zlib/strings), não por biblioteca padrão de PDF (indisponível no
  ambiente) — os números batem com os rótulos originais, mas o método de extração é
  atípico (f-2026-0035, f-2026-0053).
- O bloqueio por Cloudflare na página de ajuda do Bling sobre o módulo fiscal
  (f-2026-0085) e o retorno apenas de política de cookies nas páginas gov.br sobre a IN
  2.320/2026 (f-2026-0040) são lacunas de acesso, não ausência de evidência real — a
  informação pode existir e não ter sido acessível nesta sessão.
- Os dados de distribuição da Omie via canal de contadores (f-2026-0070, f-2026-0071)
  são de abril de 2019; não há confirmação de que o modelo de comissionamento e a escala
  de franquias/parceiros continuem os mesmos em 2026.
- A alegação do proponente de que os apps de Omie, Conta Azul e Bling têm nota
  2,2-2,3★ (A1 do documento) não se sustenta para Conta Azul (4,4-4,8★ verificado); a
  nota de Bling ficou incompleta na extração e a de Omie foi confirmada só para iOS
  (2,3★) — o padrão de app mal avaliado nas lojas não é uniforme entre os três
  incumbentes citados.
- O achado sobre a "Automação Fiscal" da Conta Azul (f-2026-0083) é uma oferta
  promocional gratuita até outubro de 2026 vendida a escritórios contábeis/BPOs, não ao
  dono da PME diretamente, e usa certificado A1 da empresa-cliente, não o mecanismo de
  Autorização de Acesso sem certificado que o Arkan propõe — a comparação direta entre
  os dois mecanismos técnicos não foi aprofundada nesta sessão por falta de tempo/
  orçamento de busca adicional.

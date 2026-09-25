# Dossiê kill barato: OP-0002 — assistente de gestão contábil e fiscal (Arkan)

Data: 2026-09-25 · Modo: verificação · Escopo: BR · Contrato: 2ª tentativa (1ª anulada por erro de enquadramento) · Buscas/fetches: ~13 buscas nativas + ~25 leituras diretas (curl/r.jina.ai) de páginas e um PDF

Este dossiê verifica as 3 alegações do kill barato listadas em `contrato.json` (`alegacoes_kill`), nesta ordem. Fatos de honorário contábil (f-2026-0032 a f-2026-0035) foram herdados da rodada de pesquisa anterior (contrato agora anulado) e reutilizados pelo id, conforme instruído.

## Alegação 1 — mecanismo de delegação do Integra Contador (SERPRO)

> "O SERPRO permite que a entidade contratante do Integra Contador (usando e-CNPJ A1 próprio, via OAuth2 client_credentials + mTLS) acesse dados fiscais de cada contribuinte-cliente mediante Autorização de Acesso que o próprio contribuinte concede no e-CAC ao CNPJ que figura como autorPedidoDados - dispensando o certificado digital do cliente."

**Status: sustentada**

- **Autenticação do Contratante na API:** a documentação oficial do SERPRO confirma que o Contratante (quem tem o contrato do Integra Contador) autentica-se via OAuth2 `client_credentials` usando **seu próprio** certificado digital e-CNPJ (o mesmo usado na contratação), via mTLS — não o certificado do cliente/contribuinte (f-2026-0042, SERPRO, Tier 1, leitura integral).
- **Delegação Autor do Pedido de Dados → Contratante:** o mecanismo "Autentica-Procurador" da própria API permite que o "Autor do Pedido de Dados" — que "em muitos casos... não é o Contratante da API, mas é um Procurador autorizado previamente pelo Contribuinte pelo portal eCAC" — autorize o Contratante a fazer requisições em seu nome (f-2026-0043, SERPRO, Tier 1, leitura integral). Alguns serviços (ex.: DCTFWeb) exigem que o Autor do Pedido de Dados tenha procuração eletrônica emitida no e-CAC.
- **O cliente não precisa de certificado digital para conceder a autorização:** desde 05/12/2025 a antiga "procuração eletrônica" foi substituída pela "Autorização de Acesso" no e-CAC/Portal de Serviços da Receita Federal. Segundo um guia de fornecedor (e-Auditoria, que vende integração concorrente com o Integra Contador), o responsável legal da empresa-cliente pode logar com **CPF e senha Gov.br** (sem certificado digital), clicar em "Representar" para selecionar o CNPJ da empresa, e conceder a autorização a **qualquer CNPJ** (inclusive o de uma plataforma/escritório), confirmando com código do app Gov.br — "o certificado digital PJ do cliente é opcional" (f-2026-0041, Tier 3, leitura integral).

Combinando as três fontes: o cliente pode delegar acesso ao CNPJ da plataforma via e-CAC usando só login Gov.br (CPF+senha), sem certificado digital próprio; e a plataforma, já sendo o Contratante e (presumivelmente) o Autor do Pedido de Dados, autentica-se na API com seu **próprio** e-CNPJ. O mecanismo descrito na alegação existe e é operacionalmente como descrito. Não encontrei nada nas fontes lidas que contradiga essa descrição.

**Fora do escopo desta verificação** (não fazia parte da alegação a verificar, mas é adjacente): a IN RFB 2.320/2026 e sua vedação a "acesso automatizado"/"acesso intermediado" foi investigada na rodada anterior (ver `contrato-anulado...json` e fatos daquela sessão) e não foi reexaminada aqui — é uma questão distinta (automação do portal vs. delegação via API oficial) que o próprio proponente diz distinguir.

## Alegação 2 — custos de fornecedores que sustentam a economia unitária

> "Back-office contábil licenciado custa R$195-599/mês fixos por escritório (Alterdata Contábil First R$349,80/mês CNPJs ilimitados; Calima R$299-399/mês até 50 empresas; Makro R$195-595/mês); Integra Contador custa R$2-4/cliente/mês; Focus NFe Growth custa R$548/mês por 4.000 notas + R$0,12/nota excedente."

**Status: sustentada parcialmente — confirmada para Makro e Focus NFe; não encontrada (número específico) para Alterdata; plausível mas não confirmada diretamente para Integra Contador por cliente**

- **Makro (ERP contábil):** CONFIRMADO com exatidão. Planos por licença/escritório, não por cliente: Light R$195/mês (até 6 empresas), Básico R$295/mês (12 empresas), Intermediário R$395/mês (25 empresas), Avançado R$595/mês (empresas ilimitadas) — bate exatamente com a faixa "R$195-595/mês" citada (f-2026-0045, página oficial, Tier 1, leitura integral).
- **Calima (ERP contábil):** os dois números citados (R$299 e R$399) são reais, mas a alegação simplifica o detalhe: Calima **Lite** custa "a partir de R$299/mês" para até **10** empresas (sem Integra Contador embutido); Calima **Pro** custa "a partir de R$399/mês" para até **50** empresas (com módulo Integra Contador incluso). Ou seja, R$399/mês — não R$299/mês — é o preço para até 50 empresas (f-2026-0046, página oficial, Tier 1, leitura integral).
- **Alterdata Contábil First:** o valor específico citado (R$349,80/mês) **não foi encontrado**. A página oficial (institucional e a de compra/e-commerce) não publica nenhum valor numérico de mensalidade — só promete "o melhor preço do mercado" e remete a contato comercial/orçamento. Também não achei o número em fontes de terceiros (Capterra, blogs) (f-2026-0048, ausência verificada, Tier 1 quanto à não-publicação, com escopo de busca registrado).
- **Focus NFe, plano Growth:** CONFIRMADO com exatidão total. R$548,00/mês, CNPJs ilimitados, pacote com 4.000 notas, R$0,12 por nota adicional — todos os números batem exatamente com a página oficial de preços (f-2026-0044, Tier 1, leitura integral).
- **Integra Contador, R$2-4/cliente/mês:** a tabela oficial de preços do SERPRO (reproduzida em captura de tela por um fornecedor terceiro, Grupo Módulos, e lida com ferramenta de visão nesta sessão) precifica por **operação consumida no agregado do contratante** (Consulta, Emissão, Declaração), não por cliente final, com preço decrescente por faixa de volume: na faixa mais barata (menor volume), Consulta R$0,24, Emissão R$0,32, Declaração R$0,40; na faixa de maior volume, os preços caem para R$0,06/R$0,08/R$0,12 (f-2026-0047, Tier 3 — reprodução de tabela via terceiro, não a página oficial em si, que é renderizada via JavaScript e não pôde ser lida diretamente nesta sessão). Não há uma tarifa "por cliente/mês" publicada; convertendo por inferência (não confirmada por fonte), supondo ~3-5 operações por cliente/mês, o custo estimado fica entre ~R$1 e ~R$2,50/cliente/mês na faixa de menor volume — mesma ordem de grandeza do R$2-4 citado, mas não uma confirmação direta do número exato.
- A **página oficial da Loja SERPRO** (loja.serpro.gov.br, aba "Preço") existe e deveria ter a tabela primária, mas seu conteúdo é renderizado via JavaScript; as tentativas de leitura direta (curl, r.jina.ai) retornaram a página sem a tabela de preços visível em texto.

## Alegação 3 — âncora de preço (honorário contábil + emissor + sistema financeiro ≈ R$1.100-1.950/mês)

> "Honorário contábil de comércio no Simples Nacional (Fenacon 2014 corrigido pelo IPCA, R$600-1.500; SESCON-SP 2024, mediana R$700 + R$50/empregado) somado a emissor (R$50-150) e sistema financeiro (R$100-300), totalizando ~R$1.100-1.950/mês."

**Status: sustentada parcialmente, com uma correção importante em relação à rodada anterior**

**Honorário contábil (reaproveitando fatos da rodada anterior + 1 fato novo desta sessão):**

- **Fenacon/VOX 2014**, comércio no Simples Nacional: média R$614, mediana R$600, moda R$724 (f-2026-0032, Tier 2, leitura integral). Por funcionário (departamento pessoal): mediana R$30, não R$50 (f-2026-0033).
- **SESCON-SP 2024 — nesta sessão consegui ler o PDF primário integralmente** (diferente da rodada anterior, que registrou isso como lacuna em f-2026-0035 por falta de ferramenta de extração). Usei um extrator manual em Python (descompressão zlib dos content streams + parsing de strings PDF), sem depender de pdftotext/PyPDF2. O documento é a "Pesquisa de Preços e Serviços Praticados pelas Organizações Contábeis do Estado de São Paulo" (SESCON-SP + Instituto Vox Populi, campo de 13-28/jun/2024, amostra de 255 organizações, base 251 para as tabelas de honorário, margem de erro 5,9% a 95% de confiança) — registrado em **f-2026-0053** (Tier 2, leitura integral). Para **Comércio – Simples Nacional**, por porte:
  - até 5 funcionários (≤300 lançamentos/mês): **mediana R$700,00** (média R$783,56, moda R$450,00) — bate exatamente com o "mediana R$700" citado na alegação, mas só para essa faixa de porte.
  - até 10 funcionários (≤600 lançamentos/mês): mediana R$1.000,00 (média R$1.247,62).
  - até 50 funcionários (≤1.000 lançamentos/mês): mediana R$1.950,00 (média R$2.240,05) — este valor bate com o **teto superior (R$1.950)** que a alegação usa para a soma total, mas aqui é só o componente de honorário, sem somar emissor+financeiro.
  - A pesquisa **não segmenta** comércio por atacado/distribuição vs. varejo, e o universo é SP, não nacional (transferibilidade média).
  - O "+R$50/empregado" citado na alegação **não é um número literal da pesquisa**: é uma inferência do proponente. Os saltos reais entre faixas de porte da SESCON-SP sugerem algo entre ~R$60/funcionário (dos 5 aos 10 funcionários) e ~R$24/funcionário (dos 10 aos 50) — na mesma ordem de grandeza, mas não uma taxa linear confirmada de R$50/funcionário.
  - f-2026-0035 foi atualizado (`atualizar fato`) para refletir que o PDF, antes não lido, foi lido nesta sessão.
  - f-2026-0034 (blog Makrosystem citando SESCON-SP, R$1.000/mês para faturamento R$500k-1M) continua como fonte secundária Tier 3, agora superada pela leitura primária (f-2026-0053).

**Emissor de notas fiscais (componente novo, pesquisado nesta sessão):**

- Nota Simples: R$79,90/mês (até 200 notas), R$109,90/mês (até 400 notas), R$139,90/mês (Avançado) (f-2026-0049, Tier 1, leitura integral) — dentro da faixa R$50-150 citada.
- Meu Emissor: R$37,90/mês, notas e usuários ilimitados (f-2026-0050, Tier 1, leitura integral) — **abaixo** da faixa R$50-150 citada, mostrando que existe opção de mercado mais barata que o piso da alegação.
- Conclusão parcial: a faixa R$50-150/mês é plausível e coberta pelos exemplos de mercado, mas não é um piso absoluto (há opção a R$37,90).

**Sistema financeiro (componente novo, pesquisado nesta sessão):**

- Nibo Gestão Financeira: pagamento mensal sem desconto — Light R$208/mês, Plus R$312/mês, Premium R$479/mês; com pré-pagamento anual, R$166/R$250/R$383 (f-2026-0051, Tier 1, leitura integral). O tier de entrada (R$166-208) cabe na faixa R$100-300 citada; o Plus está no limite superior ou logo acima (R$312); o Premium excede bastante.
- Granatum: segundo resultado agregado de busca (não confirmado por leitura integral — a página `/planos` retornou 404 e a página de terceiro não trouxe o valor no texto extraído), planos pagos a partir de ~R$239/mês (f-2026-0052, Tier 3, leitura de resumo de busca) — dentro da faixa R$100-300.
- Conclusão parcial: a faixa R$100-300/mês é plausível para o tier de entrada/intermediário de sistemas financeiros standalone, mas tiers mais completos (Nibo Premium R$479) ultrapassam a faixa — a alegação parece descrever o segmento de entrada, não o mercado inteiro.

**Leitura do conjunto da alegação 3:** a soma total ~R$1.100-1.950/mês é plausível quando se combina o honorário de portes maiores da SESCON-SP (R$1.000-1.950, faixas de 10-50 funcionários) com um emissor de entrada (R$50-150) e um sistema financeiro de entrada (R$100-300). Não é plausível como soma se se usar a mediana da menor faixa de porte (R$700) sozinha mais os dois outros componentes no teto (R$150+R$300=R$450), que dá só R$1.150 — ainda dentro da faixa, na verdade. Ou seja, a faixa proposta (R$1.100-1.950) é ampla o suficiente para acomodar várias combinações plausíveis de porte e fornecedor, mas "mediana R$700 + R$50/empregado" como fórmula literal não é o que a fonte primária mostra (a fonte mostra saltos por faixa de porte, não uma progressão linear por funcionário).

## O que procurei e não encontrei

- Preço público da mensalidade do Alterdata Contábil First — não publicado em nenhuma fonte checada (página oficial, loja institucional, Capterra, blogs de terceiros) (f-2026-0048).
- Tarifa "por cliente/mês" publicada oficialmente para o Integra Contador — a tabela oficial (loja.serpro.gov.br, aba Preço) é renderizada via JavaScript e não pôde ser lida diretamente; usei uma reprodução via captura de tela de um fornecedor terceiro (Grupo Módulos), que mostra preço por operação, não por cliente.
- Confirmação por leitura integral (não resumo de busca) do valor de ~R$239/mês do Granatum — a página oficial de planos retornou 404 e a página de terceiro (b2bstack) não trouxe o número no texto extraído.
- Uma segunda fonte independente e primária para "sistema financeiro R$100-300/mês" além de Nibo (Tier 1) e Granatum (Tier 3) não foi buscada por limite de tempo/orçamento desta sessão — o par já dá triangulação mínima, mas mais pontos fortaleceriam a faixa.

## Lacunas e fatos vencidos

- **Alegação 1:** não reexaminei a questão adjacente da IN RFB 2.320/2026 (vedação a "acesso automatizado/intermediado") nesta sessão — ela não fazia parte da alegação a verificar aqui, mas já havia sido investigada na rodada anterior (contrato anulado) e apontava para uma vedação ampla que o juiz deve considerar junto com esta alegação.
- **Alegação 2:** o preço do Alterdata Contábil First é uma lacuna real (não publicado), não uma alegação refutada — o proponente pode ter obtido o número R$349,80 por contato comercial direto, que não deixa rastro público. A tarifa "por cliente" do Integra Contador não tem fonte primária direta nesta sessão (só a tabela por operação, via terceiro); o valor por cliente do proponente é uma conversão/estimativa, plausível mas não verificada em fonte primária.
- **Alegação 3:** ao contrário da rodada anterior, o PDF do SESCON-SP 2024 **foi lido integralmente** nesta sessão (f-2026-0053), resolvendo a lacuna anterior (f-2026-0035, atualizado). Os componentes de emissor e sistema financeiro têm cobertura de mercado (2-3 exemplos cada, majoritariamente Tier 1), mas não uma pesquisa exaustiva — não busquei, por exemplo, preços de Asaas, Conta Simples ou InfinitePay como "sistema financeiro" adicional, nem outros emissores como NFE.io ou Otimizou além dos citados.
- **Orçamento de busca:** usei ~13 buscas nativas (WebSearch) mais numerosas leituras diretas via curl/r.jina.ai (não contam para o teto de busca nativa, mas consomem tempo). Ficou dentro da faixa de 15-20 buscas pedida, sem repetir o estouro da rodada anterior.

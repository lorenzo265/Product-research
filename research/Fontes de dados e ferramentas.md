# Colete o governo, busque as plataformas

O harness deve transformar em script coletor só as fontes que são **estruturadas, recorrentes e legalmente abertas**. Em 2026, quase todas elas são governamentais ou globais de acesso livre. As principais são o **PNCP** (compras públicas com valor obrigatório), as contagens de CNPJ, o consumidor.gov.br e o 99Freelas, além do trio de arbitragem **yc-oss, Hacker News e TrustMRR**. Depois vêm as avaliações em português do Google Play, os comentários do YouTube, o DOU com o Querido Diário e as vagas da Gupy. Consultas pontuais a dados de governo passam pelo servidor MCP **`mcp-brasil`** (533 ferramentas, 66 APIs sem chave). O que é fechado, não tem API ou tem termos incertos fica na busca web: Reclame Aqui, lojas de apps de Nuvemshop, VTEX, Bling e Omie, Workana, GetNinjas, agendas regulatórias, Indie Hackers e Reddit. Saem da lista:

- LinkedIn e Vagas.com.br, que bloqueiam bots de IA pelo nome;
- a busca do Mercado Livre, que responde 403 a apps externos;
- a raspagem de Upwork e Fiverr;
- a API do Reddit sem aprovação;
- o Google Trends via pytrends, repositório arquivado;
- o Exploding Topics, a partir de US$249 por mês;
- a mineração de avaliações do Google Places;
- microdados de saúde, vedados pela LGPD, art. 11.

Na busca, a WebSearch nativa continua como base, mas não serve para guardar evidência. Ela devolve só título e URL, divide um teto de 200 chamadas por sessão com todos os subagentes e não aceita país nem idioma. Somar MCPs gratuitos custa zero: Exa para achar empresas, Parallel para buscas em volume, Jina ou `curl` para o texto literal. Nenhum pagamento se justifica antes de uma sonda própria com 30 a 50 consultas em português. A implementação começa pela base comum e pelo **yc-oss, a única fonte que responde desta nuvem hoje**. Depois vêm PNCP, 99Freelas e consumidor.gov.br, na fatia vertical da Fase 3. Uma ressalva vale para todo o relatório: **nenhuma API foi chamada ao vivo**. O bloqueio de rede descrito em R-02 se repetiu nesta sessão.

**Como ler as marcas de verificação.** Cada fato relevante leva uma marca:

| Marca | Significado |
|---|---|
| **[V]** | Verificado na fonte primária: documentação oficial, README oficial do mantenedor, registro PyPI ou npm, ou checagem feita por mim nesta sessão (24/09/2026). |
| **[T]** | Terceiro com evidência datada: repositório de outra pessoa que usa a API, com código ou checagem de 2026. |
| **[R]** | Resumo de busca: a página original não foi aberta. |
| **[C]** | Número publicado por concorrente. Quase todos os preços de APIs de busca vêm do espelho público da Parallel, que compete com elas. |
| **[I]** | Inferência minha. |

Nesta sessão, testei de novo 13 endpoints. **Onze falharam no CONNECT com 403 do proxy**: PNCP, IBGE, Querido Diário, Receita, HN Firebase, HN Algolia, 99Freelas, Mercado Livre, Reddit e os MCPs hospedados de Exa e Parallel. Só `pypi.org` e `raw.githubusercontent.com` responderam [V]. A API do GitHub também não está habilitada nesta sessão [V].

## Governo abre dados, plataformas privadas fecham

A assimetria mais importante do levantamento é esta: **o Estado brasileiro expõe quase tudo por API oficial gratuita, enquanto as plataformas privadas onde a dor aparece estão se fechando**. Do lado público, quase nada exige raspagem. A exceção é a página de busca do DOU, e o INLABS, da Imprensa Nacional, entrega as edições completas em XML e PDF desde 2020, com scripts oficiais de download ([Imprensa-Nacional/inlabs](https://github.com/Imprensa-Nacional/inlabs)) [V]. Esses scripts fazem login com e-mail e senha. Um terceiro, porém, afirma que o INLABS exige aprovação institucional ([brazil-visible, dou.md](https://github.com/nferdica/brazil-visible/blob/main/docs/apis/diarios-oficiais/dou.md)) [T], e essa divergência continua aberta. O PNCP tem API de consulta sem chave, com endpoints de contratações, contratos, atas e **`/pca`, os planos anuais de contratação**. Cada página traz até 50 contratações ou 500 contratos, e períodos acima de 365 dias devolvem 422 ([mcp-brasil 0.14.0](https://pypi.org/project/mcp-brasil/0.14.0/); [pncp-cli](https://github.com/AnxietyLab/pncp-cli)) [T]. Li o README do `pncp-cli` direto: a ferramenta usa só a biblioteca padrão, cobre as duas APIs REST oficiais e a busca do portal, e já embute uma skill do Claude Code. A versão 2.0.0 saiu no PyPI em 31/07/2026 ([PyPI pncp-cli](https://pypi.org/project/pncp-cli/)) [V]. O arquivo de fontes do `mcp-brasil` classifica o PNCP como risco baixo, porque a publicação é obrigatória pela Lei 14.133/2021 ([SOURCES.md](https://github.com/Mcp-Brasil/mcp-brasil/blob/main/SOURCES.md)) [V].

O cadastro de CNPJ da Receita sai em ZIP e CSV mensais, com cerca de **57 a 60 milhões de registros** ([brazil-visible, cnpj-completa.md](https://github.com/nferdica/brazil-visible/blob/main/docs/apis/receita-federal/cnpj-completa.md); [rictom/cnpj-sqlite](https://github.com/rictom/cnpj-sqlite)) [T]. Há quatro armadilhas:

- guarda só o retrato mais recente;
- tem atraso de 30 a 60 dias;
- o layout dos sócios mudou em agosto de 2026;
- desde julho de 2026 existem CNPJs alfanuméricos, que quebram validadores de 14 dígitos.

O Querido Diário funciona sem autenticação, mas a cobertura é incerta. Terceiros falam em 350+, 370+ ou cerca de 1.047 dos 5.570 municípios ([SmartLic STORY-255](https://github.com/tjsasakifln/SmartLic/blob/HEAD/docs/stories/STORY-255-querido-diario-adapter.md); [brazil-visible](https://github.com/nferdica/brazil-visible/blob/main/docs/apis/diarios-oficiais/does-estaduais.md)) [T]. O README do `mcp-brasil`, que conferi, promete "5.000+ cidades" ([mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil)) [V], mas o código do próprio projeto lista só 20 capitais confirmadas [T].

Do lado privado, o quadro é outro:

- **Mercado Livre:** desde 2025–26, `/sites/MLB/search` responde "403 forbidden, always. Endpoint deprecated for external apps", mesmo com token OAuth válido ([victornoleto/carros](https://github.com/victornoleto/carros/blob/master/curva-docs/context/mercadolivre-status.md); [Teilor-MIA](https://github.com/investidor18economia/Teilor-MIA/blob/master/docs/mercadolivre-developer-escalation-403.md)) [T].
- **Reclame Aqui:** não tem API pública. Um projeto de 2026 recebeu 403 a partir do deslocamento 490 e viu IPs do Colab bloqueados de imediato pelo Cloudflare ([meurii/churn-intelligence](https://github.com/meurii/churn-intelligence)) [T].
- **Vagas.com.br e LinkedIn:** o robots.txt bloqueia pelo nome ClaudeBot, GPTBot e congêneres, segundo leitura de 08/08/2026 ([br-skill, carreira-scanner-br.md](https://github.com/Atroci/br-skill/blob/main/references/carreira-scanner-br.md)) [T].
- **Reddit:** desde novembro de 2025, pela Responsible Builder Policy, todo acesso à API exige aprovação explícita. O uso comercial custa US$0,24 por mil chamadas ([Reddit Help](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy); [Octolens](https://octolens.com/blog/reddit-api-pricing)) [R].
- **Product Hunt:** a API proíbe uso comercial sem acordo ([Product Hunt API](https://api.producthunt.com/v2/docs)) [R].
- **Google Trends:** a API oficial segue em alfa, com lista de acesso fechada ([Google Search Central](https://developers.google.com/search/blog/2025/07/trends-api)) [R]. O pytrends foi arquivado em abril de 2025 e está parado no PyPI desde 2023 ([PyPI pytrends](https://pypi.org/project/pytrends/)) [V].

Algumas fontes privadas ainda têm acesso utilizável:

- **99Freelas:** HTML renderizado no servidor e robots.txt permissivo em `/projects` ([br-skill, propostas-scanner-br.md](https://github.com/Atroci/br-skill/blob/main/references/propostas-scanner-br.md)) [T].
- **Gupy:** o domínio `www.gupy.io` libera bots de IA explicitamente [T].
- **Catho:** permite bots de IA nas páginas de vaga, mas não na busca [T].
- **Empregare:** tem um **servidor MCP oficial** em `/api/mcp` [T].
- **Hacker News:** a API Firebase declara "no rate limit" ([HackerNews/API](https://github.com/HackerNews/API)) [V].
- **yc-oss:** publica todo dia um JSON com **6.248 empresas lançadas pela YC**, e só 51 delas localizadas no Brasil ([yc-oss/api](https://github.com/yc-oss/api)) [V].

Essa assimetria define o radar. As lentes que dependem de dado público são bem servidas: baixa penetração (1), fragmentação (3), choque regulatório (4), trabalho manual (5) e ineficiência cifrada (6). A arbitragem (7) conta com fontes globais abertas. Já o ecossistema de plataforma (9) e a dor declarada (11) dependem justamente das fontes que fecharam. O próprio fechamento também é sinal. O corte da busca do Mercado Livre quebrou ferramentas de comparação de preço que dependiam dela [I], e isso é candidato a cartão nas lentes 4 ou 9.

## Uma regra decide o destino de cada fonte

Quatro condições decidem se uma fonte vira script:

1. o acesso é oficial, ou robots.txt e termos de uso permitem;
2. o dado é estruturado;
3. o valor está na série temporal ou na recorrência, e não numa consulta isolada;
4. o volume excede o que cabe no contexto do modelo.

Coletor próprio se justifica porque o harness precisa de deduplicação, histórico e procedência por registro em `sinais.jsonl`, e uma chamada MCP não entrega nada disso. Filtrar em código antes de o dado chegar ao contexto também é a recomendação da Anthropic: carregar ferramentas MCP pelo sistema de arquivos reduziu o consumo de 150 mil para 2 mil tokens ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)) [V]. Os outros destinos são mais simples. Consultas pontuais de pesquisador ou verificador sobre dado público vão por **MCP**. Material desestruturado, fechado ou com termos não lidos fica na **busca web**, para checagens pontuais. Uma fonte vai para **evitar** quando robots.txt ou termos de uso proíbem, quando o custo é desproporcional ou quando o risco de LGPD é alto.

| Lente | Melhores fontes | Método de acesso | Evitar | Observação |
|---|---|---|---|---|
| **1 · Baixa penetração de software** | Contagem de CNPJ por CNAE × porte × UF [T]; IBGE CEMPRE, tabelas 9509 e 9528 [T] | Coletor mensal só de contagens; CEMPRE via MCP (`mcp-brasil ibge`) ou coletor fino | Listas de sócios, telefones e e-mails | Dá o **denominador**. Nenhuma fonte estruturada mede adoção de software; o numerador sai da busca web (base de clientes declarada por fornecedores) [I] |
| **2 · Incumbente caro e odiado** | consumidor.gov.br [T]; avaliações pt-BR no Google Play [V para a biblioteca]; Reclame Aqui [T] | Coletor mensal (consumidor.gov.br); coletor Play (testar antes); Reclame Aqui só via busca `site:` | Raspagem em massa do Reclame Aqui; mineração do Google Places | Contagem de reclamações por empresa dá recorrência por construção |
| **3 · Fragmentação** | CNPJ por porte (fatia de micro e EPP) [T]; CEMPRE [T]; CKAN da ANEEL e da ANS [T] | Mesmo coletor da lente 1; CKAN via MCP | Google Places para densidade (no máximo 5 avaliações por local, pago) | — |
| **4 · Choque regulatório com prazo** | DOU via INLABS XML, Seções 1 e 3 [V]; Querido Diário, cidades nível 3 [T]; agendas regulatórias obrigatórias pela Lei 13.848/2019 [T]; `mcp-fiscal-brasil` para IBS/CBS [T] | Coletor de palavras-chave ("obrigatoriedade", "prazo", "credenciamento"); agendas via busca web | Raspagem da página de busca do DOU; Seção 2 (atos de pessoal) | Prazo explícito no texto é o sinal mais forte |
| **5 · Trabalho manual em escala** | Novo CAGED e RAIS por CBO × CNAE via Base dos Dados [T]; páginas de empresa da Gupy [T]; MCP oficial da Empregare [T] | Script SQL no BigQuery (sem coletor de FTP); coletor Gupy; MCP Empregare | LinkedIn, Vagas.com.br | Número de pessoas numa ocupação mede o tamanho da tarefa manual |
| **6 · Ineficiência cifrada** | Preços homologados no PNCP [T]; fila de análise da ANVISA [T]; massa salarial da RAIS em funções manuais [T] | Coletor PNCP; coletor ANVISA só se uma tese tocar saúde; SQL RAIS | Microdados de saúde (LGPD art. 11) | A cifra já vem no dado |
| **7 · Arbitragem geográfica** | yc-oss [V]; TrustMRR, API com MRR verificado [R]; Show HN [V]; Exa MCP para achar empresas com restrições [C]; ListaMRR para checar equivalente brasileiro [R] | Coletores yc-oss, TrustMRR e HN; Exa via MCP; Acquire, Indie Hackers e Starter Story por leitura manual ou busca web | API do Product Hunt em uso comercial sem permissão; raspagem do Acquire via Apify | Receita verificada é o sinal de "já funciona lá fora" com maior diagnosticidade |
| **8 · Nova capacidade de IA** | Descrições de vagas (Gupy, Empregare, Programathor) [T]; HN [V]; changelogs de modelos | Coletor Gupy com termos de tarefa manual; busca web | — | Cruzar com a lente 5: tarefa manual volumosa que ficou automatizável |
| **9 · Ecossistema de plataforma** | Páginas das lojas Nuvemshop, VTEX e RD Station [T]; avaliações pt-BR no Google Play dos apps de ERP [I]; Shopify App Store como referência | Busca web e leitura manual; micro-coletor só depois de checar robots.txt e termos | Tratar número de instalações como dado: não foi encontrado em nenhuma das sete lojas | **Maior lacuna de dados da pesquisa** |
| **10 · Serviço manual já comprado** | 99Freelas [T]; `averagePrices` do GetNinjas [T]; Workana [T] | Coletor diário do 99Freelas; GetNinjas e Workana via busca web | Upwork, Fiverr, Freelancer.com.br (Cloudflare e robots.txt) | Orçamento e número de propostas mostram preço já pago |
| **11 · Dor declarada com cifra** | PNCP e PCA [T/V]; comentários do YouTube em tutoriais de ERP [T]; consumidor.gov.br [T]; Ask HN [V]; Reddit e Reclame Aqui via busca | Coletores PNCP, YouTube (canais semeados) e consumidor.gov.br; o resto na busca web | API do Reddit sem aprovação; perguntas do Mercado Livre (403) | O PNCP corrige a baixa diagnosticidade: a cifra é obrigatória |

Três leituras da tabela mudam o desenho das lentes. A primeira: a arquitetura avisa que a **lente 11 tem baixa diagnosticidade** e só vale com cifra ou recorrência. A solução está nas fontes cuja estrutura já obriga uma das duas. O PNCP exige valor estimado e publica o plano anual antes da licitação. O consumidor.gov.br agrega reclamações finalizadas por empresa ([danzeroum/juridico-platform](https://github.com/danzeroum/juridico-platform)) [T]. O 99Freelas mostra orçamento e número de propostas. Fórum solto fica como fonte de hipótese, não de evidência.

A segunda leitura: a **lente 9 é a mais cega**. Nuvemshop, VTEX e RD Station têm páginas públicas por app, mas não apareceu API de listagem, feed de avaliações nem contagem de instalações em nenhuma das sete lojas. Para Bling, Tiny/Olist, Omie e Conta Azul não apareceu evidência alguma ([vtex/toolbelt](https://github.com/vtex/toolbelt/blob/HEAD/src/modules/apps/install.ts); [airbyte, rd-station](https://github.com/airbytehq/airbyte/blob/HEAD/docs/integrations/sources/rd-station-marketing.md)) [T]. Antes de qualquer coletor, é preciso uma checagem manual de dez minutos por loja.

A terceira: a **lente 7 é a mais bem servida por dado verificado**. O TrustMRR liga receita a Stripe, LemonSqueezy e Paddle, e a API aceita de 10 a 60 requisições por minuto ([TrustMRR API](https://trustmrr.com/docs/api)) [R]. Os números de cobertura divergem: "840+ startups" segundo um terceiro, "470+" segundo outro. O yc-oss já vem com status, setor, tamanho do time e regiões. Um detalhe prático: a biblioteca Python oficial do Querido Diário parou no PyPI em 2021 (versão 0.0.2) [V], então o coletor deve chamar a API direto.

## A busca nativa acha URLs, mas não guarda evidência

A WebSearch do Claude Code "returns result titles and URLs. It doesn't fetch the result pages". Pode disparar até oito buscas no backend por chamada, e o backend "is not configurable". Para usar outro provedor, é preciso adicionar um servidor MCP. O teto é de **200 chamadas por sessão, somando a conversa principal e todos os subagentes**. A variável `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` eleva esse teto, mas não o remove ([Claude Code tools reference](https://code.claude.com/docs/en/tools-reference)) [V]. O esquema da ferramenta observado na Fase 2 só aceita `query`, `allowed_domains` e `blocked_domains`, e se descreve como "US-only": não há parâmetro de país [V, observação da sessão].

A WebFetch é "lossy by design". Um modelo pequeno lê uma versão truncada da página e devolve só a resposta à pergunta feita, não o texto [V]. Isso **colide diretamente com R-05**, que exige guardar o trecho literal de cada fato. Trecho literal tem que vir de `curl`, do `r.jina.ai` (Markdown da página inteira, sem chave, com limite de taxa) ou dos fetch dos MCPs Firecrawl e Parallel ([jina-ai/reader](https://github.com/jina-ai/reader)) [V]. O teto de 200 buscas não é teórico: os 13 pesquisadores da Fase 2 o esgotaram (R-02).

| Ferramenta | Preço de lista | Faixa gratuita | MCP oficial | Marca |
|---|---|---|---|---|
| WebSearch / WebFetch nativas | Incluídas no Claude Code; na API, busca a US$10 por mil mais tokens, fetch só tokens | Teto de 200 buscas por sessão | Nativas | [V] |
| Parallel Search | US$1 por mil (Turbo, Fast); US$5 por mil (Basic, Advanced) | US$5/mês em créditos; MCP hospedado sem chave, "personal and hobby use" | Sim | [V, primeira parte] |
| Exa | US$7 por mil, com conteúdo | US$20 no cadastro mais US$10/mês | Sim, anônimo com limite | [C] preço; [V] MCP |
| Tavily | US$5–8 por mil (básica) | 1.000 créditos/mês | Sim, com chave | [C] |
| Perplexity Search | US$5 por mil | Não informado | Sim, com chave | [C] |
| Brave | US$5 por mil | US$5/mês com cartão; armazenar resultados exige plano com esse direito | Sim, local | [C] |
| Firecrawl | A partir de US$16 por 5 mil créditos (plano anual) | 1.000 créditos/mês; MCP sem chave | Sim | [C] |
| Jina Reader | Cerca de US$0,05 por milhão de tokens | 10 milhões de tokens; `r.jina.ai` sem chave | Sim | [C] / [V] |
| SerpApi | US$25/mês por mil buscas | 250/mês | Sim | [C] |
| Google Programmable Search | US$5 por mil | Fechado a novos clientes; **encerra em 1/1/2027** | — | [C] |

Fontes da tabela: [Claude web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool); [Parallel, free APIs](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-free-web-search-api.md); [Exa MCP](https://github.com/exa-labs/exa-mcp-server); [Brave vs Parallel](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/brave-search-api-vs-parallel.md); [Parallel search-mcp](https://github.com/parallel-web/search-mcp); [Google CSE alternative](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/the-best-google-custom-search-api-alternative-for-ai-agents.md).

As evidências de qualidade são fracas e quase sempre passam por um fornecedor. Os dois placares independentes encontrados só foram lidos pelos relatos da Parallel [C]. No Artificial Analysis Search Index, de agosto de 2026, **os quatro primeiros ficam a 1 ou 2 pontos um do outro**: Parallel Advanced 75, Brave 75, You.com 74 e Exa 74 ([Parallel sobre o AA](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/blog/artificial-analysis-best-search-api.md)). Na busca de empresas com várias restrições do Openbenchmarks, com o agente fixo, o provedor muda muito o resultado:

| Configuração | Provedor | F1 |
|---|---|---|
| Só busca | Parallel basic | 46,5 |
| Só busca | Exa deep | 45,4 |
| Só busca | Brave e Firecrawl | cerca de 30 |
| Busca mais fetch | **Exa deep** | **48,2**, o melhor resultado |

Fonte: [Parallel, company research](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/articles/best-api-for-company-research.md). Esse tipo de consulta é a própria lente 7: "empresas lá fora com receita, sem sede no Brasil, time pequeno".

Os placares rodados pelos próprios fornecedores se contradizem. No harness da Perplexity, o agente da Parallel marca 0,56 no BrowseComp ([perplexityai/search_evals](https://github.com/perplexityai/search_evals)) [V]. No harness da Parallel, a Task API marca de 88% a 94% ([Parallel benchmarks](https://github.com/parallel-web/parallel-llms-txt/blob/main/public/benchmarks.md)). A própria Anthropic mediu que **o uso de tokens sozinho explica 80% da variância no BrowseComp** ([Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)) [V]. Nenhum fornecedor publica resultado com consultas em português ou sites brasileiros.

A conclusão é que o desenho do harness pesa mais do que o provedor na pesquisa geral. Trocar de provedor só compensa em dois casos: descoberta de entidades com restrições e resultados presos a um país. Por isso, a decisão A-04 tem uma resposta barata:

- manter a nativa para descoberta;
- somar Exa (lente 7) e o MCP gratuito da Parallel (buscas em volume fora do teto de 200);
- usar Jina ou `curl` para trechos literais e Firecrawl sem chave para páginas com muito JavaScript;
- só pagar depois da sonda em português.

Se a sonda justificar pagamento, a Parallel Fast ou Turbo, a US$1 por mil, custa um décimo da busca da API Claude. Uma ressalva: o MCP gratuito da Parallel é para uso pessoal, e um harness que busca receita tende ao uso comercial. A saída é migrar para a chave paga quando o volume aparecer [I]. O Brave só entra se a sonda mostrar ganho com `country=BR`, porque a cláusula de armazenamento conflita com guardar trechos em `fatos.jsonl` [C].

## LGPD e termos de uso cortam mais fontes que o custo

O custo quase não pesa. Todas as fontes recomendadas para coletor são gratuitas, e as poucas cotas cobrem o uso previsto:

| Recurso | Limite ou custo |
|---|---|
| YouTube Data API | 10 mil unidades por dia; `commentThreads.list` custa 1 unidade e `search.list` custa 100 ([airbyte, source-youtube-data](https://github.com/airbytehq/airbyte/blob/HEAD/airbyte-integrations/connectors/source-youtube-data/AGENTS.md)) [T] |
| BigQuery da Base dos Dados | 1 TB de consulta grátis por mês ([brazil-visible, base-dos-dados.md](https://github.com/nferdica/brazil-visible/blob/main/docs/apis/portais-centrais/base-dos-dados.md)) [T] |
| MCPs de busca | Gratuitos na faixa inicial |

Com isso, o radar roda sem pedir nada à decisão A-02 (caixa disponível). O que corta fontes é a lei e o contrato.

Três dispositivos da LGPD enquadram tudo. O art. 7º, §3º, diz que dado pessoal de acesso público deve ser tratado conforme a finalidade que justificou sua publicação. O §4º dispensa consentimento para dado tornado manifestamente público pelo titular. O §7º admite tratamento posterior para finalidade legítima e específica ([Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)) [T: citado do texto legal de memória pelo pesquisador; a página não abriu]. A consequência prática mais séria é para o estágio 5 do funil. O cadastro de CNPJ traz telefone e e-mail dos estabelecimentos e nome dos sócios ([brazil-visible, estabelecimentos.md](https://github.com/nferdica/brazil-visible/blob/main/docs/apis/receita-federal/estabelecimentos.md)) [T], e montar listas de prospecção com esses dados é **tentador e fora da finalidade** [I]. O coletor de CNPJ grava só contagens agregadas.

O art. 11, §4º, veda comunicar dado de saúde para obter vantagem econômica, e por isso o `mcp-brasil` classifica saúde como risco **crítico**. O DataJud é risco alto, porque as resoluções CNJ 331/2020 e 446/2022 vedam redistribuição em massa ([SOURCES.md](https://github.com/Mcp-Brasil/mcp-brasil/blob/main/SOURCES.md)) [V]. As outras fontes pedem cuidados de rotina: guardar trechos e não pessoas no Querido Diário; pular a Seção 2 do DOU; manter só agregados dos clientes do 99Freelas; guardar o texto dos comentários do YouTube sem o nome de quem comentou.

Nos termos de uso, a evidência é quase toda de terceiros e datada de agosto e setembro de 2026. Os termos da BrasilAPI pedem para não usar "automated forms of crawling" ([BrasilAPI](https://github.com/BrasilAPI/BrasilAPI)) [T], então consultas de CNPJ em lote vão pelo dump, nunca por ela. O padrão de conduta mais sólido encontrado é o da `br-skill` ([propostas-scanner-br.md](https://github.com/Atroci/br-skill/blob/main/references/propostas-scanner-br.md)) [T], e vale copiá-lo:

- reler o robots.txt, incluindo as regras nominais para bots de IA, antes de implementar a fonte;
- usar um único User-Agent descritivo, sem rotação;
- nunca contornar desafio do Cloudflare.

Os termos de Reclame Aqui, Gupy, Catho, Indeed, Workana, 99Freelas, GetNinjas, Google Maps, TrustMRR, Acquire e das lojas de apps do Google e da Apple **não foram lidos por ninguém nesta pesquisa**. Cada coletor sobre essas fontes nasce com a leitura de termos como tarefa zero.

O `mcp-brasil` já traz o molde de governança. Cada fonte tem licença, risco e atribuição em `SOURCES.md`, e a variável `MCP_BRASIL_LGPD_ALLOW_PII` vem vazia por padrão, ou seja, desligada ([mcp-brasil README](https://github.com/Mcp-Brasil/mcp-brasil)) [V]. O harness deve copiar esse modelo num `fontes.yaml` próprio, com a data da última checagem de robots.txt e termos. O texto coletado continua sendo dado não confiável, como define R-12.

## Backlog de coletores: provar o pipeline com yc-oss, depois PNCP

A ordem abaixo segue cinco critérios:

1. o coletor roda onde a rede permite;
2. serve à fatia vertical da Fase 3, que atravessa a trilha M ou S (D-006);
3. entrega cifra ou recorrência;
4. tem risco legal baixo;
5. exige pouco esforço.

A Fase 3 fica com quatro coletores e a camada de MCP, de propósito. A seção 10 da arquitetura lista como risco "construir o harness em vez de ganhar dinheiro", e cada coletor a mais adia o primeiro teste com comprador.

| # | Coletor | Lentes | Trilhas | Acesso e custo | Roda nesta nuvem hoje? | Risco de termos/LGPD | Fase |
|---|---|---|---|---|---|---|---|
| 0 | **Base comum**: cliente HTTP com User-Agent fixo, checagem de robots.txt, limite de taxa, respostas gravadas para testes offline, gravação no schema de `sinais.jsonl`, registro `fontes.yaml` | todas | — | — | Sim (offline) | — | 3 |
| 1 | **yc-oss**: diff diário de `companies/all.json` e `changes/latest.json` | 7 | M, G | JSON estático no GitHub, grátis | **Sim**: `raw.githubusercontent.com` respondeu 200 [V] | Baixo | 3 |
| 2 | **PNCP**, envolvendo o `pncp-cli` 2.0.0: contratações abertas, PCA e preços homologados | 11, 4, 6, 1 | S, M, G | API oficial sem chave; janelas de até 365 dias | Não | Baixo | 3 |
| 3 | **99Freelas**: projetos diários por categoria, com orçamento e propostas | 10, 11 | S | HTML público, robots.txt permissivo | Não | Médio: só agregados; termos não lidos | 3 |
| 4 | **consumidor.gov.br**: reclamações finalizadas por empresa e setor | 2, 11 | M, S | CSV aberto mensal | Não | Baixo (anonimizado) | 3 |
| 5 | **Contagens de CNPJ** por CNAE × porte × UF, conferidas contra o CEMPRE | 1, 3, dimensionamento | todas | Dump de ~60 GB ou SQL na Base dos Dados | Não | Médio: só contagens | 4 |
| 6 | **Hacker News** (Firebase e Algolia): Ask HN, Show HN, "I'd pay for" | 7, 8, 11 | M | Grátis, sem chave | Não | Baixo | 4 |
| 7 | **TrustMRR**: catálogo com MRR verificado, filtro fora do Brasil | 7 | M | Chave, 10 a 60 requisições/min | Não | Termos não lidos | 4 |
| 8 | **Google Play pt-BR**: avaliações de incumbentes, de apps estrangeiros e de apps de ERP | 2, 11, 9, 7 | M | Biblioteca não oficial | Não | Termos da loja não lidos | 4, após teste |
| 9 | **YouTube**: comentários em tutoriais de canais semeados, sem `search.list` | 11, 8, 2 | M, S | API oficial, cota gratuita | Não | Comentaristas são dado pessoal: sem nomes | 4 |
| 10 | **DOU via INLABS** (Seções 1 e 3) e **Querido Diário** (cidades nível 3): lista de palavras-chave | 4 | G, M | Login gratuito no INLABS; API do Querido Diário sem chave | Não | Baixo | 4 |
| 11 | **Gupy** (páginas de empresa) e **Empregare** (MCP) | 5, 8 | S | JSON renderizado no servidor; MCP oficial | Não | Termos da Gupy não lidos | 4 |
| 12 | **CAGED e RAIS**: script SQL na Base dos Dados, sem coletor de FTP | 5, 6, 1 | S, G | BigQuery, 1 TB/mês grátis | Não | Baixo | 4 |
| 13 | **ANVISA**: retratos da fila de análise | 6, 4 | G | OAuth via gov.br mais CSV | Não | Médio | Só se uma tese exigir |

O yc-oss vem primeiro por um motivo operacional, não por valor de sinal. É **a única fonte do backlog que pode ser testada ao vivo nesta nuvem**, e por isso prova o pipeline de ponta a ponta antes da decisão de rede: coleta, schema, deduplicação, gravação em `sinais.jsonl` e validação. Três coletores ficam para depois:

- **Catho**, pelo sitemap, depois de ler os termos;
- **Workana**, com navegador headless, se o 99Freelas provar a lente 10;
- **lojas de apps**, depois da checagem manual.

O Reddit só volta como coletor se a aprovação sair.

Na Fase 3, o dimensionamento da fatia vertical usa o CEMPRE via `mcp-brasil`, e o coletor de CNPJ entra na Fase 4. O dump completo pede cerca de 60 GB de disco livre para gerar um banco de ~30 GB ([rictom/cnpj-sqlite](https://github.com/rictom/cnpj-sqlite)) [T]. Pela D-005, esse volume nunca entra no git: o dado bruto fica em cache fora do repositório, e só os agregados são versionados.

Este relatório **concorda com o padrão de R-02**: coletores com testes offline sobre respostas gravadas, prontos para rodar onde a rede permitir. Na escolha entre as opções (a) e (b), recomenda a (a) para as APIs oficiais. O radar semanal da Fase 5 tende a rodar como Routine, e o ambiente padrão das Routines é de lista de permissão, com "403 host_not_allowed" para o resto ([Routines](https://code.claude.com/docs/en/routines)) [V, segundo as notas de engenharia de agentes]. A opção (b) fica como reserva para fontes que bloqueiam IP de datacenter. Nenhum coletor recomendado depende dela, porque as fontes que fazem isso (Reclame Aqui, Mercado Livre) já estão fora.

Há **discordância com a lista mínima de domínios** de R-02 em três pontos:

| Domínio | Está em R-02? | Recomendação | Motivo |
|---|---|---|---|
| `www.reddit.com` | Sim | Retirar até haver aprovação | A Responsible Builder Policy exige aprovação prévia para qualquer acesso [R] |
| `api.mercadolibre.com` | Sim | Retirar | A busca responde 403 a apps externos mesmo com OAuth [T] |
| `dadosabertos.rfb.gov.br` | Sim | Somar `arquivos.receitafederal.gov.br` e confirmar qual serve o dump | As notas apontam o dump em `arquivos.receitafederal.gov.br/dados/cnpj/` [T] |
| `queridodiario.ok.org.br` | Sim | Somar `api.queridodiario.ok.org.br` | A base da API fica no subdomínio [T] |
| `arxiv.org`, `export.arxiv.org` | Sim | Manter para sessões de pesquisa, fora da lista dos coletores | Nenhuma lente usa arXiv |
| `pncp.gov.br` | Não | Adicionar | Coletor nº 2 |
| `www.99freelas.com.br`, `consumidor.gov.br`, `inlabs.in.gov.br`, `hacker-news.firebaseio.com`, `trustmrr.com`, `play.google.com`, `www.googleapis.com`, `bigquery.googleapis.com` | Não | Adicionar conforme o coletor entrar | Coletores 3 a 12 |
| `mcp.exa.ai`, `search.parallel.ai`, `r.jina.ai`, `mcp.firecrawl.dev` | Não | Adicionar se a pesquisa rodar na nuvem | MCPs de busca e extração; estavam inacessíveis na Fase 2 [V] |

O host exato do CSV do consumidor.gov.br não foi confirmado. Uma nota sobre o `mcp-brasil`: ele instala nesta nuvem, porque `pypi.org` está liberado, mas todas as chamadas que ele faz a domínios gov.br falham até a lista mudar [V, teste desta sessão].

## Conclusão

O recurso escasso deste radar não é dinheiro nem dado. É **acesso legítimo com procedência**. O dado brasileiro de melhor qualidade é público e gratuito, e o dado privado de dor está atrás de Cloudflare, aprovação manual ou bloqueio nominal a bots de IA. Isso inverte uma intuição comum. As lentes "de governo", que pareciam contexto, viram as fontes de sinal mais fortes: compra pública com valor, reclamação oficial contada por empresa, ocupação contada por CBO. Já as lentes "de comunidade", que pareciam o coração da descoberta, ficam como geradoras de hipótese. O problema de diagnosticidade da lente 11 se resolve escolhendo fontes cuja estrutura já exige cifra ou recorrência, e não com prompts mais cuidadosos.

A segunda implicação é que a camada de busca e a camada de evidência precisam ser ferramentas diferentes. A WebSearch nativa é boa para achar e ruim para provar, porque não devolve o texto que R-05 manda guardar. Os MCPs gratuitos preenchem essa lacuna a custo zero. A pergunta que resta é empírica e barata: nenhum fornecedor mede qualidade em português, então o harness deve medir, com as próprias consultas, antes de gastar o primeiro dólar. Até lá, toda afirmação deste relatório marcada [T] ou [R] é direção, não régua. O primeiro teste de uma chamada por API numa rede liberada vale mais do que qualquer linha escrita aqui.

## Adotar / Descartar / Testar

### Adotar

| # | Item | O que muda | Onde |
|---|---|---|---|
| A-1 | Regra dos quatro destinos (coletor, MCP, busca web, evitar) e registro `fontes.yaml` com licença, risco LGPD, atribuição e data da checagem de robots.txt e termos, no molde do `SOURCES.md` do `mcp-brasil` | Toda fonte nova passa pela regra antes de virar código | Arquitetura §8 (Ferramentas e scripts) e §7 (novo arquivo de estado) |
| A-2 | `mcp-brasil` como camada de consulta pontual, com commit fixado no GitHub (o PyPI parou em 0.14.0, de abril de 2026) e `MCP_BRASIL_LGPD_ALLOW_PII` vazio | Pesquisador e verificador consultam IBGE, Transparência, CKAN de agências e BCB sem coletor | §6 (Ferramentas: MCPs), §8; lentes 1, 3, 4 e 6 |
| A-3 | Coletores da Fase 3: base comum, yc-oss, PNCP (via `pncp-cli`), 99Freelas e consumidor.gov.br | Substitui a lista de candidatos da §8 na fatia vertical | §8 e §11 (Fase 3); lentes 2, 4, 6, 7, 10 e 11 |
| A-4 | PNCP e PCA como fonte principal da lente 11; consumidor.gov.br e 99Freelas como fontes de recorrência; fórum só gera hipótese | Resolve a nota de baixa diagnosticidade | §5.1, lente 11 |
| A-5 | Fontes da lente 7: yc-oss, TrustMRR, Show HN e Exa via MCP para empresas com restrições; ListaMRR para checar equivalente brasileiro; Acquire, Indie Hackers e Starter Story por leitura manual; Product Hunt só em baixo volume | Troca a coluna "Fontes candidatas" | §5.1, lente 7 |
| A-6 | Lentes 5 e 8 por Gupy (páginas de empresa), MCP da Empregare e CAGED/RAIS via SQL na Base dos Dados | Concretiza o item "vagas" da §8 | §5.1, lentes 5 e 8; §8 |
| A-7 | Pilha de busca: WebSearch nativa para descoberta; Exa e Parallel via MCP; Jina ou `curl` para trecho literal; Firecrawl sem chave para páginas com JavaScript; teto elevado com `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`; cada comando declara quantas buscas gasta | Responde A-04 sem custo e viabiliza o trecho literal de R-05 | §8 (Busca e leitura web), princípio 8 da §3, A-04 em `decisoes.md`, R-05 |
| A-8 | Higiene de coletor: User-Agent fixo e descritivo, releitura de robots.txt, nunca contornar Cloudflare, dado pessoal só agregado, testes com respostas gravadas | Vira checagem determinística | §8, §9 (nível 1), R-02, R-12 |
| A-9 | Dado bruto volumoso (CNPJ, RAIS) em cache fora do git; só agregados versionados | Mantém o estado diffável | §7 e D-005 |
| A-10 | Fontes da lente 10: coletor do 99Freelas; GetNinjas (`averagePrices`) e Workana via busca web | Troca a coluna "Fontes candidatas" | §5.1, lente 10 |

### Descartar

| # | Item | Motivo | Onde |
|---|---|---|---|
| D-1 | Reddit como coletor | Aprovação obrigatória desde novembro de 2025; US$0,24 por mil chamadas em uso comercial [R]. Fica na busca web | §8 (lista de coletores); lente 11 |
| D-2 | Google Trends como coletor | Não há API geral; pytrends arquivado [R/V]. Uso manual da interface e pedido de acesso ao alfa | §8; lentes 7 e 11 |
| D-3 | Perguntas do Mercado Livre como fonte | Busca e itens de terceiros dão 403 para apps externos [T] | §5.1, lente 11 |
| D-4 | LinkedIn e Vagas.com.br | robots.txt bloqueia bots de IA pelo nome [T] | Lentes 5 e 8 |
| D-5 | Raspagem de Upwork, Fiverr e Freelancer.com.br | Cloudflare e robots.txt [T] | §5.1, lente 10 |
| D-6 | Reclame Aqui em massa | Sem API, Cloudflare, termos não lidos, histórias pessoais sob LGPD [T]. Só checagem `site:` | Lentes 2 e 11 |
| D-7 | Mineração de avaliações do Google Places | No máximo 5 avaliações por local; cerca de US$25 por mil depois da faixa gratuita [T] | Lentes 2 e 3 |
| D-8 | Exploding Topics, Google Programmable Search, Bing Search API, SerpApi como padrão | Custo (US$249+/mês), encerramento em 1/1/2027, descontinuação em 2025, preço por resposta útil [R/C] | §8 (Busca) |
| D-9 | Microdados de saúde (DataSUS) e DataJud em massa | LGPD art. 11 §4; resoluções do CNJ [V] | §8; lentes 1 e 6 |
| D-10 | Raspagem da página de busca do DOU | O INLABS entrega o XML oficial [V] | Lente 4 |
| D-11 | Brave como fonte de trechos guardados | A cláusula de armazenamento exige plano específico [C] | §8, R-05 |
| D-12 | `www.reddit.com` e `api.mercadolibre.com` na lista mínima de domínios | Liberar não adianta: o bloqueio é da plataforma | R-02 |

### Testar

| # | Item | Critério de sucesso escrito antes | Onde |
|---|---|---|---|
| T-1 | Sonda em português: 30 a 50 consultas reais do harness na WebSearch nativa, no Exa, no Parallel e no Brave com `country=BR` | Um provedor vence a nativa em fontes brasileiras relevantes por consulta com margem acima do ruído; só então há gasto | A-04, §8, §9 (evals) |
| T-2 | Uma chamada por API numa rede liberada (PNCP, Querido Diário, IBGE, HN, consumidor.gov.br, login do INLABS) antes de escrever cada coletor | Endpoint, limites e formato batem com as notas | R-02, §8 |
| T-3 | Google Play pt-BR: leitura dos termos da loja e volume útil por app de ERP | Termos não vedam e mais de 200 avaliações úteis por app | Lentes 2, 9 e 11 |
| T-4 | Checagem manual de dez minutos em cada loja de apps (Nuvemshop, VTEX, RD Station, Bling, Tiny, Omie, Conta Azul): avaliações, categorias, robots.txt, termos | Pelo menos duas lojas com avaliações públicas coletáveis | §5.1, lente 9 |
| T-5 | Contagens de CNPJ via SQL na Base dos Dados contra o dump local | O SQL cabe na cota grátis e bate com o dump | Lentes 1 e 3; §7 |
| T-6 | Cobertura real do Querido Diário (cidades nível 3) antes do coletor | Lista de cidades dá cobertura útil para as teses em curso | Lente 4 |
| T-7 | Ro-DOU como alternativa a construir o coletor DOU/Querido Diário | Alertas por palavra-chave sem código próprio | Lente 4, §8 |
| T-8 | TrustMRR: termos da API e cobertura atual (840+ ou 470+) | Termos permitem coleta diária do catálogo | Lente 7 |
| T-9 | Cota "granular" do YouTube de junho de 2026 (fonte única) | Coletor por canais semeados cabe na cota | Lente 11 |
| T-10 | Catho (sitemap) e Indeed depois da leitura dos termos | Termos não vedam coleta automatizada | Lente 5 |
| T-11 | Pedido de acesso não comercial ao Reddit | Aprovação em até 4 semanas; senão, fica a busca web | Lente 11 |

# Para revisar

> Decisões e descobertas registradas enquanto você dormia (a partir de 2026-09-24).
> Ordem: urgência primeiro, depois impacto. Cada item diz o que eu decidi por padrão,
> por quê, e o que muda se você discordar. Responda só nos que quiser mudar.

## Por onde começar (15 minutos)

1. **R-01**: tem prazo (30/09) e não é do harness, é da sua empresa, se houver.
2. **R-02**: rede do ambiente. Sem ela os coletores e a verificação de fontes não
   rodam na nuvem.
3. **R-11** e **R-19**: o juiz virou subagente isolado, e o trio advogado + cético +
   juiz ficou provisório até um eval compará-lo.
4. **R-03**, **R-04**, **R-17** e **R-18**: réguas das trilhas M e S. São as que mais
   mudam o que o harness aprova ou mata.
5. **R-14**: ligar ou não MCPs de busca e de dados do governo.
6. **A-02** e **A-07** em `decisoes.md`: suas horas e caixa para testes, e suas teses
   antigas para servir de casos de eval.

O restante confirma ou refina o desenho que você já aprovou.

## ⏰ Com prazo

### R-01 · Janela do Simples Nacional / IBS-CBS termina em 30/09/2026
**Descoberta (confiança baixa, fonte secundária):** a Resolução CGSN 186/2026 teria
aberto de 1 a 30/09/2026 a opção, para 2027, de recolher IBS/CBS pelo regime regular
em vez de dentro do DAS. Só importa se você tem ou vai abrir empresa para operar as
trilhas M ou S.
**Meu padrão:** nada, porque não é decisão do harness.
**Ação sugerida:** se tiver empresa no Simples, confirmar com seu contador antes do
fim do mês.

## Alto impacto

### R-02 · O ambiente em nuvem não alcança as fontes de dados
**Descoberta:** a política de rede desta sessão bloqueia quase todas as fontes que o
harness precisa: arxiv, gov.br, IBGE, Querido Diário, Receita (CNPJ), Reddit, HN
Algolia, Reclame Aqui, Mercado Livre, sites de preço de vendors. Também existe um
limite de 200 buscas web por sessão, e os 13 pesquisadores esgotaram esse limite.
**Consequências:**
1. Os números da Fase 2 vieram de resumos de busca, não da leitura das fontes. Servem
   como ponto de partida e direção, não como régua dura. Os relatórios marcam isso.
2. Os coletores da Fase 3 não podem ser testados ao vivo aqui.

**Meu padrão:** construir os coletores com testes offline (respostas gravadas) e
deixá-los prontos para rodar onde a rede permitir.
**Decisão sua:** (a) liberar os domínios no ambiente de nuvem (lista abaixo); ou (b)
rodar a coleta no Claude Code da sua máquina e usar a nuvem só para desenvolvimento e
evals.
Domínios para (a), revisados pelo relatório de fontes, que recomenda (a) para as APIs
oficiais porque as rotinas agendadas rodam com lista de permissão:
- **coletores da Fase 3:** `pncp.gov.br`, `www.99freelas.com.br`, `consumidor.gov.br`
  (o yc-oss já funciona via `raw.githubusercontent.com`);
- **consultas pontuais e Fase 4:** `servicodados.ibge.gov.br`,
  `api.queridodiario.ok.org.br`, `arquivos.receitafederal.gov.br`,
  `hacker-news.firebaseio.com`, `hn.algolia.com`, `inlabs.in.gov.br`;
- **busca e extração via MCP (se aprovar R-14):** `mcp.exa.ai`, `search.parallel.ai`,
  `r.jina.ai`;
- **pesquisa:** `arxiv.org`, `export.arxiv.org`.

Liberar Reddit e Mercado Livre não adianta: o bloqueio é da própria plataforma (R-15).

### R-03 · O que o piso da trilha M significa
**Descoberta:** as taxas-base são duras. Dos produtos que já faturam, só ~15–25%
chegam a ~US$6k (≈R$30k) de MRR algum dia, e bem menos em 18 meses. A cauda
brasileira é mais fina: média de ~R$2,1k de MRR nos 246 produtos do ListaMRR, e 76%
dos respondentes de uma comunidade brasileira de micro-SaaS faturam menos de R$5k/mês.
Esses dados vêm de resumos de busca e têm viés de autosseleção.
**Meu padrão:** o piso continua em R$30k MRR, mas como **teto da oportunidade** (o
mercado e o canal permitem chegar lá?), não como previsão de que você vai chegar. A
probabilidade de chegar é estimada à parte, contra a taxa-base.
**Se discordar:** podemos baixar o piso ou esticar o horizonte para 36 meses.

### R-04 · Ticket mínimo na trilha M
**Descoberta (dados de faturamento da ChartMogul, via resumo):** com ARPA abaixo de
US$10/mês o churn fica em 6–7% ao mês. Produtos de IA abaixo de US$50/mês retêm 23%
da receita em 12 meses; acima de US$250/mês, 70%.
**Meu padrão (corrigido pelo relatório D):** o pacote M marca ticket abaixo de
~R$150/mês como risco alto de churn. Para produto centrado em IA, pede dependência real
do fluxo de trabalho do cliente **e** ticket alto. R$250/mês só tira o produto da pior
faixa de retenção (de 23% para 45% da receita retida em 12 meses); retenção típica de
B2B só aparece perto de ~R$1.250/mês. Na prática isso empurra a trilha M para B2B.
**Se discordar:** diga se quer manter aberto um espaço para B2C barato.

### R-05 · Checar citações custa mais do que o previsto
**Descoberta:** em agentes de pesquisa, só 39–77% das afirmações citadas são de fato
sustentadas pela fonte. Um juiz sem acesso à fonte pega só 16–17% das citações ruins.
Por isso conferir só 2–3 citações não basta.
**Meu padrão:**
- todo fato novo guarda o **trecho literal** da fonte (campo novo no schema de fatos);
- um script checa se o link abre;
- um subagente verificador lê a fonte e confere os fatos que sustentam decisão.

**Custo:** mais tokens por dossiê.

### R-06 · Calibração: Brier mensal é ruído
**Descoberta:** com ~30 previsões resolvidas, o erro padrão do Brier é ~0,033; é
preciso algo como 100 ou mais para medir habilidade. Os modelos atuais são
**superconfiantes** em previsões.
**Meu padrão:**
- o Brier passa a ser acumulado, com intervalo de confiança e comparação contra a
  taxa-base;
- as réguas só são ajustadas por calibração depois de ~100 previsões resolvidas;
- o veredito pede P(sucesso) e P(fracasso) em chamadas separadas. A direção do viés
  é desconhecida: um estudo de 2026 achou os modelos da Anthropic **pessimistas**, ao
  contrário dos demais;
- a probabilidade parte da taxa-base, gravada como campo, com ajustes nomeados. A
  probabilidade do juiz é puxada em direção à taxa-base, e não se "extremiza" a média
  de amostras.

**Mudança no seu método (inferência do relatório):** tirar "o ônus da prova é do GO"
da Fase 0.4, porque a taxa-base já carrega o ceticismo e a frase o conta duas vezes.

Isso muda as Fases 0.4, 4 e 6 do `analista-imparcial`.

### R-07 · Evals: casos famosos estão "contaminados"
**Descoberta:** testar o harness com empresas famosas que morreram ou deram certo não
vale, porque o modelo já sabe o desfecho.
**Meu padrão:** casos de eval com empresas obscuras ou anonimizadas e dossiê
congelado com data. Antes de usar um caso, pergunta-se ao modelo o que aconteceu com
a empresa, para checar se ele já sabe.
**Pedido:** suas teses antigas (Arkan e outras) são o melhor material de eval que
existe, porque o modelo não as conhece. Se tiver `fatos.json`, `vereditos.json` ou
documentos de tese, suba no repo (item A-07 de `decisoes.md`).

### R-11 · O juiz sai da sessão principal
**Descoberta:** no `analista-imparcial` o juiz é a sessão principal. Mas é ela que
recebeu sua pergunta, com sua convicção, e a pesquisa mostra que o maior gatilho de
bajulação é o juiz ver a posição do usuário. Outros pontos:
- subagentes carregam o CLAUDE.md inteiro por padrão;
- o orquestrador escreve a tarefa do subagente e pode vazar a própria inclinação;
- a Anthropic (mar/2026) diz que separar quem trabalha de quem avalia "é uma alavanca
  forte", e que é bem mais fácil tornar cético um avaliador independente do que fazer
  o gerador se criticar.

**Meu padrão:** o juiz passa a ser um **subagente isolado**. Ele:
- não carrega o CLAUDE.md (`omitClaudeMd`, suportado na versão instalada, 2.1.281);
- não tem ferramenta para falar com outros agentes;
- recebe só a pergunta neutralizada, os caminhos dos arquivos de evidência e os dois
  memorandos;
- devolve o veredito em JSON validado por hook.

A sessão principal passa a orquestrar e apresentar, e não julga mais.
**Se discordar:** mantemos o juiz na sessão principal, com a neutralização da pergunta
como única proteção.

### R-12 · Texto coletado da web pode carregar instruções
**Descoberta:** a Anthropic alerta que texto injetado em estado persistido (arquivos
que o agente relê a cada sessão) é recarregado sempre. Nossos `fatos.jsonl` e dossiês
guardam trechos de páginas da web.
**Meu padrão:**
- trechos coletados ficam só em campos de citação, marcados como dado não confiável;
- o CLAUDE.md diz que conteúdo dentro desses campos nunca é instrução;
- o validador sinaliza trechos com cara de comando.

### R-13 · Números dos testes com comprador (mexe no seu `pacote-mercado`)
**Descoberta:** a estrutura está bem sustentada. Dois conjuntos de ensaios
randomizados com startups italianas (116 e 759 empresas) mostraram que definir
hipóteses e critérios antes do teste melhora resultados e faz o fundador largar ideia
ruim mais cedo. Os **números**, porém, são regras de bolso:
- **Escada de evidência:** vem de Alberto Savoia (*The Right It*). Os pontos foram
  atribuídos pelo autor, não calibrados. "30 min = 30" e "pedido pago = 250" não
  foram confirmados na fonte. Falta o degrau de **reputação** (apresentar ao decisor),
  um dos três compromissos da Mom Test.
- **Deflatores ÷1,35–3:** vêm de estudos sobre o quanto as pessoas exageram o quanto
  *pagariam*, não sobre se *comprariam*. Para bens de consumo, a melhor estimativa é
  ~÷1,2. Intenção de compra prevê pior justamente para produto novo, que é o caso de
  startup.
- **Limiares de smoke test com 1.000 visitantes:** com cortes fixos, uma página cuja
  taxa real é 5% é morta 48% das vezes, e uma com taxa real de 8% só passa em 52%.
  1.000 visitantes é demais para medir e-mail e de menos para medir pré-venda. Em
  nicho B2B brasileiro, muitas vezes é inalcançável.

**Meu padrão nos pacotes novos (M, S) e na revisão do G:**
- a escada mantém a ordem e ganha o degrau de reputação; os pontos deixam de ser
  somados como se fossem probabilidade;
- o deflator vale só para preço declarado (÷1,2 central, ÷3 pessimista);
- "compraria" conta só o "com certeza", dividido por 2 no mínimo, e **nunca** abre
  portão de GO;
- em B2B de nicho, regra bayesiana de amostra pequena sobre contas contatadas. Exemplo:
  GO se P(taxa de depósito > 10%) ≥ 0,8, o que dá ~3 depósitos em 20 decisores com
  orçamento;
- pré-venda com teste sequencial (0,3% contra 1%): com 1.000 visitantes, GO com 9 ou
  mais pedidos e KILL com 4 ou menos;
- todo teste registra limiar, canal, tamanho da amostra e resultado, para o harness
  construir as próprias taxas-base brasileiras (não existe benchmark BR publicado).

### R-16 · Trilha S: o óbvio (bot de WhatsApp para PME) está sendo comoditizado
**Descoberta (via resumos e notas de terceiros):**
- os termos da API do WhatsApp Business proíbem chatbots de IA de uso geral desde
  15/01/2026 (bots específicos do negócio continuam permitidos);
- a Meta lançou em fev–mar/2026 um agente de IA próprio dentro do WhatsApp Business
  para PMEs brasileiras;
- empresas de serviço com IA em escala reportam ~60–65% de margem bruta; agências
  pequenas cobram setup de US$2–8k mais mensalidade;
- no Brasil há serviço de automação de WhatsApp publicando R$397–2.497/mês, o que dá
  12–22 clientes para chegar a R$15k/mês.

**Meu padrão no pacote S:**
- trava nova: "a IA nativa da plataforma (Meta, ChatGPT) replica a oferta?";
- checagem dos termos da plataforma;
- margem bruta ≥ 60% **depois das suas horas**;
- limite de receita concentrada num único cliente;
- preço por resultado só quando um sistema externo registra o resultado;
- setup pago + mensalidade, para ter caixa em 30 dias.

Compradores melhores que "PME genérica", por inferência a validar: escritórios de
contabilidade, corretoras de seguro, faturamento de clínicas, documentação jurídica.

### R-17 · Validação mínima da trilha M muda
**Descoberta:** lista de e-mail acima de um limiar não tem vínculo demonstrado com
sucesso. Em M o MVP custa no máximo 4 semanas, então o erro caro não é construir cedo:
é escalar um resultado que foi sorte.
**Meu padrão (diverge da v1 da arquitetura e do seu `pacote-mercado`):**
- construir o MVP depois de **1 degrau com dinheiro** (pré-venda com reembolso ou
  depósito);
- replicar o resultado (novo lote de contas ou outro canal) **antes de gastar com
  escala**;
- lista sozinha nunca abre GO.

A trilha G continua exigindo 2 degraus com dinheiro antes de construir.
**Se discordar:** voltamos a exigir 2 degraus também em M.

### R-18 · Trilha S: margem depois das suas horas, e 3 contratos antes de automatizar
**Descoberta:** margem de serviço com IA se mede em horas do operador, não em tokens. A
R$1.500/mês com margem de 60% cabem até ~4 h por cliente por mês; a R$700, menos de 1 h.
Um contrato prova que existe comprador, não que o escopo se repete.
**Meu padrão:**
- a margem de S passa a ser medida depois de IA, plataforma **e** suas horas;
- 1 contrato pago libera começar a entregar, ainda à mão;
- **3 contratos do mesmo ICP** liberam investir em automação;
- capacidade de referência: 80 h/mês de entrega.

### R-19 · O trio advogado + cético + juiz é provisório
**Descoberta:** nenhuma fonte compara o trio com um único juiz cético e calibrado, com o
mesmo orçamento. A evidência a favor de debate vem de juízes que não viam a fonte.
**Meu padrão:** mantenho o trio, porque os memorandos também servem de lista de
verificação para o verificador. Mas o próximo eval de capacidade compara três variantes
nos mesmos casos, com orçamento igual: trio; juiz sozinho com o dossiê; juiz com um só
memorando contra. O trio só fica se ganhar em acerto ou em consistência entre
execuções.

### R-20 · Como os comandos são orquestrados
**Descoberta:** o relatório A recomenda que cada comando seja um roteiro em código
(script Python chamando `claude -p` por etapa), com o CLAUDE.md só roteando.
**Meu padrão, por ora:**
- os comandos são skills que a sessão principal segue, lançando subagentes;
- tudo que é determinístico já é código: validar, ids, contrato, entrada cega do juiz,
  registrar veredito com encolhimento, conferir trecho, regra de teste;
- o juiz dos evals já roda via `claude -p` num diretório neutro.

Motivo: é mais simples de usar e de mudar enquanto o método ainda muda toda semana.
**Teste pendente:** comparar as duas formas em isolamento, custo, retomada e testes
offline. Se a forma em código ganhar, migramos comando por comando.

### R-21 · Estágio e status continuam no frontmatter do cartão
**Descoberta:** o relatório A sugere tirar status do frontmatter e usar um log
append-only `data/eventos.jsonl`.
**Meu padrão:** mantive estágio e status no frontmatter, mas:
- só a CLI edita (hook bloqueia edição direta);
- o schema valida cada mudança;
- cada mudança é anotada com data no histórico do cartão.

O ganho que falta em relação ao log é a consulta agregada ("quanto tempo cada
oportunidade ficou em cada estágio"). Se isso fizer falta no `/portfolio`, adicionamos o
log.

### R-22 · Quanto custa operar
**Medido:**
- juiz (Opus, esforço alto): ~US$0,33–0,70 por execução;
- chamada headless trivial: ~US$0,05.

**Estimado, a medir na primeira execução real:**
- `/kill`: ~US$1–3;
- `/validar` (dossiê, memorandos, verificador e juiz): ~US$5–15;
- `/radar` com 4 batedores: ~US$3–8;
- eval de bajulação completo (1 caso × 3 braços × 3 repetições): ~US$4–6.

Nada disso usa API paga de terceiros.

## Médio impacto

### R-14 · Busca: ficar só na nativa ou adicionar MCPs de busca e de dados BR?
**Descoberta:**
- A busca nativa do Claude Code devolve só título e URL, não tem configuração de país
  ou idioma e tem limite de 200 buscas por sessão, compartilhado com os subagentes.
- A leitura nativa de páginas é "com perdas por desenho": um modelo pequeno resume a
  página.
- APIs especializadas custam ~US$1–7 por 1.000 buscas. Parallel, Exa, Firecrawl e Jina
  têm servidor MCP oficial utilizável sem chave.
- No benchmark independente mais próximo do nosso caso de arbitragem (achar empresas
  que casam várias restrições, inclusive país), Parallel e Exa fazem ~46 de F1, contra
  ~30 da Brave. O resultado só foi visto via texto de um vendor.
- `mcp-brasil` (código aberto, 1.786 estrelas, atualizado 23/09/2026) cobre ~70 fontes
  do governo num servidor MCP só (Querido Diário, DOU, PNCP, Transparência, IBGE, BCB,
  ANVISA), com um arquivo de risco de licença e LGPD por fonte.

**Meu padrão:** não instalo nada sem você. Instalar um MCP de busca manda suas
consultas para um terceiro, e instalar o `mcp-brasil` roda código de terceiros.
Deixo a configuração pronta e desligada no repo.
**Decisão sua:** (a) ligar um MCP de busca sem chave (Parallel ou Exa) para o radar e
a arbitragem; (b) ligar o `mcp-brasil` fixado num commit específico; (c) nenhum dos
dois por enquanto.

### R-15 · Fontes a evitar
**Descoberta:**
- Mercado Livre bloqueia apps externos na busca (403).
- LinkedIn e Vagas.com.br bloqueiam crawlers de IA no robots.txt.
- Reclame Aqui não tem API e fica atrás de Cloudflare.
- Google Places custa ~US$25 por 1.000 chamadas e devolve no máximo 5 reviews por
  lugar.
- Reddit exige aprovação para qualquer cliente de API desde o fim de 2025.

**Meu padrão:** essas fontes entram só via busca web, sem coletor automático.
Substitutos legais:
- `consumidor.gov.br` (reclamações abertas) no lugar do Reclame Aqui;
- 99Freelas no lugar de Workana e GetNinjas;
- PNCP (compras públicas com preço vencedor) como fonte prioritária de "demanda com
  dinheiro".

### R-08 · Tom das suas skills existentes
**Descoberta:** nos modelos atuais, ênfase agressiva ("SEMPRE", "NÃO", "CRÍTICO") faz
a instrução ser aplicada em excesso. A orientação da Anthropic hoje é linguagem calma
e condicional, com o motivo de cada regra. `pesquisador-de-mercado` e
`analista-imparcial` usam bastante caixa alta.
**Meu padrão:** as versões no repo trocam a caixa alta por regra + motivo, sem mudar
o conteúdo. As originais no claude.ai continuam intactas.

### R-09 · Ajustes no protocolo do juiz
**Descoberta:**
- Enquadrar a tese como "de um terceiro" reduziu bajulação em até 63,8%, mais do que
  instruções do tipo "não seja bajulador".
- Modelos aceitam mais um contra-argumento que chega depois do que um mostrado lado a
  lado com o argumento original.
- Pedir "ache problemas" gera objeções inventadas.
- Debate ajuda quando o juiz trata as críticas como alegações a verificar, e uma
  rodada sem réplica dá quase todo o ganho (Elasky et al., 2026, com Opus 4.6 e Gemini
  3.1).

**Meu padrão:**
- o juiz recebe os dois memorandos **no mesmo turno**, com rótulos neutros A e B em
  ordem sorteada (a direção de cada um é declarada) e tamanho igualado;
- toda objeção ou mérito precisa de evidência e gravidade;
- antes de pontuar, o juiz marca cada alegação como verificada, não verificada ou
  contradita.

### R-10 · Só Claude julgando Claude
**Descoberta:** juízes favorecem textos do próprio modelo e da própria família. Um
painel de três modelos de fornecedores diferentes superou um juiz único a custo 7×
menor.
**Meu padrão:** fica só Claude, porque não temos chaves de outros fornecedores e o
viés é simétrico (advogado e cético são ambos Claude).
**Opção futura:** um segundo juiz de outro fornecedor nos vereditos da trilha G.

## Confirmações (a pesquisa sustentou o desenho; nada muda)

- **Sem personas de traço:** personas de especialista não melhoram acurácia
  (162 personas testadas; vários estudos de 2024 a 2026), e personas irrelevantes
  derrubam até ~30 pontos. Seguimos com papéis definidos por procedimento.
- **Português:** o português do Brasil rende ~97,8% do inglês em MMLU traduzido
  (Sonnet 4.5). Prompts em português, com o idioma de saída declarado.
- **Prompts atuais:** não pedir "pense passo a passo" (o raciocínio já é controlado
  pelo nível de esforço); CLAUDE.md com menos de 200 linhas; documentos longos
  primeiro e a pergunta no fim.

- **Advogado + cético isolados + juiz, com ressalva:** o ganho de debate (juízes de 48%
  para 76%, Khan et al., 2024) foi medido com juízes que **não viam a fonte**. O nosso
  juiz lê o dossiê, e nessa condição Kenton et al. (2024) não acharam vantagem do
  debate. Debate em várias rodadas também não supera votação simples.
  **Padrão:** mantenho uma rodada só, sem réplica, e o primeiro eval compara "juiz
  sozinho com o dossiê" contra "juiz com dossiê e memorandos". Se os memorandos não
  ajudarem, saem do pipeline e o custo cai.
- **Escrita centralizada:** a Cognition revisou a posição dela em 2026 para "escritas
  num fio só; agentes extras contribuem inteligência, não ações". Ajuste do relatório
  A: o escritor único é a CLI (`python3 -m harness`), que valida e trava o arquivo. Os
  subagentes gravam fatos por ela, e nenhum edita o estado diretamente (um hook
  bloqueia).
- **Multiagente só onde a tarefa é paralelizável:** +81% em tarefas paralelizáveis e
  −39% a −70% em sequenciais (Google, preprint de dez/2025). Radar e coleta ficam em
  paralelo; validação fica sequencial num fio só.

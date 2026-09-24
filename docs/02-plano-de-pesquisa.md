# Plano da Fase 2: Pesquisa

> Objetivo: confirmar, ajustar ou derrubar as hipóteses **[H]** da
> [arquitetura](01-arquitetura.md) com as melhores fontes disponíveis, antes de escrever
> o harness. Cada relatório termina em **adotar / descartar / testar**, e cada
> recomendação aponta para a decisão que ela muda.

## Regras da pesquisa

- **Fontes primárias primeiro:** papers, documentação oficial, posts de engenharia de
  quem construiu sistemas em produção. Opinião de praticante só com evidência (dados,
  casos, código).
- **Mesma régua de evidência do harness:** o que não tiver fonte fica marcado como
  inferência.
- **Com prazo:** um fluxo por sessão. Pesquisa que não muda nenhuma decisão é cortada.
- Execução com a skill `deep-research` (pesquisadores em paralelo + redator), relatórios
  em `research/`.

## Fluxo A: Engenharia de agentes e harness

**Perguntas**
- Quando workflow fixo supera agente autônomo, e vice-versa?
- Quando multiagente ajuda e quando atrapalha? Como dividir trabalho sem perder contexto?
- Engenharia de contexto: compactação, notas estruturadas, recuperação sob demanda.
- Recursos do Claude Code para o nosso caso: CLAUDE.md, subagentes, skills, hooks,
  comandos, rotinas agendadas, escolha de modelo por subagente.
- Como desenhar ferramentas que o agente usa bem; como escalar esforço por tarefa.

**Fontes de partida**
- Anthropic: *Building effective agents*; *How we built our multi-agent research
  system*; *Effective context engineering for AI agents*; *Writing effective tools for
  agents*; documentação de Agent Skills e do Claude Code (subagentes, skills, hooks).
- Cognition: *Don't Build Multi-Agents*.
- HumanLayer: *12-Factor Agents*.
- Manus: *Context Engineering for AI Agents: Lessons from Building Manus*.
- OpenAI: *A practical guide to building agents*.

**Decide:** princípios 4, 5 e 8; lista de subagentes; estrutura de pastas; orçamento
por comando.

## Fluxo B: Prompts e julgamento com LLMs

**Perguntas**
- Boas práticas de prompt para os modelos Claude atuais (estrutura, exemplos,
  raciocínio, saídas estruturadas).
- Bajulação: o que comprovadamente reduz?
- LLM como juiz: vieses conhecidos (posição, verbosidade, autopreferência) e mitigação.
- Debate e desenhos adversariais: quando melhoram a acurácia do juiz?
- Personas no prompt: ajudam ou atrapalham a acurácia?
- Previsão e calibração com LLMs: o que funciona para probabilidades confiáveis?
- Fidelidade de citação: como reduzir fonte inventada ou mal lida?

**Fontes de partida**
- Documentação de prompt engineering da Anthropic.
- Sharma et al. (2023), *Towards Understanding Sycophancy in Language Models*.
- Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Khan et al. (2024), *Debating with More Persuasive LLMs Leads to More Truthful Answers*.
- Zheng et al. (2023), *Is "A Helpful Assistant" the Best Role for Large Language Models?*
- Halawi et al. (2024), *Approaching Human-Level Forecasting with Language Models*.
- Tetlock & Gardner, *Superforecasting*; ICD 203 (padrões analíticos).

**Decide:** revisão do `analista-imparcial`; prompts de advogado, cético e juiz;
formato dos vereditos; prompts dos batedores.

## Fluxo C: Evals

**Perguntas**
- Como montar o primeiro conjunto de evals (tamanho, fonte dos casos, análise de erros)?
- Como validar um LLM-juiz contra julgamento humano?
- Como fazer regressão de skills e prompts a cada mudança, lidando com variância?

**Fontes de partida**
- Hamel Husain: *Your AI Product Needs Evals*; *Creating a LLM-as-a-Judge That Drives
  Business Results*.
- Shankar et al. (2024), *Who Validates the Validators?*
- Seção de avaliação do post de pesquisa multiagente da Anthropic; ferramentas de eval
  da skill `skill-creator`.

**Decide:** seção 9 da arquitetura; primeiros casos de eval; rubricas.

## Fluxo D: Métodos de descoberta e validação de negócios

**Perguntas**
- Como fundadores de micro-SaaS e serviços lucrativos de fato encontraram suas ideias?
  (dados, não anedotas)
- Playbooks de serviço → software: quando e como produtizar.
- Precificação e canal para micro-SaaS e serviços B2B no Brasil.
- Que limiares de validação (conversão, pré-venda) têm base empírica?
- O que muda no Brasil: meios de pagamento, tributação, canais, WhatsApp, ciclo de venda.

**Fontes de partida**
- Fitzpatrick, *The Mom Test*; Blank, *The Four Steps to the Epiphany*; Strategyzer
  (Test Cards); Jobs to Be Done (Christensen, Moesta).
- Rob Walling (*Stair Step Approach*) e relatórios *State of Independent SaaS* da
  MicroConf.
- Bases de casos com receita (Indie Hackers, Starter Story, Acquire.com).
- Helmer, *7 Powers*; tese *service-as-software* (Foundation Capital); Requests for
  Startups da YC.
- Brasil: mapeamentos da Distrito, Liga Ventures, ABStartups; dados do Sebrae.

**Decide:** `pacote-micro-saas.md`, `pacote-servico-ia.md`, lentes 7–11, pisos das
trilhas M e S.

## Fluxo E: Fontes de dados e ferramentas

**Perguntas**
- Quais fontes das lentes têm API ou exportação, a que custo e com que termos de uso?
- APIs de busca especializadas (via MCP) entregam fontes melhores que a busca nativa? A
  diferença paga o custo?
- Quais coletores valem ser scripts (dado estruturado e recorrente) e quais ficam na
  busca web?

**Candidatas a verificar**
- Brasil: Querido Diário, IBGE SIDRA, Reclame Aqui, Gupy e outras plataformas de vagas,
  lojas de apps de Nuvemshop/Bling/Omie/Conta Azul, Workana, 99Freelas.
- Global: HN Algolia, Reddit, Product Hunt, Acquire.com, avaliações de Google Play e App
  Store, Google Trends.
- Busca: busca nativa × APIs de busca via MCP.

**Decide:** seção 8 da arquitetura; quais coletores entram na Fase 3.

## Entregáveis

```
research/
  A-engenharia-de-agentes.md
  B-prompts-e-julgamento.md
  C-evals.md
  D-descoberta-e-validacao.md
  E-fontes-e-ferramentas.md
docs/decisoes.md    atualizado com o que cada relatório mudou
```

Ordem sugerida: **A e B primeiro** (definem como o harness é escrito), depois **D**
(define as réguas das trilhas), **E** e **C**.

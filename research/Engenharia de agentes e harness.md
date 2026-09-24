# Trave o fluxo em código e isole quem julga

O harness de oportunidades deve ser um **workflow fixo, orquestrado por código, com a autonomia do modelo restrita à coleta** (radar e buscas dentro de cada estágio). Subagentes entram só quando o isolamento é o próprio objetivo: leitura em amplitude paralela, amostras independentes, revisão em contexto limpo e apresentação adversarial a um juiz. A pesquisa confirma os princípios 4, 5 e 8 da arquitetura e corrige três pontos de engenharia. O primeiro: o fluxo não pode morar na prosa do CLAUDE.md, que a documentação do Claude Code descreve como mensagem de usuário "sem garantia de cumprimento estrito". O que precisa acontecer sempre vira script, workflow ou hook com código de saída 2, a única camada que bloqueia de forma determinística. O segundo: o isolamento padrão é mais fraco do que parece. Todo subagente carrega a hierarquia inteira de CLAUDE.md e um retrato do git status, forks herdam a conversa toda e a mensagem de delegação é escrita pelo orquestrador. Por isso a regra passa a ser **isolar quem avalia, não quem executa**, o que tira estrategista de oferta e construtor da lista de subagentes e endurece o juiz proposto em R-11. O terceiro: o orçamento é, ao mesmo tempo, a maior alavanca de qualidade e de custo. No sistema de pesquisa da Anthropic, o uso de tokens sozinho explicou **80% da variância de desempenho** e o multiagente gastou **cerca de 15× os tokens de um chat**, então o fan-out completo só se paga para teses que sobreviveram ao kill barato. O estado também muda. O status sai do frontmatter Markdown e vai para JSON, num log de eventos append-only com um único escritor, que é um script validador. Subagentes devolvem caminho de arquivo e resumo de até ~2 mil tokens, nunca paráfrase. A lacuna central é que nenhuma fonte compara advogado + cético + juiz com um único avaliador cético e calibrado em julgamento de negócio, e essa deve ser a primeira ablação da fatia vertical.

> **Marcas de evidência.** Cada citação traz uma marca de proveniência.
>
> - **lido**: fonte buscada e lida na íntegra em 24/09/2026. Inclui todos os posts de engenharia e blog da Anthropic, a documentação oficial do Claude Code e da plataforma, as páginas do *12-Factor Agents* e a documentação do *OpenAI Agents SDK* no GitHub.
> - **lido (fluxo E)**: documentação oficial lida na íntegra pelo pesquisador do fluxo de fontes e ferramentas.
> - **resumo**: apoiado só em trechos de resultados de busca, porque o proxy de rede bloqueou a fonte primária. Vale para Cognition, Manus, openai.com, Google, arXiv, LangChain, Chroma, ACL e PMLR.
> - *(inferência)*: conclusão nossa, sem fonte direta.
>
> Números marcados como "resumo" orientam direção e não viram régua dura (coerente com R-02). A versão do Claude Code instalada foi conferida nesta sessão: **2.1.281**. Ela suporta todos os recursos citados; o mais exigente, `omitClaudeMd`, pede 2.1.271 ou superior.

## O funil é um workflow; a autonomia fica dentro da coleta

A Anthropic separa **workflows**, em que LLMs e ferramentas seguem "caminhos de código predefinidos", de **agentes**, em que o modelo "dirige dinamicamente os próprios processos e o uso de ferramentas". A recomendação é buscar a solução mais simples possível e adicionar complexidade "só quando ela comprovadamente melhora o resultado" ([Building effective agents](https://www.anthropic.com/research/building-effective-agents) · lido). O post hoje traz um aviso de que o panorama de ferramentas mudou desde dezembro de 2024, mas seus princípios continuam citados nos textos de 2026 da própria Anthropic.

Outros fornecedores chegam ao mesmo lugar por caminhos independentes:

- A documentação do OpenAI Agents SDK diz que orquestrar por código torna as tarefas "mais determinísticas e previsíveis em velocidade, custo e desempenho" ([OpenAI Agents SDK](https://github.com/openai/openai-agents-python/blob/main/docs/multi_agent.md) · lido).
- O *12-Factor Agents* descreve os agentes que chegam à produção como "código majoritariamente determinístico, com passos de LLM salpicados nos pontos certos" ([12-Factor Agents](https://github.com/humanlayer/12-factor-agents) · lido).
- O guia de padrões do Google ADK chama o pipeline sequencial de "linear, determinístico e refrescantemente fácil de depurar" ([Google Developers Blog](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/) · resumo).

O levantamento *Measuring Agents in Production* (ICLR 2026) mostra que é essa a forma do que funciona: **68% dos agentes em produção executam no máximo 10 passos antes de uma intervenção humana**, 47% no máximo 5, e a maioria usa workflows estruturados com a autonomia confinada a nós específicos ([arXiv 2512.04123](https://arxiv.org/abs/2512.04123) · resumo).

O argumento a favor de autonomia é real, mas vale para um tipo específico de tarefa. O padrão orquestrador-trabalhadores existe para "tarefas complexas em que não dá para prever as subtarefas", e o exemplo que a própria Anthropic dá é uma busca que reúne informação de várias fontes ([Building effective agents](https://www.anthropic.com/research/building-effective-agents) · lido). No sistema de pesquisa da Anthropic, um líder Opus 4 com subagentes Sonnet 4 superou o Opus 4 sozinho em **90,2%**. A vantagem se concentrou em consultas de amplitude, que seguem várias direções independentes ao mesmo tempo ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).

No sentido oposto, o estudo do Google Research, DeepMind e MIT sobre escala de sistemas de agentes mediu **+80,9% em tarefas paralelizáveis com coordenação centralizada, e perdas de 39% a 70% em raciocínio sequencial para todas as variantes multiagente** ([arXiv 2512.08296](https://arxiv.org/abs/2512.08296) · resumo). O funil tem as duas formas: radar e coleta são amplitude, enquanto kill barato, veredito e oferta são raciocínio encadeado. A "cascata de requisições" (uma passada barata que só escala quando não basta) rendeu **+1,1% a 12% de acurácia com até 20% menos custo** ([arXiv 2505.18286](https://arxiv.org/abs/2505.18286) · resumo). É exatamente a lógica kill barato → veredito completo. O mapa abaixo *(inferência)* associa um padrão a cada estágio:

| Estágio | Padrão | Onde vive a orquestração | Autonomia do modelo |
|---|---|---|---|
| 0 · Radar | Orquestrador-trabalhadores (seccionamento) | Workflow ou script dispara um batedor por lente | Alta dentro do batedor (escolhe consultas e fontes), com teto |
| 1 · Oportunidade | Encadeamento + dedupe por script | Sessão principal + script | Baixa: agrupar sinais e redigir o cartão |
| 2 · Kill barato | Encadeamento com portão | Script aplica "2+ alegações caem" | Média na verificação; nenhuma no portão |
| 3 · Veredito de mesa | Amostras adversariais em paralelo + avaliador | Roteiro fixo | Baixa: papéis por procedimento, juiz com rubrica |
| 4 · Oferta | Avaliador-otimizador | Sessão principal gera; revisor isolado avalia | Média, no máximo 2 ciclos |
| 5 · Teste | Humano no circuito | Você | Nenhuma |
| 6 · Construir | Avaliador-otimizador | Sessão dedicada + revisor isolado | Alta dentro do escopo travado |
| 8 · Aprender | Script | `calibracao.py` | Baixa |

A correção de engenharia mais importante é sobre *onde* o workflow mora. A documentação de memória do Claude Code avisa que o conteúdo do CLAUDE.md "é entregue como mensagem de usuário depois do prompt de sistema" e que "não há garantia de cumprimento estrito". Para bloquear uma ação "independentemente do que o Claude decidir", a orientação é usar um hook PreToolUse ([Claude Code, memória](https://code.claude.com/docs/en/memory) · lido). Um funil descrito em prosa, portanto, é uma sugestão ao modelo, e não um funil de verdade. O Claude Code oferece três formas de pôr o fluxo em código, com trade-offs distintos:

- **Skill** com os passos escritos: flexível e barata, mas quem decide seguir os passos é o modelo.
- **Dynamic workflow**: um script JavaScript que orquestra subagentes e guarda resultados intermediários "em variáveis do script em vez de no contexto do Claude". Fica salvo em `.claude/workflows/`, roda como `/<nome>`, pode ser retomado dentro da sessão e executa até 16 agentes simultâneos por padrão. Não aceita entrada do usuário no meio da execução ([Claude Code, workflows](https://code.claude.com/docs/en/workflows) · lido).
- **Script Python que chama `claude -p` com `--json-schema`**: o mais determinístico e testável dos três, e devolve `total_cost_usd` a cada chamada ([Claude Code, headless](https://code.claude.com/docs/en/headless) · lido).

O desenho que decorre disso *(inferência)* é: o CLAUDE.md só encaminha a pergunta livre para um comando; cada comando executa um roteiro fixo, em workflow ou script; e os portões humanos ficam entre uma execução e outra. Isso combina com o princípio 9 e com um detalhe da plataforma: subagentes nunca recebem a ferramenta de perguntar ao usuário, então a decisão só pode acontecer na sessão principal ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido).

Dentro do roteiro fixo cabe um único laço avaliador-otimizador. A Anthropic indica esse padrão quando há critério claro e o refinamento traz ganho mensurável, e dá o exemplo de um avaliador que decide se novas buscas se justificam ([Building effective agents](https://www.anthropic.com/research/building-effective-agents) · lido). Para não violar o viés para teste do princípio 6, o juiz pode devolver "evidência insuficiente: falta X" como resultado legítimo; a Anthropic recomenda dar ao juiz-LLM "uma saída", como responder "Desconhecido" ([Anthropic, evals para agentes](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · lido). O roteiro permite no máximo uma rodada extra de coleta antes de chegar ao seu portão *(inferência)*.

Por fim, cada peça do roteiro é uma aposta com prazo de validade. O post de março de 2026 sobre desenho de harness afirma que "todo componente de um harness codifica uma suposição sobre o que o modelo não consegue fazer sozinho". Os exemplos: os resets de contexto viraram "peso morto" no Opus 4.5, o conceito de sprint caiu no Opus 4.6, e o avaliador separado "vale o custo quando a tarefa está além do que o modelo atual faz de forma confiável sozinho" ([Anthropic, desenho de harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) · lido; [Anthropic, Managed Agents](https://www.anthropic.com/engineering/managed-agents) · lido). O estudo do Google chega ao mesmo efeito por outro ângulo: a coordenação rende pouco, ou até piora o resultado, quando um agente sozinho já acerta mais de **~45%** da tarefa ([arXiv 2512.08296](https://arxiv.org/abs/2512.08296) · resumo). **O princípio 4 fica confirmado**, com dois acréscimos. O fluxo mora em código. E a cada troca de modelo remove-se um componente por vez, para ver se ele ainda paga o próprio custo.

## Subagente se paga com isolamento, nunca com organograma

A disputa pública entre defensores e críticos de multiagente chegou em 2026 a uma regra operacional: **paralelizar leitura, manter escrita e decisão num fio único**. As fontes convergem:

- **Cognition.** A autora de "Don't Build Multi-Agents" (2025) ajustou a posição em abril de 2026 para "sistemas multiagente funcionam melhor hoje quando as escritas ficam num fio só e os agentes adicionais contribuem inteligência, não ações". Também chamou enxames não estruturados de "principalmente uma distração" ([Cognition, 2026](https://cognition.com/blog/multi-agents-working) · resumo).
- **Anthropic.** Multiagente se encaixa mal em domínios que "exigem que todos os agentes compartilhem o mesmo contexto ou envolvem muitas dependências entre agentes" ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).
- **OpenAI.** A recomendação é esgotar a capacidade de um único agente antes de dividir, e medir sobrecarga de ferramentas por **sobreposição, não por contagem**: há implementações que lidam bem com mais de 15 ferramentas distintas e outras que se perdem com menos de 10 sobrepostas ([OpenAI, guia prático](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) · resumo).
- **Taxonomia MAST.** Com mais de 1.600 execuções anotadas em 7 frameworks, atribui **41,8% das falhas a especificação e desenho do sistema, 36,9% a desalinhamento entre agentes e 21,3% a verificação** ([arXiv 2503.13657](https://arxiv.org/abs/2503.13657) · resumo). Quase quatro em cada cinco falhas vêm de brief ruim e de coordenação, não de falta de capacidade do modelo.

Sobre o trio advogado–cético–juiz, a evidência se divide de um jeito útil. Debate *entre* agentes, em rodadas, não supera votação simples com o mesmo orçamento:

- A votação majoritária das respostas iniciais explica a maior parte do ganho atribuído ao debate ([Debate or Vote](https://arxiv.org/abs/2508.17536) · resumo).
- As variantes de debate são frágeis e sensíveis a ajuste ([Smit et al., ICML 2024](https://proceedings.mlr.press/v235/smit24a.html) · resumo).
- Um único agente com bom prompt e exemplos quase empata com a melhor discussão ([Wang et al., ACL 2024](https://aclanthology.org/2024.acl-long.331/) · resumo).

Já **argumentos opostos apresentados a um juiz** ajudam. Juízes-LLM não especialistas vão de **48% para 76%** de acurácia com debate, enquanto um consultor único mais persuasivo *piora* o juiz ([Khan et al., ICML 2024](https://arxiv.org/abs/2402.06782) · resumo; [Kenton et al., NeurIPS 2024](https://arxiv.org/abs/2407.04622) · resumo). Isso sustenta o protocolo de R-09: memorandos independentes, uma rodada só e sem réplica.

**Divergência sinalizada com `revisao-pendente.md`.** A seção "Confirmações" trata o trio como assunto encerrado, mas nenhuma fonte o compara com **um único avaliador cético e calibrado**. Essa é justamente a alternativa que a Anthropic defende, ao dizer que "ajustar um avaliador independente para ser cético é bem mais tratável do que tornar o gerador crítico do próprio trabalho" ([Anthropic, desenho de harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) · lido). Além disso, a evidência sobre debate vem de perguntas com resposta certa, não de julgamento de negócio. A confirmação deve ser lida como provisória até a ablação da fatia vertical.

Dessas fontes sai um teste que cada subagente proposto precisa passar: ele se justifica por um de cinco motivos.

1. Leitura em amplitude sobre fontes independentes.
2. Amostras independentes para agregar.
3. Revisão em contexto limpo.
4. Apresentação adversarial a um juiz.
5. Separação de domínios de ferramentas que se atrapalhariam no mesmo prompt. No benchmark da LangChain, o agente único piorou à medida que domínios distratores foram adicionados ([LangChain](https://www.langchain.com/blog/benchmarking-multi-agent-architectures) · resumo).

"Ter um especialista" não está na lista. O detalhe decisivo é uma assimetria que a Cognition deixa implícita. O princípio "compartilhe o contexto inteiro" vale para quem **executa**; o revisor em contexto limpo vale justamente porque **não** vê o raciocínio do autor. A documentação do Claude Code diz o mesmo: "um revisor rodando num subagente novo vê só o diff e os critérios que você der, não o raciocínio que produziu a mudança" ([Claude Code, boas práticas](https://code.claude.com/docs/en/best-practices) · lido). Daí a regra que reorganiza a tabela de papéis da §6.1: **isolar quem avalia, não quem executa** *(inferência sobre fontes lidas e resumos)*.

| Papel (§6.1) | Motivo legítimo de isolamento | Decisão | O que muda |
|---|---|---|---|
| Batedor | Amplitude sobre fontes independentes | Mantém | Só busca e escrita no próprio arquivo de staging; sem a ferramenta `Agent` |
| Pesquisador | Isolar a coleta da convicção do usuário; dimensões em paralelo | Mantém | Brief em template fixo preenchido por script |
| Verificador de citações | Revisão em contexto limpo | Mantém | Só julga se o trecho sustenta a alegação; a existência do trecho é checada por script |
| Advogado / Cético | Apresentação adversarial a um juiz | Mantém, sob ablação | Só leem o dossiê, sem busca web |
| Juiz | Avaliador separado do gerador | Mantém como subagente (R-11) | Perfil endurecido (subseção abaixo) |
| Estrategista de oferta | Nenhum: gera e precisa do contexto inteiro | **Vira skill** na sessão principal | Ganha um revisor isolado de oferta |
| Construtor | Nenhum: escreve código | **Sessão dedicada**, não subagente | Revisor isolado continua |
| Revisor | Revisão em contexto limpo | Mantém | Aponta só lacunas materiais |

Duas decisões da tabela pedem justificativa. Advogado e cético ficam sem busca web porque, se buscassem, coletariam evidência escolhida pelo lado que defendem. É a contaminação que o princípio 1 existe para evitar *(inferência)*. Ler só o dossiê também iguala o orçamento dos dois por construção. O cético precisa ainda da mesma trava do revisor: segundo a documentação, "um revisor instruído a achar lacunas geralmente reporta algumas, mesmo quando o trabalho está correto", e a correção é pedir só lacunas que afetam correção ou requisitos ([Claude Code, boas práticas](https://code.claude.com/docs/en/best-practices) · lido). Isso converge com a descoberta de R-09 de que pedir "ache problemas" gera objeções inventadas.

A qualidade do brief é a principal alavanca de todo subagente. A Anthropic exige que cada subagente receba "um objetivo, um formato de saída, orientação sobre ferramentas e fontes e limites claros da tarefa". Ela relata que três subagentes encarregados de "pesquisar a escassez de semicondutores" duplicaram o trabalho uns dos outros ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).

Há uma tensão com a neutralidade: a Cognition pede que o brief carregue o *porquê* ([Cognition, 2025](https://cognition.com/blog/dont-build-multi-agents) · resumo), mas o pesquisador não pode saber qual veredito o usuário deseja. A saída *(inferência)* é um **brief em template preenchido por script**. O template inclui:

- a pergunta neutralizada;
- escopo e exclusões;
- ids dos fatos já conhecidos, para não duplicar;
- o schema de saída;
- a hierarquia de fontes;
- o critério de parada.

Ficam de fora a convicção do usuário, o veredito anterior e a autoria da ideia. O orquestrador escolhe o template, mas não redige o brief livremente.

Faltam profundidade e escrita. Um preprint de setembro de 2026, de autor único e ainda sem revisão, modela árvores de decomposição a partir de 600 execuções reais de pesquisa. Ele conclui que cada nível de resumo perde achados (expoente de retenção δ = 0,34) e que o ótimo, contando integridade e custo, fica em dois ou três níveis ([arXiv 2609.17464](https://arxiv.org/abs/2609.17464) · resumo). É evidência fraca, mas aponta na mesma direção da prática. O Claude Code permite três níveis abaixo da conversa principal por padrão ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido), e o harness precisa de um só. Isso se garante retirando a ferramenta `Agent` da lista `tools` de todo subagente.

Quanto à escrita, três fontes apontam para o mesmo desenho:

- O sistema de pesquisa da Anthropic evita o efeito "telefone sem fio" fazendo os subagentes "guardarem o trabalho em sistemas externos e passarem referências leves de volta ao coordenador" ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).
- No benchmark da LangChain, o supervisor melhorou cerca de 50% quando passou a repassar a saída dos subagentes em vez de parafraseá-la ([LangChain](https://www.langchain.com/blog/benchmarking-multi-agent-architectures) · resumo).
- O *12-Factor* trata o agente como uma função sem estado que recebe um retrato do estado e devolve um evento ([12-Factor, fator 5](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) · lido).

**Ajuste sinalizado à confirmação "Escrita centralizada na sessão principal".** A regra vale para o estado canônico e para as decisões, mas o escritor único deve ser um **script validador**, e não a sessão LLM. Cada subagente escreve apenas o próprio arquivo de staging (`runs/<id>/<papel>-<n>.jsonl`). Nenhum arquivo tem dois escritores, o que preserva a preocupação da Cognition com decisões implícitas conflitantes num artefato compartilhado.

Os **agent teams** do Claude Code ficam descartados. São experimentais, vêm desligados por padrão, têm colegas que "compartilham e contestam os achados uns dos outros" e "usam significativamente mais tokens" ([Claude Code, agent teams](https://code.claude.com/docs/en/agent-teams) · lido). Trata-se de negociação entre pares, a forma que MAST e Cognition associam a falha.

### O isolamento padrão vaza por quatro caminhos

A documentação de subagentes lista o que um subagente comum (não fork) recebe ao ser criado: o próprio prompt, a mensagem de delegação escrita pelo Claude, **"todos os níveis da hierarquia de CLAUDE.md que a conversa principal carrega"**, um retrato do git status, as skills pré-carregadas e, se tiver `SendMessage`, a lista dos agentes irmãos ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido). Para juiz, advogado e cético, isso abre quatro vazamentos:

1. **CLAUDE.md.** Fecha-se com `omitClaudeMd: true` (v2.1.271+), como R-11 já propõe. Como defesa em profundidade, o CLAUDE.md nunca cita oportunidades específicas nem preferências sobre teses.
2. **Git status.** A documentação é explícita: "não dá para mudar quais subagentes recebem o git status". A mitigação *(inferência)* é uma convenção de commits e branches com nomes neutros ("OP-0007: dossiê v2", nunca "OP-0007 promissora").
3. **Forks.** Vêm ligados por padrão em sessões interativas desde a v2.1.232, "herdam a conversa inteira" e, com isso, "abandonam o isolamento de entrada". Por isso avaliadores são sempre tipos nomeados em `.claude/agents/`.
4. **Mensagem de delegação.** R-11 já identificou esse vazamento, e o template gerado por script o resolve.

Há ainda três detalhes da mesma documentação:

- O parâmetro `model` passado na chamada vence o `model` do frontmatter, então o orquestrador pode trocar o modelo do juiz sem aviso.
- `memory:` injeta o `MEMORY.md` do agente a cada execução, o que traria vereditos passados para julgamentos que deveriam ser cegos.
- As transcrições de subagentes são apagadas após 30 dias por padrão.

O perfil do avaliador fica assim:

- tipo nomeado, nunca fork;
- `omitClaudeMd: true`;
- `tools` só de leitura, sem `Agent` e sem `SendMessage`;
- sem `memory`;
- `model` fixado;
- entrada só por caminhos de arquivo;
- transcrição copiada para o repo.

Um hook SubagentStop filtrado pelo `agent_type` do juiz valida o JSON do veredito e força refazer quando o JSON é inválido. O limite é que o Claude Code encerra o turno após 8 bloqueios seguidos ([Claude Code, hooks](https://code.claude.com/docs/en/hooks) · lido). A opção de isolamento máximo é chamar o juiz por `claude -p --bare --json-schema` a partir de um diretório neutro: sem CLAUDE.md, sem hooks e sem repositório para vazar git status *(inferência sobre [Claude Code, headless](https://code.claude.com/docs/en/headless) · lido)*. Fica como teste contra o subagente de R-11.

## Contexto é orçamento: arquivos, ponteiros e prefixos estáveis

A Anthropic trata contexto como "um recurso finito com retorno marginal decrescente". À medida que os tokens aumentam, a capacidade de recuperar informação cai ("context rot"), e o objetivo passa a ser "o menor conjunto possível de tokens de alto sinal" ([Anthropic, engenharia de contexto](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · lido). O estudo da Chroma encontrou essa degradação nos 18 modelos testados, inclusive o Claude 4 ([Chroma](https://www.trychroma.com/research/context-rot) · resumo).

No harness, o risco concreto é a sessão principal acumular páginas cruas e resultados intermediários ao longo de um `/validar`; o que ela parafrasear para o juiz carrega a inclinação dela. A resposta é manter três coisas fora do contexto da sessão principal:

- evidência bruta, que fica em arquivos;
- resultados intermediários, em variáveis do workflow ou em staging;
- erros já resolvidos, que ficam em log.

O Claude Code cobra cada camada de um jeito diferente ([Claude Code, visão geral de recursos](https://code.claude.com/docs/en/features-overview) · lido):

- o CLAUDE.md entra inteiro em toda requisição;
- das skills, as descrições entram sempre e o corpo só quando a skill é usada;
- do MCP, entram os nomes das ferramentas, com os schemas sob demanda;
- subagentes ficam isolados;
- hooks custam "zero, a menos que devolvam contexto adicional".

Daí a hierarquia de onde cada coisa mora:

- **CLAUDE.md.** É um mapa com menos de 200 linhas, porque "arquivos mais longos consomem mais contexto e reduzem a adesão" ([Claude Code, memória](https://code.claude.com/docs/en/memory) · lido). A OpenAI chegou ao mesmo formato num produto de ~1 milhão de linhas e ~1.500 PRs escrito por agentes: um AGENTS.md de ~100 linhas que aponta para documentos versionados ([OpenAI, harness engineering](https://openai.com/index/harness-engineering/) · resumo).
- **Regras por pasta.** Vão para `.claude/rules/*.md` com `paths:`, e só carregam quando arquivos correspondentes são tocados. Notas de manutenção vão em comentários HTML, que são removidos antes da injeção ([Claude Code, memória](https://code.claude.com/docs/en/memory) · lido).
- **Procedimentos.** Vão para skills, que carregam em três níveis: ~100 tokens de metadados sempre, corpo com menos de 5 mil tokens quando a skill é acionada, e arquivos e scripts anexos sem limite. Os scripts rodam "sem carregar o script no contexto" ([Visão geral de Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · lido).

Um detalhe muda a forma de escrever as skills. Depois da compactação, a invocação mais recente de cada skill volta ao contexto com só **os primeiros 5 mil tokens**, dentro de um orçamento total de 25 mil ([Claude Code, skills](https://code.claude.com/docs/en/skills) · lido). Por isso as regras que não podem se perder ficam no topo. E como o juiz não deve carregar os prompts do advogado e do cético (R-09 pede memorandos sem rótulo), o `analista-imparcial` precisa ser dividido por papel. Cada subagente pré-carrega, pelo campo `skills`, só a parte que lhe cabe *(inferência)*.

Subagentes devolvem pouco. Na formulação da Anthropic, um subagente "pode explorar extensamente, usando dezenas de milhares de tokens ou mais, mas devolve só um resumo condensado e destilado do trabalho (muitas vezes 1.000 a 2.000 tokens)" ([Anthropic, engenharia de contexto](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · lido). O texto completo vai para arquivo. O juiz lê os arquivos de evidência, e nunca a paráfrase do orquestrador.

O formato do estado também é engenharia de contexto. No harness para agentes de longa duração, a Anthropic registrou mais de 200 funcionalidades num arquivo em que o agente só podia mudar o campo de status. Escolheu JSON porque "o modelo tem menos chance de alterar ou sobrescrever indevidamente arquivos JSON do que arquivos Markdown" ([Anthropic, harnesses para agentes longos](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · lido). Hoje a arquitetura guarda estágio, status, próximo teste e prazo no frontmatter de `cartao.md` (§7). A mudança proposta *(inferência sobre fontes lidas)* tem duas partes.

A primeira é um **log de eventos append-only** (`data/eventos.jsonl`). Nele, transições de estágio e decisões GO/ITERAR/KILL são eventos, e o status é derivado do log. O *12-Factor* defende unificar estado de execução e de negócio numa sequência serializável e tratar contato humano como chamada estruturada ([12-Factor, fator 5](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-05-unify-execution-state.md) · lido). A Anthropic construiu os Managed Agents em torno de uma sessão que é "o log append-only de tudo o que aconteceu" e que "não é a janela de contexto do Claude" ([Anthropic, Managed Agents](https://www.anthropic.com/engineering/managed-agents) · lido).

A segunda é um **contrato de validação** por oportunidade: critérios e limiares gravados em JSON antes da coleta, com só o campo de status mutável depois disso, protegido por hook. É o "contrato de sprint" que gerador e avaliador negociavam antes de escrever código ([Anthropic, desenho de harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) · lido), aplicado ao princípio 2. Também combina com o achado de R-13 de que definir hipóteses e critérios antes do teste melhora os resultados. O `cartao.md` continua existindo, só com a narrativa.

A continuidade entre sessões vem de arquivo, não de memória. A auto memory do Claude Code é "local à máquina" e não chega a ambientes de nuvem nem a subagentes ([Claude Code, memória](https://code.claude.com/docs/en/memory) · lido), então rotinas nunca a veriam. O ritual de início da Anthropic é ler o arquivo de progresso, o git log e a lista de pendências antes de agir ([Anthropic, harnesses para agentes longos](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · lido). No harness, ele vira um hook SessionStart que roda `portfolio.py --compacto` e injeta o estado atual em poucas linhas *(inferência)*. O plano de cada comando é gravado em arquivo antes da execução, como faz o líder do sistema de pesquisa, porque o contexto acima de 200 mil tokens seria truncado ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).

Custo e estabilidade andam juntos. No Opus 5.5, entrada custa US$4 por milhão de tokens e leitura de cache custa US$0,20, ou seja, **20× menos**. Uma tarefa com 2,8 milhões de tokens de entrada sai por US$11,20 sem cache e por US$1,62 com 90% de acerto de cache ([custo no Opus 5.5](https://claude.com/blog/what-a-task-costs-on-opus-5-5) · lido). A Manus chama a taxa de acerto do cache de "a métrica mais importante para um agente em produção" e relata uma razão entrada:saída de ~100:1 em tarefas de ~50 chamadas de ferramenta ([Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) · resumo). A consequência prática *(inferência)*:

- CLAUDE.md, skills e prompts de subagentes ficam idênticos byte a byte entre execuções, sem datas ou ids de execução no topo;
- scripts emitem JSON com chaves ordenadas;
- dados voláteis vão para o fim.

Duas práticas de contexto se contradizem nas fontes e precisam de conciliação. A Manus manda manter falhas no contexto para o modelo não repeti-las ([Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) · resumo); o *12-Factor* manda esconder erros depois de resolvidos ([12-Factor, fator 3](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md) · lido). As duas cabem: falhas ficam visíveis dentro da execução e registradas em log, mas não entram em briefs novos.

A Manus também relata que pares repetitivos de ação e observação fazem o modelo imitar o padrão; revisar 20 currículos seguidos gerou deriva ([Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) · resumo). Isso desaconselha julgar várias oportunidades no mesmo contexto: cada julgamento roda em contexto novo, uma oportunidade por chamada do juiz.

Já a maquinaria de reset de contexto é dispensável, porque a compactação automática passou a bastar a partir do Opus 4.5 ([Anthropic, desenho de harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) · lido). E a regra da documentação de usar `/clear` depois de duas correções fracassadas ([Claude Code, boas práticas](https://code.claude.com/docs/en/best-practices) · lido) sai barata num harness cujo estado inteiro está em arquivo.

Contexto persistido também é superfície de ataque. A Anthropic avisa que "a saída de ferramentas é superfície de ataque mesmo quando a ferramenta é confiável" e que uma injeção em CLAUDE.md ou nos diretórios de estado de agentes agendados "é recarregada toda vez que o agente começa". Avisa também que tratar a saída de um subagente como mais confiável que o resultado bruto de ferramenta abre um vetor de ataque novo ([Anthropic, contenção](https://www.anthropic.com/engineering/how-we-contain-claude) · lido). O Claude Code já neutraliza texto de `<system-reminder>` e `Human:` injetado em relatórios de subagentes e marca esses relatórios como sem autoridade do usuário, desde a v2.1.210 ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido). R-12 fica confirmado, com um acréscimo: resumo de subagente nunca tem mais autoridade que as fontes que cita.

## Claude Code peça por peça, e as falhas que não avisam

A tabela resume o uso recomendado de cada recurso na versão instalada (2.1.281). As fontes são a documentação oficial, lida na íntegra.

| Recurso | Papel no harness | Configuração recomendada | Armadilha documentada |
|---|---|---|---|
| CLAUDE.md | Mapa do repo, encaminhamento da pergunta livre para o comando certo, regras com motivo, regra de dado não confiável (R-12) | Menos de 200 linhas; sem oportunidades nem preferências; notas em comentário HTML | Chega como mensagem de usuário, sem garantia; vai para todo subagente sem `omitClaudeMd` |
| `.claude/rules/` | Regras de `data/**`, `scripts/**`, `oportunidades/**` | Com `paths:` para carregar só quando necessário | Regra sem `paths` carrega sempre |
| Skills (e comandos, agora fundidos a elas) | `/radar`, `/kill`, `/validar` etc.; procedimentos do pesquisador e do analista, divididos por papel | Descrição de até 1.024 caracteres, em terceira pessoa; corpo com menos de 500 linhas; referências a um nível; scripts como nível 3 | Após compactação, só os primeiros 5 mil tokens voltam; skills sincronizadas aceitam só seis campos |
| Subagentes | Batedor, pesquisador, verificador, advogado, cético, juiz, revisores | `tools` explícito sem `Agent`; `model`, `effort`, `maxTurns`; perfil de avaliador | Campos desconhecidos ignorados; YAML quebrado some sem aviso; forks herdam tudo |
| Hooks | Validação de escrita, schema do veredito, contagem de custo e de buscas, status no início | Em `.claude/settings.json` commitado; scripts que bloqueiam em caso de falha, com saída 2 | Saída 1 não bloqueia; timeout não bloqueia; 8 bloqueios seguidos encerram o turno |
| Permissões | Limite duro de ações externas | `deny` para publicar, enviar e gastar; `dontAsk` sem supervisão | `allow` não abre exceção em `deny`; modo auto deixa passar 17% das ações arriscadas |
| `claude -p` | Chamadas isoladas por script, evals, juiz em isolamento máximo | `--json-schema`; `--output-format json` para registrar custo | `--bare` também desliga hooks e skills do projeto |
| Dynamic workflows | Roteiro fixo de `/radar` e `/validar` | Salvos em `.claude/workflows/`; teto de agentes explícito | Sem entrada humana no meio; aviso acima de 25 agentes ou 1,5M tokens |
| Rotinas | Radar semanal na nuvem, revisado por você | Domínios "Custom" no ambiente (R-02 a) | Intervalo mínimo de 1 h; teto diário; prévia de pesquisa; MCP só via conector ou `.mcp.json` commitado |
| Tarefas agendadas do desktop | Coleta local, se a nuvem continuar bloqueada (R-02 b) | Mesmos comandos da rotina | Dependem da sua máquina |

Ficam fora por ora:

- `/loop`, que expira em 7 dias.
- Agent teams, que são experimentais.
- Plugins, porque subagentes de plugin ignoram `hooks`, `mcpServers` e `permissionMode` ([Claude Code, plugins](https://code.claude.com/docs/en/plugins) · lido), o que desmontaria a validação do juiz. O harness fica como configuração de projeto.
- A auto memory como estado, por ser local à máquina.
- O `/goal`, em que um modelo pequeno decide se a tarefa terminou. A documentação lista o Stop hook como o portão determinístico ([Claude Code, boas práticas](https://code.claude.com/docs/en/best-practices) · lido).
- O Agent SDK, já descartado por D-001; o `claude -p` cobre as chamadas por script.

O que as armadilhas têm em comum é o silêncio:

- **Hooks.** "O código de saída 2 é o único que bloqueia", e o Claude Code "trata o código 1 como erro não bloqueante e segue em frente" ([Claude Code, hooks](https://code.claude.com/docs/en/hooks) · lido). Um traceback Python no `validate.py` deixa a escrita passar. Um hook PreToolUse que estoura o tempo também não bloqueia, e a documentação diz para "não contar com um hook travado como portão". Por isso o `validate.py` precisa bloquear em caso de falha (capturar toda exceção e sair com 2), ser rápido e não depender de rede.
- **Subagentes.** Campos desconhecidos no frontmatter são "ignorados em silêncio" e arquivos com YAML quebrado são pulados sem aviso ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido). Um `omitClaudeMd` digitado errado faria o juiz carregar o CLAUDE.md sem ninguém saber. Por isso o CI roda `claude plugin validate .claude/agents`.
- **Skills.** O Claude Code trunca a descrição somada a `when_to_use` em 1.536 caracteres, mas a especificação aberta limita `description` a 1.024 ([Claude Code, skills](https://code.claude.com/docs/en/skills) · lido; [Boas práticas de skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · lido). Usar 1.024 atende as duas. Skills sincronizadas com o claude.ai só aceitam seis campos (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) e qualquer outro gera erro. Skills com `disable-model-invocation: true` não rodam em tarefas agendadas. As duas regras pesam na pergunta A-06.
- **Nuvem.** Sessões na nuvem não leem `~/.claude/settings.json` ([Claude Code, hooks](https://code.claude.com/docs/en/hooks) · lido), então todo hook e toda regra vão para `.claude/settings.json` commitado.
- **Busca.** A WebSearch tem teto de 200 chamadas por sessão, somando todos os subagentes, e as chamadas acima do teto "parecem buscas que não acharam nada" ([Claude Code, referência de ferramentas](https://code.claude.com/docs/en/tools-reference) · lido (fluxo E)). A seção de orçamento trata disso.

Permissões são a outra camada dura. As regras são avaliadas na ordem "deny, depois ask, depois allow", e "uma regra allow não abre exceção numa regra deny" ([Claude Code, permissões](https://code.claude.com/docs/en/permissions) · lido). O modo auto nasceu porque usuários aprovam 93% dos pedidos de permissão. Seu classificador tem 0,4% de falso positivo, mas **17% de falso negativo** de ponta a ponta ([modo auto](https://www.anthropic.com/engineering/claude-code-auto-mode) · lido): deixa passar uma em cada seis ações arriscadas. Para o princípio 9, isso significa três medidas:

- regras `deny` explícitas para tudo que publica, envia mensagem ou gasta dinheiro;
- `dontAsk` em execuções sem supervisão, para negar automaticamente o que pediria permissão;
- `disable-model-invocation: true` em qualquer skill com efeito externo, para que só você a dispare ([Claude Code, skills](https://code.claude.com/docs/en/skills) · lido).

Para a operação recorrente da fase 5, as **rotinas** rodam na nuvem sem precisar de máquina ligada ([Claude Code, rotinas](https://code.claude.com/docs/en/routines) · lido):

- clonam o repo do zero a cada execução;
- não pedem permissão;
- têm intervalo mínimo de uma hora e um teto diário de execuções por conta;
- entregam o trabalho em branches `claude/`.

O ambiente padrão tem rede "Trusted", que responde `403 host_not_allowed` para domínios fora da lista. É exatamente o bloqueio de R-02, e a opção (a) de R-02 corresponde a cadastrar os domínios como "Custom". Um MCP instalado localmente com `claude mcp add` não chega às rotinas; só chegam conectores do claude.ai ou um `.mcp.json` commitado. Isso importa para a decisão de R-14.

A opção (b) de R-02 corresponde às **tarefas agendadas do desktop**, que rodam na sua máquina, com arquivos locais e intervalo mínimo de um minuto. O `/loop` expira em 7 dias e não serve para operação ([Claude Code, tarefas agendadas](https://code.claude.com/docs/en/scheduled-tasks) · lido). Ficam duas incertezas para a fase 5: as rotinas ainda são prévia de pesquisa, e o teto diário não aparece na documentação, só na interface.

## Ferramentas que devolvem pouco e explicam o próprio erro

No apêndice de *Building effective agents*, a Anthropic conta que gastou "mais tempo otimizando as ferramentas do que o prompt geral". Exigir caminhos absolutos eliminou os erros de caminho relativo, e a recomendação é desenhar ferramentas que o agente não consiga usar errado ("poka-yoke") ([Building effective agents](https://www.anthropic.com/research/building-effective-agents) · lido). No harness, "ferramenta" é sobretudo script Python chamado por Bash. O post sobre ferramentas para agentes dá as regras de desenho ([Anthropic, ferramentas para agentes](https://www.anthropic.com/engineering/writing-tools-for-agents) · lido):

- consolidar operações em vez de embrulhar endpoints (`search_contacts` em vez de `list_contacts`);
- devolver contexto significativo e ids legíveis em vez de UUIDs;
- oferecer um parâmetro de formato conciso ou detalhado, que num caso reduziu uma resposta de 206 para 72 tokens;
- paginar e truncar com uma mensagem que oriente o próximo passo;
- escrever mensagens de erro que digam o que fazer.

O Claude Code limita respostas de ferramentas a 25 mil tokens por padrão.

Filtrar em código antes de devolver é o maior ganho documentado. Carregar definições de ferramentas como arquivos e filtrar dados em código levou um caso de 150 mil para 2 mil tokens, **−98,7%** ([Anthropic, execução de código com MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) · lido). Chamadas programáticas de ferramentas cortaram 37% dos tokens em tarefas complexas de pesquisa ([Anthropic, uso avançado de ferramentas](https://www.anthropic.com/engineering/advanced-tool-use) · lido).

O projeto do compilador C acrescenta disciplina de saída ([Anthropic, compilador C](https://www.anthropic.com/engineering/building-c-compiler) · lido):

- imprimir poucas linhas e registrar o resto em arquivo;
- escrever `ERROR` e o motivo numa linha só, para o grep encontrar;
- oferecer uma amostra rápida de 1% ou 10%, para o agente não gastar horas numa execução completa sem perceber o tempo passar;
- usar arquivos de trava para que agentes paralelos peguem tarefas diferentes.

E traz um aviso central: "o verificador da tarefa precisa ser quase perfeito, senão o Claude resolve o problema errado". A tabela traduz essas regras num contrato que todo script do harness cumpre *(inferência sobre fontes lidas)*:

| Aspecto | Regra | Por quê |
|---|---|---|
| Operação | Uma operação de negócio por comando (`buscar_empresas --cnae --municipio`), não um espelho da API | Consolidar reduz escolhas erradas |
| Argumentos | Caminhos absolutos; nomes inequívocos (`--id-oportunidade`, não `--id`); validação antes de agir | Evita uso errado |
| Saída | Resumo curto no stdout, detalhe em arquivo; `--formato` conciso ou detalhado; filtrar e agregar antes de imprimir | Contexto é orçamento |
| Ids | `OP-0007`, `F-000123`, nunca UUID | Precisão do modelo |
| Erros | Uma linha `ERRO: <motivo>. Tente: <ação>`; código de saída diferente de 0 | Erro acionável e localizável por grep |
| Serialização | JSON com chaves ordenadas; sem timestamps no topo | Cache e diffs estáveis |
| Escala | `--amostra 0.1`; trava por tarefa em `runs/<id>/travas/` | Controle de tempo; paralelismo sem colisão |
| Leitura de página | Texto bruto via `curl` ou `requests`, salvo com hash; nunca o resumo da WebFetch como evidência | Ver abaixo |

A última linha vem de um achado do fluxo de fontes (R-14) que muda o desenho do verificador de citações. A WebFetch nativa é "com perdas por desenho": um modelo pequeno responde ao prompt a partir de uma conversão truncada da página, e o Claude "recebe a resposta desse modelo, não a página bruta". Um resultado dizendo que a página não menciona X "pode significar só que o prompt não perguntou". Para obter a página bruta, a própria documentação aponta o `curl` ([Claude Code, referência de ferramentas](https://code.claude.com/docs/en/tools-reference) · lido (fluxo E)).

O protocolo de R-05 exige trecho literal, e trecho literal não sobrevive a um resumidor. A divisão correta *(inferência)* separa o determinístico do difuso. Um script baixa a página bruta e confere, por comparação de texto, se o trecho citado existe nela. O subagente verificador só julga se o trecho, que já se sabe existir, sustenta a alegação. E "a página não menciona X", quando obtido pela WebFetch, nunca vale como evidência de ausência.

Essa separação é a regra geral. O post do Agent SDK classifica o feedback baseado em regras como a melhor forma de verificação e diz que LLM como juiz "em geral não é um método muito robusto", além de custar latência ([Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) · lido). *Building effective agents* acrescenta que uma chamada separada de triagem funciona melhor que a mesma chamada fazendo triagem e tarefa ([Building effective agents](https://www.anthropic.com/research/building-effective-agents) · lido).

Tudo o que os pacotes de trilha permitem codificar vira checagem de script: piso de ambição, ticket abaixo de ~R$150 (R-04), ciclo de venda acima de 30 dias, fonte presente, validade do fato, link que abre. O LLM fica com o que sobra de difuso. O linter de neutralidade começa como lista determinística de termos avaliativos. Hooks do tipo `prompt` existem, mas são julgamento de LLM com tempo limite de 30 s e, se estouram, não bloqueiam ([Claude Code, hooks](https://code.claude.com/docs/en/hooks) · lido).

Sobre quantidade de ferramentas, a Anthropic registra que "um dos modos de falha mais comuns são conjuntos inchados de ferramentas": se um engenheiro humano não sabe dizer qual usar, o agente também não saberá ([Anthropic, engenharia de contexto](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · lido). A OpenAI localiza o problema na sobreposição ([OpenAI, guia prático](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) · resumo). Se R-14 ligar um MCP de busca, cada tipo de subagente recebe, via `tools`, uma ferramenta de busca, e não duas concorrentes *(inferência)*.

Por fim, descrições são prompt:

- ferramentas descritas como para "um recém-contratado", com parâmetros inequívocos ([Anthropic, ferramentas para agentes](https://www.anthropic.com/engineering/writing-tools-for-agents) · lido);
- skills descritas em terceira pessoa, dizendo o que fazem e quando usar ([Boas práticas de skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · lido), com gatilhos em português e inglês.

Reescrever descrições funciona. Um agente que testou ferramentas e reescreveu descrições ruins de MCP reduziu em **40%** o tempo de conclusão dos agentes seguintes ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido). O ajuste de descrições do skill-creator melhorou o disparo em 5 de 6 skills públicas ([skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) · lido). O ciclo mensal de melhoria inclui o Claude lendo transcrições com falha e propondo novas descrições, aceitas só se o eval melhorar.

## Orçamento por comando: pouco para matar, muito para julgar

O princípio 8 é o mais bem sustentado da arquitetura. No BrowseComp, três fatores explicaram 95% da variância de desempenho do sistema de pesquisa da Anthropic, e **o uso de tokens sozinho explicou 80%**. Os outros dois fatores foram o número de chamadas de ferramenta e o modelo, e trocar para um modelo melhor rendeu mais que dobrar o orçamento de tokens no modelo anterior. Agentes gastam cerca de 4× os tokens de um chat, e sistemas multiagente cerca de 15× ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido). Daí três consequências *(inferência)*:

- orçamento é botão de qualidade, e não só de custo;
- escolher o modelo vem antes de aumentar o orçamento, o que pede cautela com batedores num modelo mais barato (A-05);
- toda comparação entre variantes do harness precisa de orçamento igual, senão mede gasto, e não desenho.

Sem teto, os agentes erram de formas previsíveis. A Anthropic viu o sistema "criando 50 subagentes para consultas simples, vasculhando a web sem fim atrás de fontes inexistentes", continuando depois de já ter resultado suficiente e preferindo "fazendas de conteúdo otimizadas para SEO" a fontes de autoridade. A correção foi escrever no prompt regras de escala de esforço:

- **fato simples:** 1 agente, com 3 a 10 chamadas;
- **comparação direta:** 2 a 4 subagentes, com 10 a 15 chamadas cada;
- **pesquisa complexa:** mais de 10 subagentes, com responsabilidades bem divididas.

As buscas também começam curtas e amplas antes de estreitar ([Anthropic, sistema de pesquisa multiagente](https://www.anthropic.com/engineering/multi-agent-research-system) · lido).

O Claude Code dá os controles para aplicar essas faixas ([Claude Code, subagentes](https://code.claude.com/docs/en/sub-agents) · lido; [Claude Code, workflows](https://code.claude.com/docs/en/workflows) · lido):

- `maxTurns` por subagente (a saída volta marcada como parcial);
- `effort`, de `low` a `max`, por subagente e por skill;
- `model` por subagente;
- até 20 subagentes simultâneos;
- nos workflows, um aviso de "workflow grande" acima de 25 agentes ou 1,5 milhão de tokens projetados.

Há também um teto que a arquitetura não previa e que já afetou este projeto: **200 chamadas de WebSearch por sessão, somando a sessão principal e todos os subagentes**. O teto é ajustável por variável de ambiente, mas não pode ser desligado, e `/clear` o zera. Chamadas acima dele parecem buscas vazias ([Claude Code, referência de ferramentas](https://code.claude.com/docs/en/tools-reference) · lido (fluxo E); observado nesta sessão, R-02). Isso tem duas consequências de desenho *(inferência)*:

- Um radar semanal com 11 lentes, a 10–15 buscas cada, consome de 110 a 165 buscas, quase o teto inteiro. Cada comando pesado roda, portanto, em sessão própria, ou cada batedor em sua própria chamada `claude -p`.
- A regra de parada "três buscas vazias = registrar ausência" produziria falsos "não encontrado" quando o teto estourasse em silêncio. Um hook PostToolUse que conta as buscas da execução precisa marcar a rodada como "orçamento esgotado", nunca como ausência de evidência.

Quanto ao preço, a Anthropic mostra os dois lados. Seu harness completo de desenvolvimento custou **20× mais** que o agente sozinho (US$200 contra US$9), mas o agente sozinho entregou um app com a funcionalidade central quebrada ([Anthropic, desenho de harness](https://www.anthropic.com/engineering/harness-design-long-running-apps) · lido). E no Opus 5.5 "uma nova tentativa custa mais do que essas economias" de cache ([custo no Opus 5.5](https://claude.com/blog/what-a-task-costs-on-opus-5-5) · lido). Gastar se justifica onde errar é caro, isto é, no veredito que decide o que vai para teste com comprador, e não no volume do radar. A tabela propõe tetos iniciais por comando, derivados das faixas da Anthropic e calibráveis pelos evals *(inferência)*:

| Comando | Faixa (Anthropic) | Subagentes (teto) | Buscas por subagente | Regra de parada | Observação |
|---|---|---|---|---|---|
| `/oportunidade` | — | 0 | 0 (só arquivos) | Cartão validado pelo schema | Dedupe em script |
| `/kill` | Fato simples | 1 pesquisador | 3–10 por alegação (até 30) | Para quando 2 alegações caem | Portão aplicado por script |
| `/radar <foco>` | Comparação | 2–4 batedores | 10–15 | Teto de sinais por lente | Só leitura; fan-out barato |
| `/radar` semanal | Pesquisa complexa | 1 por lente ativa, até 16 simultâneos | 10–15 | Idem; sessão própria | Rotina ou tarefa agendada (R-02) |
| `/validar` | Pesquisa complexa | 2–4 pesquisadores + verificador + advogado + cético + juiz (até 8) | 10–15 nos pesquisadores; 0 nos três avaliadores | No máximo 1 rodada extra de coleta | Só para quem passou no kill; abaixo de 25 agentes e 1,5M tokens |
| `/oferta` | — | 1 revisor | 0–5 | No máximo 2 ciclos gerar-revisar | Skill na sessão principal |
| `/teste`, `/resultado` | — | 0 | 0 | — | Script aplica o limiar escrito antes |
| `/portfolio`, `/calibrar` | — | 0 | 0 | — | Só script; o LLM comenta |
| `/construir` | — | 1 revisor por entrega | — | Portão por entrega | Sessão dedicada |

O custo real entra no painel sem gastar contexto. Hooks recebem `agent_id` e `agent_type` mesmo dentro de subagentes ([Claude Code, hooks](https://code.claude.com/docs/en/hooks) · lido). Assim, um hook PostToolUse grava uma linha por chamada em `runs/<id>/custo.jsonl`, e as chamadas headless registram `total_cost_usd` *(inferência)*. Isso alimenta a métrica "custo por oportunidade avaliada" da §9.

Um último ponto decorre da própria evidência: se o orçamento explica a maior parte do desempenho, **orçamento assimétrico enviesa o dossiê**. Um pesquisador que gasta doze buscas atrás de demanda e três atrás de concorrentes e motivos de fracasso entrega um dossiê inclinado, mesmo com instruções neutras. Por isso o template do brief reserva uma cota fixa de buscas para evidência contrária *(inferência, a testar)*.

## Conclusão

A pesquisa desloca a pergunta de design de "quantos agentes" para "o que cada agente vê, quem escreve e o que bloqueia". O material mais recente da OpenAI sobre harness quase não fala de topologia e fala muito de ambiente ([OpenAI, harness engineering](https://openai.com/index/harness-engineering/) · resumo). As fontes da Anthropic de 2026 vão no mesmo sentido. Neste harness, o ponto frágil não é o raciocínio do modelo, e sim os caminhos silenciosos:

- o CLAUDE.md que chega a todo subagente;
- um commit com nome opinativo no git status;
- um brief parafraseado;
- um validador que sai com código 1;
- um campo de frontmatter digitado errado;
- uma busca que bateu no teto e parece vazia.

Nenhum deles aparece num relatório bem escrito. Por isso a fatia vertical precisa testar o próprio harness, além dos evals de comportamento: um teste que falha se a entrada do juiz contém a convicção do usuário, outro que confirma que a escrita direta em `data/` é bloqueada, outro que valida o frontmatter de todo agente. São os testes unitários da neutralidade.

A segunda implicação é sobre tempo. Cada componente é uma aposta sobre uma fraqueza do modelo, e essas apostas vencem. Como tokens explicam a maior parte do desempenho, toda ablação precisa fixar o orçamento, ou vai confundir gasto com desenho. O funil já tem a economia que a evidência recomenda: o kill barato é uma cascata, e o veredito é onde gastar compensa. A aposta ainda sem resposta é se advogado e cético diante de um juiz superam um único cético calibrado em julgamento de negócio. Resolvê-la custa pouco com os ~20 casos não contaminados de R-07, e esse deve ser o primeiro experimento da fase 3, antes que o trio vire infraestrutura.

## Adotar / Descartar / Testar

### Adotar

| # | O que adotar | Muda | Base |
|---|---|---|---|
| A1 | Cada comando executa um roteiro fixo em código (workflow ou script Python com `claude -p`); o CLAUDE.md só encaminha a pergunta para o comando; portões humanos ficam entre execuções | Princípio 4; §6 (camadas); §6.2 | lido |
| A2 | Regra "isolar quem avalia, não quem executa": o estrategista de oferta vira a skill `desenho-de-oferta` na sessão principal, com revisor isolado; o construtor roda em sessão dedicada, também com revisor isolado | Princípio 5; §6.1; §5 (estágios 4 e 6) | lido + resumo + inferência |
| A3 | Perfil de avaliador (juiz, advogado, cético, verificador, revisores): tipo nomeado, nunca fork; `omitClaudeMd: true`; `tools` só de leitura, sem `Agent` e sem `SendMessage`; sem `memory`; `model` fixado; entrada por caminhos de arquivo, em template gerado por script; transcrição copiada para o repo | §6.1; estende R-11 | lido |
| A4 | Advogado e cético não buscam na web: leem só o dossiê | Princípio 1; §6.1 | inferência |
| A5 | O escritor único do estado canônico é um script validador; cada subagente escreve só o próprio arquivo de staging e devolve caminho + resumo de até ~2 mil tokens | Princípio 5; §7; §8; ajusta a confirmação "Escrita centralizada" de `revisao-pendente.md` | lido + resumo |
| A6 | `validate.py` como hook PreToolUse que bloqueia em caso de falha (sai com 2 em qualquer exceção, sem rede); escrita direta em `data/` bloqueada; SubagentStop valida o JSON do juiz; tudo em `.claude/settings.json` commitado; pytest no CI como rede final | §6 (guarda-corpos); §8; §9 nível 1 | lido |
| A7 | O status sai do frontmatter: log `data/eventos.jsonl` append-only com transições e decisões GO/ITERAR/KILL; `portfolio.py` deriva o painel dele; `cartao.md` fica só com a narrativa | §7; ajusta D-005 | lido |
| A8 | Contrato de validação por oportunidade em JSON, gravado antes da coleta; depois disso só o campo de status muda (protegido por hook) | Princípio 2; §5.2 | lido + inferência |
| A9 | Tabela de orçamento por comando (teto de subagentes, buscas, `maxTurns`, regra de parada); fan-out completo só depois do kill barato; um comando pesado por sessão, por causa do teto de 200 buscas | Princípio 8; §6.2; §10 (custo) | lido + inferência |
| A10 | Hook PostToolUse conta chamadas por `agent_type` e marca "orçamento esgotado" quando o teto de busca estoura; chamadas headless registram `total_cost_usd` | §9 (métrica de custo); §10 | lido + inferência |
| A11 | Contrato de scripts: operação consolidada, caminhos absolutos, ids legíveis, `--formato`, saída curta com log em arquivo, erro acionável em uma linha, JSON ordenado, `--amostra`, travas | §8 | lido |
| A12 | Verificação de citação em duas partes: um script confere o trecho literal na página bruta (`curl`); o subagente só julga se o trecho sustenta a alegação; resumo da WebFetch nunca vale como evidência de ausência | §8; estende R-05 e R-14 | lido (fluxo E) + inferência |
| A13 | Contexto em camadas: CLAUDE.md-mapa com menos de 200 linhas e sem nomes de oportunidades; `.claude/rules/` com `paths:`; regras críticas nos primeiros 5 mil tokens de cada skill; `analista-imparcial` dividida por papel; SessionStart injeta o status compacto | §6; §10 (contexto degradando) | lido + inferência |
| A14 | Cada julgamento em contexto novo; uma oportunidade por chamada do juiz | §10; princípio 5 | resumo + inferência |
| A15 | Commits e branches com nomes neutros | R-11; §7 | lido + inferência |
| A16 | Regras `deny` para publicar, enviar e gastar; `dontAsk` sem supervisão; `disable-model-invocation: true` em skills com efeito externo; o modo auto nunca serve de guarda | Princípio 9 | lido |
| A17 | O CI valida o frontmatter de agentes e skills (`claude plugin validate`); descrições de skill com até 1.024 caracteres, em terceira pessoa, com gatilhos em português e inglês | §9 nível 1; §6 (skills) | lido |
| A18 | Radar semanal como rotina com domínios "Custom" (R-02 a) ou como tarefa agendada no desktop (R-02 b), com saída em branch `claude/` para sua revisão | §11 (fase 5); R-02 | lido |
| A19 | Hierarquia de fontes primárias acima de SEO e buscas curtas antes de estreitas no brief do pesquisador | §5.1; skill `pesquisador-de-mercado` | lido |

### Descartar

| # | O que descartar | Muda | Base |
|---|---|---|---|
| D1 | Agent teams e qualquer negociação entre pares | Princípio 5; §6 | lido + resumo |
| D2 | Debate em várias rodadas, ou réplica entre advogado e cético | §5 (estágio 3); mantém R-09 | resumo |
| D3 | Subagente que cria subagente (mais de um nível abaixo da sessão principal) | Princípio 5; §6 | lido + resumo (preprint fraco) |
| D4 | Fork (`/subtask`) em qualquer papel avaliador | §6.1 | lido |
| D5 | Estrategista de oferta e construtor como subagentes isolados | §6.1 (ver A2) | inferência sobre fontes lidas |
| D6 | Campos de status no frontmatter Markdown | §7 | lido |
| D7 | Auto memory ou `memory:` de subagente como estado, e qualquer memória nos avaliadores | §7; §6.1 | lido |
| D8 | Maquinaria de reset de contexto entre estágios, e "resumos compactos entre estágios" como mitigação principal (substituídos por arquivos e ponteiros) | §10 | lido |
| D9 | Paráfrase do orquestrador como entrada do juiz ou de qualquer avaliador | §6.1; R-11 | lido + resumo |
| D10 | Empacotar o harness como plugin nesta fase | §6; D-001 | lido |
| D11 | `/loop` para operação recorrente | §11 (fase 5) | lido |

### Testar

| # | O que testar | Muda | Critério de decisão |
|---|---|---|---|
| T1 | Trio advogado + cético + juiz × juiz único cético e calibrado (rubrica + exemplos) × juiz + cético, com orçamento igual, nos casos de R-07 | Princípio 5; §5 (estágio 3); §9; confirmação do trio em `revisao-pendente.md` | Acurácia, consistência entre execuções repetidas (pass^k) e custo; o trio fica só se ganhar |
| T2 | Juiz holístico único × juízes isolados por dimensão (a Anthropic recomendou o primeiro em 2025 e o segundo em 2026) | Formato do veredito; §9 | Concordância com o seu julgamento |
| T3 | Juiz como subagente (R-11) × `claude -p --bare --json-schema` em diretório neutro | R-11; §6.1 | Vazamento medido por teste, custo e atrito de uso |
| T4 | Forma de orquestração: dynamic workflow × Python + `claude -p`; inclui verificar se agentes de workflow aceitam tipos nomeados com `omitClaudeMd` (o post da Anthropic sobre workflows não foi lido) | Princípio 4; §6 | Isolamento verificável, custo registrado, retomada, teste offline |
| T5 | Kill barato com 1 pesquisador × 3 em paralelo (um por alegação) | §5 (estágio 2); princípio 8 | Mesma taxa de acerto com menos tokens |
| T6 | Batedores num modelo mais barato (A-05) | §10; A-05 | Recall de sinais e qualidade de fonte iguais |
| T7 | Curva de orçamento: teto proposto × metade × dobro em `/radar` e `/validar` | Princípio 8 | Ponto em que o ganho marginal para |
| T8 | Laço avaliador-otimizador com uma rodada extra × nenhuma | Princípio 6; §5 | Ganho de acurácia contra tempo até o teste |
| T9 | Cota fixa de buscas por evidência contrária no brief do pesquisador | Princípio 1; §5 | Equilíbrio do dossiê em casos com desfecho conhecido |
| T10 | Hook PreToolUse na ferramenta `Agent` que rejeita brief de avaliador fora do template ou com troca de `model` | R-11; §6 (guarda-corpos) | Bloqueios indevidos × vazamentos evitados |
| T11 | Convivência das skills do repo com as sincronizadas no claude.ai (disparo em dobro, seis campos nas rotinas, orçamento de listagem de 1% da janela de contexto) | A-06 | Taxa de disparo correto no `claude plugin eval` ou no skill-creator |
| T12 | MCP de busca (se R-14 o ligar) × busca nativa, uma ferramenta por tipo de subagente | A-04; R-14; §8 | Qualidade de fonte e recall por custo |
| T13 | Nova ablação a cada troca de modelo, removendo um componente por vez | §11 (ciclo); §9 | O componente sai se não pagar o próprio custo |

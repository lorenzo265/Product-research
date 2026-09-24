# Para revisar

> Decisões e descobertas registradas enquanto você dormia (a partir de 2026-09-24).
> Ordem: urgência primeiro, depois impacto. Cada item diz o que eu decidi por padrão,
> por quê, e o que muda se você discordar. Responda só nos que quiser mudar.

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
Domínios mínimos para (a): `servicodados.ibge.gov.br`, `queridodiario.ok.org.br`,
`dadosabertos.rfb.gov.br`, `hn.algolia.com`, `www.reddit.com`, `api.mercadolibre.com`,
`export.arxiv.org`, `arxiv.org`.

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
**Meu padrão:** o pacote M marca ticket abaixo de ~R$150/mês como risco alto de churn.
Para produto centrado em IA, pede ticket de ~R$250/mês ou mais, ou dependência real
do fluxo de trabalho do cliente. Na prática isso empurra a trilha M para B2B.
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
- o veredito pede P(sucesso) e P(fracasso) separadamente, para detectar viés
  otimista;
- a probabilidade parte da taxa-base, com ajustes nomeados.

Isso muda a Fase 6 do `analista-imparcial`.

### R-07 · Evals: casos famosos estão "contaminados"
**Descoberta:** testar o harness com empresas famosas que morreram ou deram certo não
vale, porque o modelo já sabe o desfecho.
**Meu padrão:** casos de eval com empresas obscuras ou anonimizadas e dossiê
congelado com data. Antes de usar um caso, pergunta-se ao modelo o que aconteceu com
a empresa, para checar se ele já sabe.
**Pedido:** suas teses antigas (Arkan e outras) são o melhor material de eval que
existe, porque o modelo não as conhece. Se tiver `fatos.json`, `vereditos.json` ou
documentos de tese, suba no repo (item A-07 de `decisoes.md`).

## Médio impacto

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
- o juiz recebe os dois memorandos **no mesmo turno**, sem rótulos e com tamanho
  igualado;
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

- **Advogado + cético isolados + juiz:** debate com argumentos opostos subiu a
  acurácia de juízes não especialistas de 48% para 76% (Khan et al., 2024). Mas debate
  em **várias rodadas** não supera votação simples. **Padrão:** uma rodada só, sem
  réplica.
- **Escrita centralizada na sessão principal:** a Cognition revisou a posição dela em
  2026 para "escritas num fio só; agentes extras contribuem inteligência, não ações".
  É exatamente o nosso desenho.
- **Multiagente só onde a tarefa é paralelizável:** +81% em tarefas paralelizáveis e
  −39% a −70% em sequenciais (Google, preprint de dez/2025). Radar e coleta ficam em
  paralelo; validação fica sequencial num fio só.

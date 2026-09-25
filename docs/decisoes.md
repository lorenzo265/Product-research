# Registro de Decisões

Cada decisão registra o contexto, o que foi decidido e o que a faria mudar.
Decisões nunca são apagadas: quando mudam, a antiga fica com status `substituída`.

## Tomadas

### D-001 · Runtime: Claude Code + scripts Python · 2026-09-24 · ativa
O harness vive neste repo: CLAUDE.md, subagentes, skills e comandos do Claude Code;
scripts Python para coleta, validação e métricas; estado em arquivos versionados.
**Alternativas descartadas:** app próprio com Agent SDK (mais código para manter);
só skills no claude.ai (sem testes automatizados nem estado versionado).
**Mudaria se:** precisarmos rodar 24/7 sem sessão aberta em volume que as rotinas
agendadas não atendam.

### D-002 · Mercado: Brasil + arbitragem · 2026-09-24 · ativa
Fontes, preços e regulação brasileiros como base; lente de arbitragem para produtos
validados lá fora sem equivalente forte aqui. Número estrangeiro entra sempre rotulado
com geografia e transferibilidade.

### D-003 · Três trilhas: G, M, S · 2026-09-24 · ativa
G (grandes problemas, SaaS B2B vertical), M (micro-SaaS / nicho), S (serviço com IA).
Foco atual em M e S; G mantida para grandes projetos. Cada trilha tem pacote de
critérios e piso de ambição próprios.

### D-004 · Núcleo reaproveita as skills existentes · 2026-09-24 · ativa
`pesquisador-de-mercado` (coleta) e `analista-imparcial` (julgamento) são a base.
Na Fase 3 entram no repo, versionadas e com evals, e ganham os pacotes das trilhas
M e S e as lentes novas.

### D-005 · Estado em JSONL + Markdown · 2026-09-24 · ativa
`data/*.jsonl` para registros (fatos, sinais, vereditos, testes) e uma pasta por
oportunidade com `cartao.md`. **Mudaria se:** o volume tornar busca e agregação lentas
(então SQLite).

### D-006 · Fatia vertical primeiro · 2026-09-24 · ativa
A Fase 3 entrega uma oportunidade real atravessando radar → cartão → kill barato →
veredito antes de construir o funil completo.

### D-007 · Pisos de ambição por trilha · 2026-09-24 · ativa
G: K1 atual (R$16,7M ARR capturável). M: caminho plausível a ~R$30k MRR em 18 meses.
S: ~R$15k/mês de receita com margem. Pisos são critério de rejeição (K1 de cada
trilha), nunca filtro de descoberta. Resolve A-01.

## Tomadas por Claude na noite de 24/09, aguardando sua revisão

Cada uma tem o item correspondente em [`revisao-pendente.md`](revisao-pendente.md). Se
você discordar, ela vira `substituída`.

### D-008 · O juiz é um subagente isolado; a sessão principal não julga · provisória (R-11)
Juiz sem CLAUDE.md, só leitura, modelo fixado; entrada gerada por
`python3 -m harness pacote-juiz`, com memorandos A/B em ordem sorteada e mesmo teto.

### D-009 · Protocolo de julgamento revisado · provisória (R-06, R-09)
- Tese como proposta de terceiro.
- Evidência antes do nível.
- Taxa-base como campo, com ajustes nomeados em log-odds.
- Probabilidade encolhida em direção à taxa-base (fator 0,7) até haver calibração.
- Uma rodada de memorandos, sem réplica.
- Brier acumulado com intervalo, e ajuste de réguas só depois de ~100 previsões.
- Sai "ônus da prova é do GO".

### D-010 · Evidência com trecho literal e verificação por leitura · provisória (R-05)
Fato documentado exige `citacao_literal` e registra `leitura`. O verificador lê a
página; `conferir-trecho` confere por código.

### D-011 · Pacotes M e S e réguas de teste revisadas · provisória (R-03, R-04, R-13, R-16, R-17, R-18)
Pacotes em `.claude/skills/metodo-julgamento/references/`, com:
- escada ordinal com degrau de reputação;
- deflator só para preço;
- testes SPRT e Beta-Binomial.

### D-012 · Escritor único do estado é a CLI; edição direta bloqueada por hook · ativa
Resolve concorrência entre subagentes (trava de arquivo) e mantém o estado sempre
válido.

### D-013 · Orquestração por skills + subagentes, com passos determinísticos na CLI · provisória (R-20)
Em vez de scripts Python chamando `claude -p` para cada etapa. A comparação entre as duas
formas fica como teste.

### D-014 · Skills do repo com nomes próprios · ativa (resolve A-06)
`metodo-pesquisa` e `metodo-julgamento` (não visíveis como comando). O CLAUDE.md
manda usar os comandos do repo, e não as versões sincronizadas do claude.ai.

### D-015 · Leitor alternativo (r.jina.ai) para página pública que recusa o curl · ativa (resolve R-27) · 2026-09-25
Quando uma página pública, sem login nem paywall, recusa o `curl` do harness (openai.com e
planalto.gov.br no radar de 25/09), o coletor pode lê-la via `r.jina.ai`, e o
`conferir-trecho` tenta esse caminho só depois que o `curl` direto falha, declarando no
resultado que a leitura veio dele. Login, paywall e desafio anti-bot continuam fora.
**Decidido por:** usuário, em 25/09 ("se der certo, pode ser").
**Mudaria se:** o leitor alterar o texto da página (então a conferência por ele deixa de
valer) ou se o site proibir o acesso nos termos de uso.

## Em aberto

| # | Pergunta | Quem decide | Quando |
|---|---|---|---|
| A-02 | Capacidade disponível: horas por semana e caixa para testes (anúncios, ferramentas, domínios) | Você | Antes do desenho de cunhas |
| A-03 | Stack padrão de MVP (M) e de entrega de serviço (S) | Você | Fase 4 |
| A-04 | APIs de busca via MCP × busca nativa (R-14) | Você; depois, sonda com 30–50 consultas em português | Fase 3 |
| A-05 | Modelo por papel: coletores em Sonnet por padrão; juiz e memorandos em Opus fixado | Evals | Fase 3 |
| A-07 | Existem `fatos.json`, `vereditos.json` ou teses antigas (Arkan e outras) para importar como dados iniciais e casos de eval? | Você | Fase 3 |
| A-08 | Rede do ambiente de nuvem: liberar domínios ou rodar coleta na sua máquina (R-02) | Você | Antes dos coletores |

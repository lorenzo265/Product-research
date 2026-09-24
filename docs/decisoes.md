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

## Em aberto

| # | Pergunta | Quem decide | Quando |
|---|---|---|---|
| A-02 | Capacidade disponível: horas por semana e caixa para testes (anúncios, ferramentas, domínios) | Você | Antes do desenho de cunhas |
| A-03 | Stack padrão de MVP (M) e de entrega de serviço (S) | Você + Fase 2 | Fase 4 |
| A-04 | APIs de busca pagas via MCP × busca nativa | Fase 2, fluxo E | Fase 3 |
| A-05 | Modelo por papel (batedores mais baratos?) | Evals | Fase 3 |
| A-06 | Como as skills do repo convivem com as versões sincronizadas do claude.ai sem disparar em dobro | Fase 3 | Fase 3 |
| A-07 | Existem `fatos.json`, `vereditos.json` ou teses antigas (Arkan e outras) para importar como dados iniciais e casos de eval? | Você | Fase 3 |

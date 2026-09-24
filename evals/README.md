# Evals do harness

Como saber se o harness está melhorando ou piorando a cada mudança. O desenho vem do
relatório `research/Evals para harness de agentes.md`. Resumo: nos primeiros meses, o
sinal vem de **invariantes e consistência**, não de acurácia, porque o desfecho real das
oportunidades demora meses. Até haver centenas de previsões resolvidas, o harness pode
provar que é estável, coerente e imune à convicção de quem pergunta, mas ainda não que
acerta.

## Famílias

| # | Família | O que pega | Como roda | Custo | Estado |
|---|---|---|---|---|---|
| E0 | Integridade do estado | JSONL fora do schema, referência quebrada, fato sem trecho, p fora da faixa | `python3 -m pytest` + hooks | zero | ✅ |
| E1 | Invariantes do protocolo | Juiz ou memorando com CLAUDE.md, juiz com ferramenta além de leitura, agente que cria agentes, entrada do juiz com arquivo fora da lista | `tests/unit/test_invariantes.py`, `tests/integration/test_julgamento.py` | zero | ✅ parcial (falta checar transcrições reais) |
| E2 | Citação, camada de código | Trecho literal que não está na página | `python3 -m harness conferir-trecho` | zero | ✅ (precisa de rede) |
| E3 | Roteamento | Pedido do usuário indo para o comando errado; disparo em dobro com as skills sincronizadas | a construir: 10 pedidos que devem disparar + 10 quase-acertos, 3 execuções cada | baixo | ⏳ |
| E4 | Bajulação | Veredito que muda com a convicção do fundador | `python3 -m evals.bajulacao` | ~US$0,70 por execução do juiz | ✅ 1 caso sintético |
| E5 | Consistência sem gabarito | P(A)+P(não A) longe de 1; paráfrase que muda P | a construir | médio | ⏳ |
| E6 | Citação, juiz | Fonte que não sustenta a alegação | a construir; o juiz binário precisa de ~100 rótulos seus | baixo em tokens, alto em rótulos | ⏳ |
| E7 | Backtest | Matar vencedor, poupar cadáver | a construir: casos obscuros ou anonimizados com dossiê congelado e datado | alto na curadoria | ⏳ |
| E8 | Neutralidade da coleta | Pesquisador que acha o que a pergunta sugere | a construir; precisa de rede | alto | ⏳ |

## Como rodar

```bash
python3 -m pytest                                  # E0, E1: grátis, a cada mudança
python3 -m evals.bajulacao --so-preparar           # monta os diretórios, sem custo
python3 -m evals.bajulacao --repeticoes 3          # E4 completo: 3 braços × 3 × casos
```

Os resultados ficam em `evals/resultados/`. O juiz roda num diretório temporário que
contém só o que a entrada dele lista (sem CLAUDE.md, sem git, sem conversa), com o prompt,
o modelo e o esforço de `.claude/agents/juiz.md`.

## Casos

`evals/casos/<nome>/` tem `contrato.json`, `fatos.jsonl`, `dossie-*.md` e
`memorandos/`. É um dossiê congelado: ele não muda depois de criado, o que elimina
vazamento de informação futura e permite rodar tudo offline.

- `sintetico-conciliacao-contabil`: caso sintético de evidência mista (trilha M).
  Entidades e URLs são fictícias.

Próximos casos: as suas teses antigas (A-07), que o modelo não conhece, e os dossiês
congelados das primeiras execuções reais do harness.

## Quando rodar os pagos

- A suíte rápida (E3 + E4 com 1 repetição) quando mudar skill, agente, comando ou
  CLAUDE.md.
- A suíte completa quando mudar o juiz, o modelo ou a versão do Claude Code.
- A análise de erros (ler 5 execuções reais e anotar o primeiro erro de cada) todo mês,
  junto com `/calibrar`.

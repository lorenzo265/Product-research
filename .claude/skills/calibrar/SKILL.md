---
name: calibrar
description: Revisão de calibração do harness. Resolve previsões vencidas com o usuário, calcula Brier acumulado com intervalo e calibração por faixa, e registra lições. Use no fechamento do mês ou quando o usuário perguntar se o harness está acertando.
---

# /calibrar

1. `python3 -m harness calibracao` lista as previsões vencidas sem resultado.
2. Para cada uma, pergunte ao usuário o que aconteceu (ou busque, se for observável) e
   atualize o veredito: o array `previsoes` inteiro, com `resultado` e `resolvido_em`
   preenchidos, via `python3 -m harness atualizar veredito v-... '{"previsoes": [...]}' --motivo "resolução"`.
3. Rode de novo `python3 -m harness calibracao` (e `--trilha M` / `S` / `G`).
4. Leia o resultado com a régua certa:
   - abaixo de ~100 previsões resolvidas, o Brier é descritivo; **não ajuste réguas por
     ele**;
   - olhe a calibração por faixa: se "PROVAVEL" acontece bem menos que 65–90%, registre
     como lição a observar;
   - skill score negativo significa que prever a frequência média teria acertado mais.
5. Registre as lições do mês em `docs/licoes.md` (data, observação, o que muda quando
   houver amostra).
6. Faça também a análise de erros: leia 5 execuções recentes (dossiês, memorandos,
   vereditos) e anote o primeiro erro de cada uma. É daí que nascem os próximos evals.

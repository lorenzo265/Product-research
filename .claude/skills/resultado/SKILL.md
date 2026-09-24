---
name: resultado
description: Registra o resultado de um teste com comprador do harness, aplica a regra de decisão escrita antes do teste e resolve as previsões ligadas a ele. Use quando o usuário contar como foi um teste ("3 de 40 pediram proposta", "ninguém pagou o depósito", "fechei 1 contrato").
argument-hint: "t-AAAA-NNNN <amostra> <sucessos>"
---

# /resultado

1. **Leia o Test Card** (`python3 -m harness obter teste t-...`).
2. **Registre o resultado:**
   `python3 -m harness atualizar teste t-... '{"resultado": {"amostra": N, "sucessos": K, "observacoes": "..."}, "fim": "<data>"}' --motivo "resultado informado pelo usuário"`.
3. **Aplique a regra gravada**, sem mudá-la: recalcule a tabela com os mesmos parâmetros
   (`python3 -m harness regra-teste ...`) e leia o GO/KILL para o N observado. Se o N
   ficou abaixo do planejado e a tabela ainda não decide, diga isso: é "sem decisão",
   não GO.
4. **Proponha a decisão** (GO / ITERAR / KILL) e peça a confirmação do usuário. Com a
   confirmação, grave `decisao` e `decidido_em` no teste.
5. **Resolva previsões:** a `previsao_p_go` do teste resolve agora. Se alguma previsão de
   veredito dependia deste teste, atualize o veredito com o resultado e `resolvido_em`.
6. **Cartão:** registre a mudança de estágio e o próximo passo (novo degrau, construir,
   reformular ou cadáver com motivo).

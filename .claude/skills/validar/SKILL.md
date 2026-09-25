---
name: validar
description: Roda a validação de mesa completa de uma oportunidade do harness que passou no kill barato. Sequência dossiê → verificação de citações → memorandos a favor e contra → juiz isolado → veredito registrado com probabilidades e previsões. Use quando o usuário pedir para aprofundar, validar, analisar ou dar veredito sobre uma OP.
argument-hint: "OP-NNNN"
---

# /validar

Objetivo: um veredito calibrado, por dimensão, feito por um juiz que não viu a convicção
de ninguém. Siga as etapas 2 a 6 do `metodo-julgamento`. Você orquestra; não julga.

## Pré-requisitos

- `contrato.json` gravado (senão, rode `/kill` antes).
- Kill barato com `GO`, ou pedido explícito do usuário para validar mesmo assim
  (registre isso no histórico do cartão).

## Passos e orçamento

| Passo | Quem | Orçamento |
|---|---|---|
| 1. Dossiê | `pesquisador`, modo `dossie` | até ~40 buscas |
| 2. Verificação | `verificador` | só leitura de fontes |
| 3. Memorandos | `memorando` ×2, na mesma mensagem | sem busca |
| 4. Juiz | `juiz` | sem busca |

1. **Dossiê.** Lance o `pesquisador` em modo `dossie` com a oportunidade. Ao voltar, rode
   `python3 -m harness validar` e corrija erros.
2. **Verificação.** Lance o `verificador` com a oportunidade, antes dos memorandos, para
   que eles já leiam o status de cada fato. Na OP-0001, 4 de 9 fatos vindos de resumo de
   busca estavam errados, e os memorandos escritos antes da verificação se apoiaram
   neles.
3. **Memorandos.** Lance dois subagentes `memorando` na mesma mensagem. A tarefa de cada
   um é só: "Pasta: oportunidades/<pasta>. Direção: a favor." e "Pasta:
   oportunidades/<pasta>. Direção: contra.". Nada além disso.
4. **Juiz.** Rode `python3 -m harness pacote-juiz OP-xxxx`. Passe ao subagente `juiz`
   exatamente a mensagem impressa, sem acrescentar nada. Se o comando avisar que um
   memorando passou de 1.500 palavras, peça a esse `memorando` que reescreva dentro do
   teto e gere o pacote de novo: o corte automático tira o fim do texto só de um lado.
5. **Registro.** Salve a resposta do juiz num arquivo
   (`oportunidades/<pasta>/juiz/<rodada>/resposta.json`) e rode
   `python3 -m harness registrar-veredito OP-xxxx - < <arquivo>`. Se o schema recusar,
   devolva o erro ao juiz na mesma conversa e peça o JSON corrigido.

   **Fato corrigido depois do veredito.** Se uma verificação posterior corrigir ou
   contradisser um fato que o veredito cita, refaça os passos 3 a 5 com os fatos
   corrigidos e registre com
   `registrar-veredito OP-xxxx - --substitui v-AAAA-NNNN --motivo "<fato e correção>" < <arquivo>`
   (o `-` vem logo depois do id).
   A regra vale nos dois sentidos, seja a correção a favor ou contra a tese, e não
   depende do resultado: refazer porque o veredito desagradou é pescar veredito. O
   veredito antigo fica gravado e sai da calibração.
6. **Cartão.** Atualize `estagio` para `veredito` e `proximo_passo`: se a recomendação for
   GO, o próximo passo é `/teste`; se ITERAR, o que precisa ser resolvido; se KILL, a
   decisão do usuário.
7. **Apresente**, nesta ordem:
   - recomendação e, ao lado, a objeção mais forte que sobreviveu;
   - perfil por dimensão (nível, faixa e p), com as travas;
   - p_sucesso (e a bruta do juiz) contra a taxa-base;
   - hipóteses rivais com probabilidades;
   - o que mudaria o veredito;
   - próximo teste com comprador.

   Termine perguntando GO / ITERAR / KILL: a decisão é do usuário.

Rode este comando sozinho na sessão: ele consome boa parte do teto de buscas.

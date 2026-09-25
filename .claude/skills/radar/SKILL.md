---
name: radar
description: Varre setores, temas ou lentes de sinal em busca de dores com dinheiro mal servido e grava sinais no harness. Use quando o usuário pedir oportunidades, ideias, "o que existe em X", um panorama de opções, ou rodar o radar semanal.
argument-hint: "[setor ou tema] [lente 1-11] [trilha G|M|S]"
---

# /radar

Objetivo: transformar um escopo em sinais registrados e em candidatos a oportunidade,
sem julgar nenhum deles.

## Passos

1. **Escopo.** Leia o pedido: setor/tema, lentes, trilha. Sem lentes definidas, use por
   padrão (4 batedores):
   - trilhas M e S: lentes 5 e 8 juntas (a 8 cruza tarefas manuais da 5 com o que a IA
     passou a fazer), 10, 11 e 7;
   - trilha G: lentes 1, 2, 4 e 6 (a 3 entra junto com a 1).
   Se o pedido for amplo, sem setor ("me dá opções"), escolha até 4 lentes que cubram
   trilhas diferentes e prefira as lentes guiadas por fonte (4, 5/8, 10, 11, 7), que não
   dependem de um setor escolhido. Diga ao usuário quais temas já têm oportunidade aberta
   (`/portfolio`) para os batedores não gastarem busca neles.
2. **Rede.** Teste as fontes das lentes escolhidas com um `curl` curto (PNCP, 99Freelas,
   Gupy, yc-oss...). Fonte fora do ar vira lacuna declarada, e a lente roda só por busca
   ou é trocada. Não conte fonte inacessível como ausência de sinal.
3. **Batedores em paralelo.** Lance até 4 subagentes `batedor` na mesma mensagem, um por
   lente (ou por fonte), cada um com lente, escopo, trilha e os temas já cobertos. Cada
   um gasta ~5–12 buscas. A busca nativa tem teto de 200 por sessão, compartilhado: rode
   um comando pesado por sessão.
4. **Validar.** `python3 -m harness validar`. Corrija erros antes de seguir.
5. **Agrupar.** `python3 -m harness sinais` lista os sinais novos com as contagens
   mecânicas (cifra, recorrência, fatos, fatos com leitura integral e conferidos). Agrupe
   os que falam da mesma dor para o mesmo comprador e ordene os grupos por essas
   contagens e por quantas lentes dispararam. Isso não é veredito; é fila de trabalho.
6. **Relatório.** Escreva `radar/AAAA-MM-DD-<escopo>.md` com: escopo e lentes, tabela de
   grupos, uma linha por sinal, "o que procurei e não encontrei", lacunas e bloqueios
   (fonte fora do ar, orçamento de busca), e o número de buscas. Registro factual, como
   num dossiê: sem "promissor", sem ranking por potencial.
7. **Apresentar.** Tabela: grupo · trilha provável · lentes · cifra (sim/não) · ids dos
   sinais · próximo passo sugerido. Pergunte quais grupos viram oportunidade, ou abra
   os que o usuário já pediu com `/oportunidade`.

## Limites

Sem ranking por "potencial", sem recomendar entrar ou não: isso vem depois do kill
barato e do juiz. Sinais fracos ficam registrados; descartar é decisão explícita
(`python3 -m harness atualizar sinal <id> '{"status": "descartado"}' --motivo "..."`).

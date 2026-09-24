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
   padrão:
   - trilhas M e S: lentes 5, 8, 10, 11 e 7;
   - trilha G: lentes 1, 2, 3, 4 e 6.
   Se o pedido for amplo ("me dá opções"), escolha até 4 lentes que cubram trilhas
   diferentes.
2. **Batedores em paralelo.** Lance até 4 subagentes `batedor` na mesma mensagem, um por
   lente (ou por fonte), cada um com lente, escopo e trilha. Cada um gasta ~5–10 buscas.
   A busca nativa tem teto de 200 por sessão, compartilhado: rode um comando pesado por
   sessão.
3. **Validar.** `python3 -m harness validar`. Corrija erros antes de seguir.
4. **Agrupar.** Leia os sinais novos em `data/sinais.jsonl` e agrupe os que falam da
   mesma dor para o mesmo comprador. Ordene os grupos por força de evidência, de forma
   mecânica: tem cifra? tem recorrência? quantas lentes dispararam? quantos fatos com
   leitura integral? Isso não é veredito; é fila de trabalho.
5. **Apresentar.** Tabela: grupo · trilha provável · lentes · cifra (sim/não) · ids dos
   sinais · próximo passo sugerido. Pergunte quais grupos viram oportunidade, ou abra
   os que o usuário já pediu com `/oportunidade`.

## Limites

Sem ranking por "potencial", sem recomendar entrar ou não: isso vem depois do kill
barato e do juiz. Sinais fracos ficam registrados; descartar é decisão explícita
(`python3 -m harness atualizar sinal <id> '{"status": "descartado"}' --motivo "..."`).

---
name: oportunidade
description: Abre um cartão de oportunidade no harness a partir de uma ideia livre do usuário ou de sinais do radar, com a pergunta neutralizada e a trilha (G, M ou S). Use quando o usuário disser "tive uma ideia", "e se eu fizesse X", "abre uma oportunidade", ou escolher grupos de sinais do radar.
argument-hint: "[ideia em texto livre | ids de sinais s-AAAA-NNNN]"
---

# /oportunidade

Objetivo: registrar a oportunidade de forma que ninguém depois dela (pesquisador,
memorandos, juiz) herde a empolgação de quem a trouxe.

## Passos

1. **Neutralize.** Reescreva a ideia como pergunta aberta, em terceira pessoa, sem
   convicção, e mostre ao usuário. Exemplo: "tenho certeza que um app de agendamento
   para barbearias vai bombar" → "Barbearias de 2–10 cadeiras pagam R$X/mês por
   agendamento com cobrança antecipada?".
2. **Trilha.** Proponha G, M ou S com uma linha de motivo, conforme
   `docs/01-arquitetura.md` (seção 4). Se ficar entre duas, pergunte. Uma ideia pode
   entrar como S (serviço) e subir para M depois.
3. **Crie o cartão:**

   ```bash
   python3 -m harness novo-cartao '{"titulo": "...", "trilha": "M",
     "estagio": "oportunidade", "status": "ativa", "origem": "ideia do usuário",
     "pergunta_neutralizada": "...", "quem_sofre": "...", "quem_paga": "...",
     "workaround": "...", "custo_workaround": null, "lentes": [],
     "sinais": [], "travas": [], "proximo_passo": "kill barato",
     "revisar_em": "<hoje + 14 dias>"}'
   ```

   Campos desconhecidos ficam como "a verificar", nunca como suposição apresentada como
   fato.
4. **Ligue os sinais**, se vieram do radar: inclua os ids em `sinais` e marque cada
   sinal como agrupado
   (`python3 -m harness atualizar sinal <id> '{"status": "agrupado", "oportunidade": "OP-xxxx"}' --motivo "agrupado em OP-xxxx"`).
5. **Material do proponente.** Se a ideia chegar com documento próprio (SDD, pitch,
   planilha), guarde o arquivo fora do git (`cache/entrada/`) e escreva em
   `oportunidades/<pasta>/alegacoes-do-proponente.md` só as **alegações verificáveis**
   que ele faz (números, preços, normas, tamanho de mercado, concorrentes), cada uma
   com a fonte que o documento cita, como pista. Nenhum subagente lê o documento: ele
   carrega a convicção de quem o escreveu. O pesquisador verifica as alegações na fonte
   original; o que ele não confirmar não vira fato.
6. **Próximo passo:** ofereça `/kill OP-xxxx`. O kill barato é o estágio mais barato e
   mata a maioria das ideias ruins.

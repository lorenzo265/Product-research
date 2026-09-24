---
name: kill
description: Roda o kill barato de uma oportunidade do harness. Grava o contrato de validação (pergunta neutra, premissas, condições-barreira, taxa-base, teto e as 3 alegações mais baratas de falsificar), manda o pesquisador verificá-las e aplica a regra "2 ou mais caem → reformular". Use depois do /oportunidade ou quando o usuário pedir para testar rápido se uma ideia para em pé.
argument-hint: "OP-NNNN"
---

# /kill

Objetivo: matar cedo e barato o que não para em pé, antes de gastar com dossiê completo.
Siga as etapas 0 e 1 do `metodo-julgamento`.

## Passos

1. **Leia o cartão** (`python3 -m harness obter cartao OP-xxxx`) e o pacote da trilha em
   `.claude/skills/metodo-julgamento/references/`.
2. **Enquadre** (etapa 0): tese de terceiro, premissas críticas, condições-barreira da
   menos para a mais crível, taxa-base com classe de referência, conta do teto da
   trilha.
3. **Escolha as 3 alegações** mais baratas de falsificar com maior dano se falsas. Boas
   alegações são factuais e checáveis por busca: "existe ferramenta X que já faz Y por
   menos de R$Z", "o comprador W tem orçamento para isso", "a norma N obriga até a data
   D".
4. **Grave o contrato** (`python3 -m harness contrato '{...}'`). Mostre ao usuário as 3
   alegações e a taxa-base. O contrato não muda depois.
5. **Atualize o estágio:**
   `python3 -m harness atualizar cartao OP-xxxx '{"estagio": "kill_barato"}' --motivo "contrato gravado"`.
6. **Verifique:** lance um subagente `pesquisador` em modo `verificacao` com a
   oportunidade. Orçamento: ~15 buscas.
7. **Aplique a regra** sobre os status devolvidos no `dossie-kill-barato.md`:
   - 2 ou mais caíram → `REFORMULAR`, ou `KILL` se não houver reformulação plausível;
   - 0 ou 1 caiu → `GO` (segue para `/validar`).
   "Não encontrada" não é "caiu": conta como lacuna e vira pauta da validação.
8. **Registre** o veredito do kill barato:

   ```bash
   python3 -m harness registrar-veredito OP-xxxx '{"trilha": "M", "modo": "kill_barato",
     "pergunta_neutralizada": "...", "base_rate": {"p": 0.1, "classe_referencia": "..."},
     "alegacoes_kill_barato": [{"alegacao": "...", "resultado": "caiu", "fatos": ["f-..."]}],
     "dimensoes": {}, "travas": [], "hipoteses_rivais": {}, "recomendacao": "GO",
     "previsoes": []}'
   ```

   Depois atualize `proximo_passo` e `estagio` no cartão (`veredito` se passou).
9. **Apresente:** o que caiu, o que ficou de pé, o que não foi encontrado, e a
   recomendação pela regra. A decisão de matar é do usuário: não marque o cartão como
   cadáver sem a confirmação dele (depois dela:
   `'{"status": "cadaver", "motivo_morte": "..."}'`).

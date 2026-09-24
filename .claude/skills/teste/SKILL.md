---
name: teste
description: Desenha o próximo teste com comprador de uma oportunidade do harness. Monta o Test Card com hipótese, degrau da escada, p0/p1, N máximo, regra de decisão calculada antes dos dados e previsão do resultado, e prepara o material (roteiro de entrevista, mensagens, texto de página). Use depois de um veredito GO ou quando o usuário pedir para testar com clientes reais.
argument-hint: "OP-NNNN"
---

# /teste

Objetivo: o teste mais barato que sobe um degrau da escada de evidência, com a régua
escrita antes do dado. Regras em
`.claude/skills/metodo-julgamento/references/teste-com-comprador.md` e no pacote da
trilha.

## Passos

1. **Leia** o cartão, o último veredito (travas, `mudaria`, previsões) e o pacote da
   trilha. O teste deve atacar a trava ou a dimensão mais incerta.
2. **Escolha o degrau** que o teste alcança e o formato:
   - M: pré-venda com reembolso automático ou depósito (lista de e-mail só autoriza o
     degrau seguinte);
   - S: diagnóstico ou setup pago oferecido a decisores do ICP (T1);
   - G: sequência de degraus com dinheiro de decisores com orçamento.
3. **Calcule a regra antes do teste:**
   - com tráfego: `python3 -m harness regra-teste sequencial --p0 <p0> --p1 <p1>`
   - com poucas contas: `python3 -m harness regra-teste bayes --alvo <taxa> --n-max <N>`
   Cole a tabela no Test Card.
4. **Pré-mortem e pré-parada** em duas linhas cada, e sua previsão `previsao_p_go`.
5. **Grave o Test Card:**
   `python3 -m harness adicionar teste '{...}'` com `oportunidade`, `degrau`, `hipotese`,
   `experimento`, `metrica`, `regra_decisao` (tipo, go, kill, parametros com p0/p1 ou
   alvo/N), `canal`, `publico`, `amostra_planejada`, `dias_max`, `criado_em`,
   `previsao_p_go`, `resultado: null`, `decisao: null`.
6. **Prepare o material** em `oportunidades/<pasta>/testes/<id-do-teste>/`:
   - roteiro de conversa (Mom Test: só fatos passados, termina pedindo compromisso);
   - mensagens de abordagem;
   - texto da página e da oferta, com termos, reembolso e aviso de privacidade.
7. **Atualize o cartão** (`estagio: teste`, `testes`, `proximo_passo`) e diga ao usuário
   exatamente o que ele precisa executar e quando voltar com `/resultado`.

O harness não envia mensagens, não publica páginas e não cobra: quem executa é o
usuário.

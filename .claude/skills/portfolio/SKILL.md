---
name: portfolio
description: Mostra o painel de todas as oportunidades do harness por trilha e estágio, com pendências (revisões vencidas, testes sem decisão, previsões a resolver) e sugere o foco da semana. Use quando o usuário perguntar "o que eu faço agora?", "como está o portfólio?", pedir o comitê semanal ou quiser escolher entre opções.
---

# /portfolio

1. Rode `python3 -m harness validar` e depois `python3 -m harness portfolio`.
2. Mostre o painel.
3. **Foco da semana**, por regra explícita, nesta ordem:
   1. pendências que bloqueiam decisão (teste com resultado a registrar, previsão
      vencida);
   2. oportunidades com veredito GO ainda sem teste com comprador (viés para teste);
   3. testes em andamento perto do prazo;
   4. kill barato das oportunidades novas.
   Proponha no máximo 3 ações, cada uma com o comando que a executa.
4. Se o usuário quiser escolher entre oportunidades, compare pelo que está registrado
   (trilha, estágio, p_sucesso contra a taxa-base, travas, custo do próximo teste), sem
   gerar julgamento novo. Perfil e acessos do usuário só entram aqui, no ranqueamento
   final (camada A).

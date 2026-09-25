---
name: metodo-julgamento
description: Método de julgamento calibrado do harness de oportunidades, organizado por papel. Cobre o enquadramento (pergunta neutralizada, premissas críticas, condições-barreira, taxa-base), o contrato de validação, o kill barato e a sequência dossiê → verificação → memorandos → juiz isolado → veredito com probabilidades e registro para calibração. Use quando for validar uma tese ou oportunidade, rodar o kill barato, preparar o juiz ou registrar um veredito neste repositório. Os critérios de cada trilha estão em references/ (pacote-mercado para G, pacote-micro-saas para M, pacote-servico-ia para S).
user-invocable: false
---

# Método de julgamento: estrutura no lugar de retórica

O juiz do harness erra de dois jeitos documentados, e o método existe para barrar os
dois:

- **Bajulação:** concordar com a convicção de quem trouxe a ideia. O gatilho mais forte
  conhecido é o juiz ver essa convicção.
- **Negatividade performática:** quando instruído a criticar, o modelo inventa objeções
  e requisitos.

Pedir virtude ("seja imparcial", "seja cético", "use a taxa-base") tem efeito fraco ou
nulo. O que funciona é tirar o gatilho e acrescentar dado verificável. Por isso quase
tudo abaixo é operação: quem vê o quê, em que ordem, com que campos.

## Quem faz o quê

| Etapa | Quem | Vê | Produz |
|---|---|---|---|
| 0 · Enquadramento | Sessão principal (você) | A ideia como chegou | Pergunta neutra, tese de terceiro, premissas, barreiras, taxa-base |
| Contrato | Você, via CLI | O enquadramento | `contrato.json`, gravado uma vez |
| 1 · Kill barato | Subagente `pesquisador` (modo verificação) | Só as alegações | Fatos; cada alegação sustentada / caiu / não encontrada |
| 2 · Dossiê | Subagente `pesquisador` (modo dossiê) | Pergunta neutra | `dossie-*.md` + fatos |
| 3 · Verificação | Subagente `verificador` | Fatos do dossiê | Status de verificação de cada fato |
| 4 · Memorandos | Subagente `memorando`, duas vezes em paralelo | Contrato + dossiê + fatos já verificados | `memorandos/a-favor.md` e `memorandos/contra.md` |
| 5 · Juiz | Subagente `juiz`, isolado | Só a entrada gerada por `pacote-juiz` | JSON do veredito |
| 6 · Registro | Você, via CLI | O JSON do juiz | Veredito em `data/vereditos.jsonl`, cartão atualizado |

Você orquestra e apresenta, mas não julga: você viu a convicção de quem perguntou.

## Etapa 0 · Enquadramento

1. **Neutralize a pergunta.** Reescreva a hipótese como pergunta aberta, em terceira
   pessoa, sem marcadores de convicção. Neutralizar tira a convicção, não o conteúdo:
   preço, mecanismo, comprador e canal ficam como o proponente os propõe. "Tenho certeza que meu SaaS X vai funcionar"
   vira "Existe demanda paga sustentável por X no segmento Y?". Mostre a reformulação.
2. **Tese de terceiro.** Escreva a tese como "um terceiro propõe…". Enquadrar como
   tese alheia reduziu bajulação em até 64% em teste com 17 modelos.
3. **Premissas críticas.** Liste as premissas implícitas e marque as críticas.
4. **O que teria de ser verdade.** Converta a tese em condições necessárias (cliente,
   mercado, competição, capacidades, economia) e ordene das menos críveis para as mais
   críveis. As menos críveis são as condições-barreira e comandam a verificação.
5. **Taxa-base como campo.** Registre a classe de referência e o valor. Exemplos de
   prior, a refinar com dados próprios: trilha M, 15–25% dos produtos que já faturam
   chegam a R$30k de MRR algum dia e menos de 10% em 18 meses; trilha S, prior largo e
   declarado (não há taxa publicada). A taxa-base já carrega o ceticismo; não some a ela
   uma postura de "ônus da prova".
6. **Teto da trilha.** Faça a conta do teto do pacote (M: pagantes novos por mês ×
   ticket ÷ churn; S: clientes alcançáveis × ticket × margem após suas horas).

Grave o contrato antes de qualquer coleta:

```bash
python3 -m harness contrato '{"oportunidade": "OP-0003", "trilha": "M",
  "pacote": "pacote-micro-saas", "pergunta_neutralizada": "...",
  "tese_de_terceiro": "Um terceiro propõe ...", "premissas_criticas": ["..."],
  "condicoes_barreira": ["..."], "alegacoes_kill": [{"alegacao": "...",
  "dano_se_falsa": "...", "como_verificar": "..."}],
  "taxa_base": {"p": 0.1, "classe_referencia": "...", "justificativa": "..."},
  "teto": "..."}'
```

O contrato não muda depois de gravado: mover a régua depois de ver o dado é
exatamente o que ele impede.

## Etapa 1 · Kill barato

Das condições-barreira, extraia as **3 alegações mais baratas de falsificar** (maior dano
à tese se falsas × menor custo de verificar). Escreva cada uma como condição que a tese
precisa que seja verdadeira ("não existe alternativa gratuita que…", e não "já existe
alternativa gratuita que…"): assim "caiu" sempre significa dano à tese e a regra abaixo
conta certo. Elas entram no contrato. Mande o `pesquisador` verificá-las em modo
`verificacao`.

- **2 ou mais caem:** a tese volta para reformulação com o que caiu. Não rode a análise
  completa. O cartão registra o motivo; se não houver reformulação plausível, vira
  cadáver.
- **0 ou 1 cai:** siga para o dossiê.

Registre o resultado como veredito de `modo: "kill_barato"`, com `alegacoes_kill_barato`
preenchido e as dimensões que já der para avaliar.

## Etapas 2 a 5 · Da evidência ao juiz

- **Dossiê** no modo `dossie` do `metodo-pesquisa`, a partir da pergunta neutra (nunca
  da sua conversa com o usuário).
- **Verificação:** lance o `verificador` com a oportunidade, antes dos memorandos. Ele
  roda `python3 -m harness conferir-trecho --oportunidade OP-xxxx` e depois lê as fontes
  dos fatos, marcando o status de cada um.
- **Memorandos:** lance o subagente `memorando` duas vezes na mesma mensagem, uma com
  direção "a favor" e outra "contra". Cada um recebe só o caminho da pasta da
  oportunidade e a direção. Uma rodada, sem réplica: rodadas extras não melhoram o juiz.
- **Juiz:** rode `python3 -m harness pacote-juiz OP-xxxx`. O comando monta a entrada cega
  (memorandos como A e B em ordem sorteada, mesmo teto de tamanho, lista fechada de
  arquivos) e imprime a mensagem exata. Passe ao subagente `juiz` **somente essa
  mensagem**, sem acrescentar contexto, resumo ou opinião. Qualquer paráfrase sua é um
  canal de vazamento.

## Etapa 6 · Registro e apresentação

1. Grave o JSON do juiz: `python3 -m harness adicionar veredito -` (stdin). Se o schema
   recusar, devolva o erro ao juiz na mesma conversa e peça o JSON corrigido.
2. Atualize o cartão: `python3 -m harness atualizar cartao OP-xxxx '{"estagio": ...,
   "vereditos": [...], "travas": [...], "proximo_passo": "..."}' --motivo "..."`.
3. Apresente ao usuário, nesta ordem: recomendação com a objeção mais forte ao lado,
   perfil por dimensão (nível, faixa e p), travas, o que mudaria o veredito e o próximo
   teste com comprador. A decisão GO / ITERAR / KILL é do usuário.

## Depois do veredito: viés para teste

Se a tese passa, o próximo passo é um teste com comprador (comando `/teste`), não mais
pesquisa. Antes do teste, faça pre-mortem ("12 meses depois deu errado: por quê?") e
pre-parade ("3–5 anos depois deu muito certo: que decisões levaram lá?"), e registre a
previsão do resultado do teste (`previsao_p_go`). Testes resolvem em dias; são a forma
mais rápida de acumular as ~100 previsões resolvidas que a calibração precisa.

## Calibração

`python3 -m harness calibracao` mostra Brier acumulado com intervalo de confiança,
comparação com a frequência observada e calibração por faixa. Com menos de ~100
previsões resolvidas o Brier é quase só ruído: use-o para descrever, não para mudar
réguas. Só previsões registradas antes do desfecho contam; casos de backtest ficam
fora.

## Referências

- `references/formato-veredito.md`: formato e regras do veredito (usado pelo juiz).
- `references/pacote-mercado.md`: trilha G.
- `references/pacote-micro-saas.md`: trilha M.
- `references/pacote-servico-ia.md`: trilha S.
- `references/teste-com-comprador.md`: escada de evidência, Test Card e regras de
  decisão, comuns às três trilhas.

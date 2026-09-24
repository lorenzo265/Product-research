# Teste com comprador: escada, Test Card e regras de decisão

Comum às três trilhas. A estrutura tem apoio experimental: em dois conjuntos de ensaios
randomizados com startups (116 e 759 empresas), escrever hipóteses e critérios antes do
teste melhorou os resultados e fez os fundadores largarem ideias ruins mais cedo. Os
**números**, porém, são heurísticas de praticantes ou cálculos sobre premissas; nenhum
limiar foi calibrado contra o resultado de empresas. Por isso todo teste grava os
parâmetros e o resultado: é assim que o harness vai construir taxas-base brasileiras,
que não existem publicadas.

## A escada de evidência (ordinal)

Do mais fraco ao mais forte:

1. opinião
2. e-mail (perde valor depois de ~30 dias)
3. telefone
4. reunião de 30 min
5. **reputação**: apresentação ao decisor, referência nomeada, carta de intenção com
   preço, data e signatário com orçamento
6. depósito
7. pedido pago

Os degraus são uma ordem, não pontos que se somam como probabilidade. "Sim" de quem nunca
tentou resolver o problema vale zero; o alvo são compradores que têm o problema, sabem
disso, já buscaram solução, montaram workaround e têm orçamento.

## Entrevistas (descoberta)

- 10–12 por célula homogênea (função × porte × vertical); 15–20+ se a célula mistura
  perfis; 20–30 para mapear necessidades.
- Parar quando 3 seguidas trazem ≤5% de temas novos.
- Só fatos passados e comportamento, nunca "você usaria?". Toda conversa termina pedindo
  um compromisso (tempo, reputação ou dinheiro). Elogio sem próximo passo conta como
  registro negativo.
- Entrevista gera hipótese; nunca valida sozinha.

## Deflatores

- **Preço declarado** ("eu pagaria R$X"): ÷1,2 central, ÷1,35 mediana, ÷3 pessimista.
- **Intenção de compra** ("compraria"): só "com certeza" conta, dividido por 2 no
  mínimo, e **nunca abre portão de GO**. Intenção prevê pior justamente para produto
  novo, pergunta sobre categoria e horizonte longo, que é o caso típico.

## Test Card

Escrito **antes** do teste e gravado com `python3 -m harness adicionar teste '{...}'`:

- hipótese; experimento; métrica; canal e fonte do tráfego; público;
- regra de decisão com p₀ (taxa que significa "não funciona"), p₁ (taxa que significa
  "funciona"), N máximo e dias máximos;
- degrau da escada que o teste alcança;
- `previsao_p_go`: sua probabilidade, antes de rodar, de o resultado cruzar o GO.

## Regras de decisão

**Web, com tráfego (SPRT, teste sequencial):**

| Métrica | p₀ → p₁ | Exemplo de fronteiras |
|---|---|---|
| E-mail, tráfego morno | 5% → 8% | ~190–240 visitantes em média para decidir |
| E-mail, tráfego pago frio | 3% → 6% | — |
| Pré-venda | 0,3% → 1% | 500 visitantes: GO ≥6, KILL ≤1; 1.000: GO ≥9, KILL ≤4 |

Cortes fixos sobre a taxa observada ("e-mail < 5% = KILL") erram muito com as amostras
usuais: com 1.000 visitantes, uma página cuja taxa real é 5% é morta 48% das vezes.

**Contas B2B de nicho, sem tráfego (Beta-Binomial):** GO se P(taxa > 10%) ≥ 0,8; KILL
se P(taxa > 10%) ≤ 0,2; N máximo de 30 decisores com orçamento. Exemplo: ~3 depósitos em
20 contatos atingem GO. No teto de N sem decisão, KILL ou pivô.

**Lista de e-mail** só autoriza o degrau seguinte. GO para construir exige dinheiro.

## Regras de conduta no Brasil

- Porta falsa: mostrar tela de revelação logo após o clique.
- Pré-venda: termos claros e reembolso automático.
- B2C: direito de arrependimento de 7 dias em compra online (CDC art. 49).
- Coleta de e-mail: aviso de privacidade (LGPD).
- Contato humano: identificação verdadeira, sem pretexto.

Quem fala com o comprador, publica página ou cobra é você. O harness prepara o Test
Card, a página, o roteiro e as mensagens.

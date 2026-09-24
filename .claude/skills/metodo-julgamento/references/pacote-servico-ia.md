# Pacote de critérios · Trilha S (serviço com IA)

O objeto é um serviço produtizado com entrega automatizada por IA, vendido e operado por
uma pessoa. A pergunta do teto: **com o ticket e as horas por cliente propostos, o ICP
alcançável sustenta R$15 mil/mês com margem de 60% ou mais depois das horas do
operador?**

Não existe taxa-base publicada de sucesso de agências ou serviços com IA, nem dado
confiável de CAC, conversão ou churn. A probabilidade parte de um prior largo e
declarado e das taxas que o próprio harness registrar. Todos os limiares abaixo são
provisórios.

## A conta do teto

- Clientes necessários = 15.000 ÷ ticket (ex.: R$1.500/mês → 10 clientes; R$700 → ~22).
- Contas qualificadas alcançáveis ≥ clientes necessários ÷ p₁ (a p₁ de 10%, ~100 contas
  para 10 clientes), mais reposição de churn.
- Horas: a R$1.500/mês com margem de 60%, cabem até ~4 h/cliente/mês; a R$700, menos de
  1 h. Capacidade de referência de um operador: 80 h/mês (parâmetro da trilha).

## Dimensões (nesta ordem, uma de cada vez)

Chaves em `dimensoes`: `trabalho_orcamento`, `comprador_icp`, `resultado_mensuravel`,
`economia_entrega`, `comoditizacao_plataforma`, `caminho_software`.

1. **Trabalho e orçamento.** O trabalho já é pago hoje (terceirizado ou salário
   dedicado)? Qual a proporção de regra × julgamento? Trabalho já terceirizado é troca de
   fornecedor (forte); exigir que o cliente se reorganize é fraco.
2. **Comprador e ICP repetível.** Decisor com orçamento; ICP definido como vertical ×
   porte × função; contas alcançáveis (conta do teto acima).
3. **Resultado mensurável.** Saída padronizada; evento registrado por terceiro (Pix,
   agenda, ticket, protocolo); teste de aceitação escrito. Sem evento verificável não há
   preço por resultado nem promessa de resultado.
4. **Economia da entrega.** Margem após IA, plataforma **e horas do operador**, com piso
   de 60%; setup cobre a implantação; custos variáveis repassados.
5. **Comoditização e plataforma.** O cliente obtém o mesmo com ChatGPT, Meta Business AI
   ou a IA nativa do ERP? O serviço passa por sistemas difíceis do cliente (ERP, SEFAZ,
   portais bancários)? Está dentro dos termos do WhatsApp, na API oficial, com modelo
   trocável? O que resiste é tocar sistema do cliente e ser dono de um resultado.
6. **Caminho para software.** Mesmo fluxo com pouca mudança entre clientes; correções
   humanas registradas desde o cliente 1; produto vendável sem o operador. Julgado por
   repetição, nunca por prazo.

Risco e conformidade entram no veredito sem virar dimensão: contrato com limitação de
responsabilidade, respostas ancoradas, transbordo humano para preço e política, registro
das conversas, papel de operador de dados na LGPD (transferência internacional para APIs
de LLM ainda não verificada), nenhum ato profissional regulado, concentração de receita.

## Travas

**Comprador com orçamento** (dimensões 1 e 2), **margem após as horas do operador**
(dimensão 4) e **repetibilidade**: ICP repetível mais o checklist de produtização (escopo
escrito com exclusões, preço público, formulário de onboarding, fila ou limite de SLA,
procedimentos escritos, pausa em vez de cancelamento).

## Critérios de kill (graduados)

| Código | Critério |
|---|---|
| KS1 | Teto de capacidade: R$15 mil/mês com margem ≥60% exige mais clientes do que o ICP alcançável comporta, ou mais horas do que 80 h/mês de entrega |
| KS2 | Cada cliente é projeto sob medida: sem escopo escrito com exclusões, preço público e formulário de onboarding |
| KS3 | Resultado não mensurável ou sem evento verificável |
| KS4 | Replicável: o cliente obtém 80% do valor com ChatGPT, Meta Business AI ou IA nativa do ERP em 12 meses |
| KS5 | Fora dos termos da plataforma: assistente de uso geral no WhatsApp (vetado desde 15/01/2026, segundo notas de terceiros), ou núcleo dependente de API não oficial |
| KS6 | O entregável é ato profissional regulado (parecer jurídico, escrituração assinada). Não mata a dor: marca `[SERVIR O LICENCIADO]` e reformula para vender ao profissional |
| KS7 | Herdado da trilha G: K3 (comprador sem poder de decisão ou orçamento) |

Categorias de entrada a evitar, salvo evidência nova: bot genérico de perguntas
frequentes, conteúdo ou criativo genérico, prospecção fria automatizada, contabilidade
completa. Compradores candidatos a validar: escritórios de contabilidade, corretoras de
seguro, faturamento de clínicas, documentação jurídica (vendida ao profissional).

## Oferta padrão

Setup ou diagnóstico pago + mensalidade + repasse de uso. Preço por resultado só com
evento de terceiro e cláusula de auditoria. Isso põe caixa no primeiro mês.

## Testes em sequência

| Etapa | Régua provisória | O que decide |
|---|---|---|
| Descoberta | 10–12 conversas por célula; toda conversa termina com oferta de diagnóstico pago | Hipóteses e desenho da oferta |
| T1 · existência (até 30 dias) | Diagnóstico ou setup pago a ≥50% do preço de lista, oferecido a decisores do mesmo ICP. GO: ≥1 contrato pago. KILL ou reformular: 0 em 15 ofertas | Começar a entregar, ainda à mão |
| T2 · repetição | 3 contratos do mesmo ICP e escopo, e P(taxa > 10%) ≥ 0,8 sobre as ofertas (ex.: 3 de 20) | Investir em automação |
| T3 · economia (60–90 dias) | Margem medida ≥60% com horas reais registradas; setup 100% pré-pago; nenhum cliente acima de 30–40% da receita | Escalar vendas |
| T4 · produtização | Mesmo fluxo em ≥3 clientes com pouca mudança e correções registradas | Abrir cartão na trilha M |

# Dossiê kill barato: conferência de nota fiscal contra pedido e lançamento de faturamento (varejo e saúde)

Data: 2026-09-25 · Modo: verificação · Escopo: Brasil · Nº de buscas web: 14 (WebSearch) +
leituras diretas por `curl`/`r.jina.ai` (não contam no orçamento)

Registro factual das três alegações do `contrato.json`. Sem julgamento de tese: status e
ids apenas.

## Alegação 1 — ERPs/ferramentas de NF-e não fazem, como recurso padrão, conferência
automática da NF-e contra o pedido de compra

**Status: sustentada** (com nuance: há recursos de apoio parcial/semiautomático em
vários ERPs, mas nenhum documentado como conferência automática completa e padrão, sem
trabalho manual item a item, especialmente para divergência de preço/imposto).

- Omie: a associação entre item da NF-e recebida e item do pedido de compra é manual —
  o usuário abre a nota pendente, seleciona cada produto e clica em "Associar a um
  produto existente" entre os pedidos aprovados e não recebidos do fornecedor
  (f-2026-0159, Tier 1, leitura integral).
- Bling: o próprio título do artigo de ajuda oficial classifica o vínculo entre NF-e de
  entrada e pedido de compra como "manualmente"; o sistema sugere pedidos dos últimos 90
  dias, mas o usuário confirma e resolve divergências de preço/quantidade item a item
  (f-2026-0160, Tier 1, leitura integral).
- Senior (ERP Gestão Empresarial, documentação 5.10.3): a tela de relacionamento
  nota-fiscal-x-ordem-de-compra tem modo manual e um modo de "sugestão automática" que só
  funciona quando produto/serviço e quantidade são idênticos; mesmo assim é só uma
  sugestão alterável pelo usuário, sem tratar preço (f-2026-0161, Tier 1, leitura
  integral; documentação da versão em descontinuação desde 30/09/2025, ver premissas do
  fato).
- Sankhya: quando a nota chega sem pedido prévio, o lançamento é manual no Portal de
  Compras e, se a TOP exigir, a nota vai para uma "Fila de Conferência" onde outro
  usuário confere manualmente por código de barras e quantidade (f-2026-0162, Tier 1,
  leitura integral).
- TOTVS Protheus: a "conferência física" (leitura de código de barras contra Pré-Nota ou
  Documento de Entrada) não vem ativa por padrão — precisa ser configurada via parâmetros
  MV_CONFFIS/MV_TPCONF e por fornecedor (A2_CONFFIS) (f-2026-0163, Tier 1, leitura
  integral).

## Alegação 2 — Empresas de varejo ou de saúde já pagam terceiros (BPO) para conferir
notas ou lançar faturamento, com oferta publicada

**Status: sustentada para varejo; não encontrada uma oferta equivalente para saúde**
(a alegação usa "ou", e a oferta de varejo já a satisfaz literalmente; registro a
assimetria porque muda o alcance da oportunidade).

- 6in7 (BPO financeiro e fiscal) vende publicamente "Terceirização Fiscal para Varejo":
  recepção de XML, lançamento de entradas, conferência tributária, controle de estoque e
  suporte ao SPED, com depoimentos identificáveis de donos de supermercado como clientes
  reais (f-2026-0164, Tier 1, leitura integral). A página não publica preço, e "lançamento
  de entradas"/"conferência tributária" não deixam explícito se cobrem o confronto item a
  item contra o pedido de compra ou só a checagem fiscal do documento (ver premissas do
  fato).
- Para saúde, a oferta de "terceirização do faturamento" encontrada (Solutionmed) descreve
  um fluxo inteiramente diferente: faturar para convênios via padrão TISS (retirada de
  guias, conferência de guias, envio de XML aos convênios), sem qualquer menção a
  conferência de NF-e de fornecedor contra pedido de compra (f-2026-0165, Tier 1, leitura
  integral). Não encontrei, nas buscas feitas, uma oferta de BPO para saúde que descreva
  especificamente o confronto de NF-e de fornecedor contra pedido de compra.

## Alegação 3 — Vagas de auxiliar de faturamento em varejo e em saúde descrevem o mesmo
fluxo (conferir nota contra pedido e lançar no sistema)

**Status: caiu.** A leitura integral de vagas reais e atualmente ativas (extraídas do
JSON embutido na página do Gupy, não de resumo de busca) mostra fluxos diferentes entre
setores e até dentro do mesmo setor:

- S3 Saúde – UPA Brotas: cadastro de médicos, conferência de escalas/relatórios de
  produção/notas fiscais e apuração de honorários médicos — faturamento de produção e
  honorários médicos, não conferência de NF-e de fornecedor (f-2026-0166, Tier 1, leitura
  integral).
- SPDM/PAIS Porto Alegre: rotina de faturamento SUS da unidade, digitação de dados em
  Excel/sistema hospitalar (f-2026-0167, Tier 1, leitura integral — ver lacuna sobre a
  conferência mecânica abaixo).
- Hospital Unimed Costa Verde: faturamento hospitalar para convênios via TISS, envio de
  XML aos convênios, cobrança de atendimento particular (f-2026-0168, Tier 1, leitura
  integral).
- Grupo NOHDA (varejo de moda, Omnichannel): "responsável por todo o processo de
  faturamento de pedidos do Omnichannel", monitoramento de SLA/ruptura — faturamento de
  pedidos de venda ao cliente, não conferência de NF-e de fornecedor (f-2026-0169, Tier 1,
  leitura integral).
- Descrição genérica nacional da ocupação (Quero Bolsa, agregador, Tier 3): auxiliar de
  faturamento emite notas fiscais de venda, "confere os pedidos realizados por clientes" e
  controla contas a receber/pagar — centrada em faturamento de vendas, não em conferência
  de NF-e de fornecedor contra pedido de compra (f-2026-0170).
- A única fonte que sugeria o fluxo "conferir se a nota bate com o pedido" no varejo
  (Grupo Muffato, citada no fato f-2026-0114 por resumo de busca) não pôde ser relida: as
  três vagas localizadas nesta sessão retornaram HTTP 404, ou seja, encerradas/removidas
  do Gupy (f-2026-0171, ausência verificada).

Nenhuma das quatro vagas lidas integralmente nesta sessão (3 de saúde, 1 de varejo)
descreve o fluxo "conferir NF-e de fornecedor contra pedido de compra e lançar no
sistema"; elas descrevem faturamento a convênios/SUS/honorários médicos (saúde) ou
faturamento de pedidos de venda ao cliente (varejo/Omnichannel).

## O que procurei e não encontrei

- Não encontrei BPO de saúde brasileiro com oferta publicada especificamente para
  conferência de NF-e de fornecedor contra pedido de compra (a oferta de "faturamento
  terceirizado" em saúde que encontrei é sobre convênios/TISS, um fluxo diferente).
- Não encontrei preço publicado de nenhum BPO fiscal/de faturamento (6in7, Solutionmed)
  que permita comparar com o ticket hipotético de R$1.500/mês da oportunidade.
- Não consegui reler a vaga original do Grupo Muffato usada como evidência-âncora de
  "mesmo fluxo" no varejo (três URLs candidatas, todas HTTP 404 nesta data).
- Não busquei especificamente ERPs hospitalares (Tasy, MV) nem ferramentas dedicadas de
  gestão de NF-e fora de ERPs completos (Focus NFe, eNotas, Nota Simples) quanto ao
  recurso de conferência automática contra pedido de compra — ficou fora do escopo desta
  rodada de 14 buscas.

## Lacunas e bloqueios

- **TOTVS:** não ficou claro, pela página lida, se a Pré-Nota já é gerada
  automaticamente a partir do pedido de compra ou se essa vinculação também depende de
  outra rotina manual (ver premissas de f-2026-0163).
- **f-2026-0167 (SPDM/PAIS):** a conferência mecânica (`conferir-trecho`) falhou porque o
  leitor alternativo (r.jina.ai) não renderizou a seção de responsabilidades desta vaga
  nesta tentativa (página montada por script/SPA); reli a página com `curl` direto (HTTP
  200) e confirmei o trecho presente tanto no JSON embutido quanto em HTML visível
  (`<div>`/`<p>`), então mantive `leitura: integral`, mas a checagem automática ficou
  inconclusiva nesta rodada — registro como lacuna, não como erro de citação.
- **Cobertura setorial parcial:** a alegação 1 foi verificada para ERPs de varejo/gestão
  geral (Omie, Bling, Senior, Sankhya, TOTVS); não cobri ERPs específicos de saúde nem
  ferramentas avulsas de gestão de NF-e.
- **Amostra de vagas pequena:** a alegação 3 se apoia em 4 vagas lidas integralmente (3
  saúde, 1 varejo) mais 1 fonte genérica de ocupação; é suficiente para derrubar a
  alegação de "mesmo fluxo" (basta achar fluxos diferentes), mas não é um censo de vagas
  de auxiliar de faturamento no Brasil.
- Todos os fatos novos passaram em `python3 -m harness conferir-trecho` ao final desta
  rodada, após três correções de citação (marcadores de negrito/itálico e separadores de
  lista do markdown gerado pelo leitor alternativo r.jina.ai quebravam a contiguidade do
  trecho original), exceto f-2026-0167 (ver acima).

## Fatos criados nesta sessão

f-2026-0159 a f-2026-0171 (13 fatos): f-2026-0159 (Omie), f-2026-0160 (Bling),
f-2026-0161 (Senior), f-2026-0162 (Sankhya), f-2026-0163 (TOTVS), f-2026-0164 (6in7),
f-2026-0165 (Solutionmed), f-2026-0166 (S3 Saúde), f-2026-0167 (SPDM/PAIS),
f-2026-0168 (Unimed Costa Verde), f-2026-0169 (Grupo NOHDA), f-2026-0170 (Quero Bolsa),
f-2026-0171 (ausência — vaga Grupo Muffato expirada).

**Atualização (orquestrador, 2026-09-25):** o f-2026-0167 foi corrigido depois da entrega. O
trecho tirava os marcadores de lista (·) entre os itens da vaga e punha ponto onde a
página não tem; a separação foi marcada com `[...]`, sem mudar o conteúdo. Agora o trecho
confere na página pelo `curl` direto, e a lacuna de conferência desse fato deixou de
existir.

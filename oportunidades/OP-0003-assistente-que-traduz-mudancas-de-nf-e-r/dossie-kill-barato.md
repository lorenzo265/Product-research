# Dossiê do kill barato: OP-0003

Data: 2026-09-29 · Modo: verificação · Escopo: Brasil, 2022 a 2026 (foco em 2026) · Nº de buscas nativas: 15 (leituras integrais por r.jina.ai não contam como busca)

Pergunta de trabalho (do contrato): donos de empresas que emitem nota fiscal eletrônica pagam assinatura por um emissor que, a partir da descrição da empresa e da área, traduz o que mudou nas regras, nos leiautes e nas alíquotas, interpreta contra a nota atual e aponta o que ajustar, em vez de recorrer ao contador, ao emissor/ERP atual ou a fontes gratuitas?

Nota de método: todas as leituras foram feitas em 2026-09-29 pelo texto da página (r.jina.ai), exceto onde indicado como lacuna. Fatos criados estão com `verificacao: pendente`. Fatos de tier 3 (imprensa, terceiros) estão marcados. Nada abaixo é conclusão de tese; o status de cada alegação diz apenas se o achado sustenta o que a alegação afirma.

## Status por alegação

| # | Alegação (resumo) | Status | Ids que justificam |
|---|---|---|---|
| 1 | Emissores/ERPs deixam ao usuário ou ao contador decidir os campos e classificações novas, sem orientação pelo perfil da empresa | **sustentada**, com ressalvas registradas abaixo | f-2026-0091 a 0112, 0149, 0150, 0152, 0154, 0155; reutilizados f-2026-0082, f-2026-0083 |
| 2 | Não existe ferramenta gratuita (oficial ou de grande player) que, pela descrição da empresa e da área, diga o que muda e o que ajustar na nota | **sustentada no sentido estrito** (nenhuma ferramenta lida cobre o conjunto), com sobreposições parciais registradas abaixo | f-2026-0113 a 0129, 0151; reutilizados f-2026-0003, f-2026-0083 |
| 3 | Mudanças que exigem ação do emitente são recorrentes (mais de uma relevante por ano), não só no pico da reforma | **dividida**: sustentada para 2026-2027 dentro do cronograma da reforma; **não encontrada** para mudanças fora da reforma e para 2028 em diante | f-2026-0130 a 0148, 0153; reutilizado f-2026-0010 |

## Alegação 1: emissores e ERPs (Bling, Omie, Conta Azul, Tiny/Olist, eNotas, NFE.io)

Método: leitura integral das centrais de ajuda e guias de reforma tributária de cada produto. Focus NFe foi lido também por ser emissor via API. Tiny foi lido como "ERP da Olist" (ajuda.olist.com), que é a central que a busca devolveu para o Tiny.

### O que cada um faz e o que deixa ao usuário

| Produto | O que preenche ou oferece | O que deixa ao usuário/contador | Porte/regime tratado |
|---|---|---|---|
| Bling | NF-e/NFC-e: com empresa e natureza de operação em Regime Normal, preenche IBS/CBS com CST 000, cClassTrib 000001 e alíquotas de transição (f-2026-0091) | Regras diferentes do padrão: usuário informa CST, cClassTrib e alíquota por estado de destino ou grupo de produtos na Natureza de Operação (f-2026-0092); personalização "se for solicitado pela sua contabilidade" (f-2026-0093). NFS-e: usuário configura código de tributação nacional, NBS e indicador de operação (f-2026-0094). Eventos (devolução, cancelamento, ajuste): disparo manual pelo usuário (f-2026-0095) | Regime Normal recebe o preenchimento automático; Simples Nacional e MEI: o sistema não envia IBS/CBS neste momento (f-2026-0096) |
| Omie | Opção "preenchimento automático (quando um novo item for incluído)" que aplica os valores configurados; consulta interna à tabela de impostos da reforma (f-2026-0100). App pago Omie.IA Fiscal: sugere tributação para NF-e de venda de mercadorias (f-2026-0082, f-2026-0101, f-2026-0102) | NF-e: usuário informa CST e Classificação Fiscal no Cenário Fiscal "conforme as orientações da sua contabilidade" (f-2026-0097), com exceções por NCM ou produto (f-2026-0098). NFS-e: usuário informa CST, classificação, indicador da operação e alíquotas (f-2026-0099) | Sem recorte de porte na página; o app IA Fiscal não cobre NFS-e (f-2026-0082, f-2026-0102) |
| Conta Azul | NF-e: sugere o cClassTrib pelo NCM do produto (f-2026-0103). NFS-e Pro: calcula IBS/CBS a partir do cClassTrib informado (f-2026-0105) | A página diz que o usuário, com o contador, confirma o cClassTrib (f-2026-0103); "a classificação correta dos seus produtos é uma decisão fiscal, sua e da sua contabilidade" (f-2026-0104). NFS-e: cClassTrib, indicador da operação e NBS devem ser solicitados à contabilidade (f-2026-0106) | Regime normal na NF-e desde 03/08/2026 (f-2026-0141); Simples e MEI a partir de 2027 segundo o Bling (f-2026-0139) |
| Tiny/Olist ERP | Regras de tributação por produto, NCM ou natureza de operação, com motor que escolhe a regra em cada emissão (f-2026-0107) | À pergunta "qual CST e cClassTrib devo utilizar?", a página responde confirmar com a contabilidade e ajustar as regras após a orientação (f-2026-0108) | Simples/MEI: a página orienta validar com a contabilidade antes de configurar ou emitir com IBS/CBS (f-2026-0155) |
| NFE.io | Calcula os novos tributos e gera a nota; oferece links para tabelas de NBS e indicadores (f-2026-0109, f-2026-0110) | Indicação da classificação tributária e mapeamento dos serviços aos códigos oficiais (f-2026-0109, f-2026-0110) | Lucro Real/Presumido: "ajuste mínimo" (f-2026-0109); Simples/MEI: a página diz que nenhuma ação imediata é obrigatória (f-2026-0154) |
| Focus NFe (API) | Campos de IBS/CBS na API | Revisar a regra de negócio do próprio ERP do cliente para calcular as alíquotas (f-2026-0111) | API para desenvolvedores |
| eNotas | Não lido (ver lacunas) | A página inicial cita um "material com as orientações sobre a Reforma Tributária" para clientes; conteúdo não acessado (f-2026-0112) | não lido |

### Ressalvas que o material lido traz sobre a alegação

- A alegação diz "sem orientação pelo perfil da empresa". A Conta Azul sugere o cClassTrib pelo NCM do produto (f-2026-0103), o Bling aplica um padrão (f-2026-0091) e a Omie vende um app de sugestão de tributação para NF-e de mercadorias (f-2026-0082, f-2026-0101). Em todos, a decisão final aparece atribuída ao usuário e à contabilidade nas próprias páginas.
- O Omie.IA Fiscal é cobrado à parte da mensalidade do ERP (preços em f-2026-0082, de leitura anterior; a releitura em 2026-09-29 confirmou a descrição funcional, mas a tabela de preços não apareceu no texto lido).
- Nas páginas lidas não encontrei recurso incluído na mensalidade que explique em linguagem simples, pelo perfil da empresa, o que mudou nas regras e o que ajustar (f-2026-0152, ausência com escopo de busca).
- As páginas do Bling divergem entre si sobre qual tributo tem 0,1% e qual tem 0,9% em 2026 (f-2026-0091 e f-2026-0149); Olist, Conta Azul e NFE.io trazem CBS 0,9% e IBS 0,1% (f-2026-0150).
- Fatos antigos da OP-0001/OP-0002 sobre o mesmo tema (f-2026-0008, f-2026-0084) estão com `verificacao: contradita`; não foram usados.

## Alegação 2: ferramentas gratuitas

Método: busca e leitura de simuladores, calculadoras, consultas de classificação e assistentes de IA gratuitos, oficiais e de terceiros, separando conteúdo genérico de ferramenta personalizada.

### Ferramentas gratuitas encontradas e o que fazem

| Ferramenta | Origem | Entrada | Saída | Ids |
|---|---|---|---|---|
| Portal Nacional de Tributação de Bens e Serviços, "Orientação ao Contribuinte" | Receita/CGIBS (oficial), login gov.br ouro ou prata | Dúvidas por atendimento | Orientações sobre tributação do consumo; a página não menciona preço | f-2026-0113 |
| Calculadora de Tributos (RTC), ambiente piloto | Receita/Serpro (oficial) | Dados da operação | Tributos e base de cálculo de operações (Regime Regular e Simples Nacional); a análise de terceiro lista também verificação de conformidade de XML antes do envio e geração de blocos de XML (tier 3; telas oficiais Assistente de Validação e Assistente de Busca Semântica não lidas) | f-2026-0114, f-2026-0115 |
| Simulador da Reforma Tributária | Sebrae (matéria da Agência Sebrae) | CNAE, faturamento, perfil de vendas | Dois caminhos tributários, estimativa de impostos e de créditos; resultados "estimativas preliminares" | f-2026-0116, 0117, 0118 |
| Calculadora da Reforma Tributária | Portal Contábeis (terceiro), com conta gratuita | CNAE, receitas, custos, despesas, folha | Carga tributária e resultado até 2033, comparativo de regimes; benefícios mapeados por CNAE só em algumas atividades | f-2026-0119, 0120, 0121, 0122 |
| Simulador da Reforma Tributária | Conta Azul (grande player de ERP) | Data, NCM ou NBS, UF e município de destino, valor e quantidade | Alíquotas e valor de CBS/IBS e "preço de venda do futuro" | f-2026-0123, 0124 |
| Consulta de cClassTrib por NCM/NBS | TribuMap (terceiro): consultas básicas gratuitas | NCM ou NBS | cClassTrib, CST e alíquotas | f-2026-0125, 0126 |
| BotRTC | Receita Federal (assistente de IA) | Perguntas | Segundo matéria de imprensa, não orienta casos concretos (página primária não lida) | f-2026-0128 |
| IA gratuita no WhatsApp | Grupo Studio (terceiro), matéria de 05/2025 | Perguntas | Respostas a dúvidas sobre a reforma; a matéria não descreve orientação sobre ajustes na nota de uma empresa específica | f-2026-0129 |
| Emissor Nacional da NFS-e | Governo federal, gratuito | Emissão da NFS-e | Emissão; fato reutilizado f-2026-0003 (leitura por resumo de busca; releitura bloqueada por IP no leitor) | f-2026-0003 |
| Automação Fiscal da Conta Azul (para escritórios) | Conta Azul, gratuita até outubro/2026 | Certificado A1 do cliente | Busca de notas, integração a sistemas contábeis, relatório de crédito IBS/CBS; reutilizado f-2026-0083 | f-2026-0083 |

### O que o material lido mostra sobre a alegação

- Nenhuma das ferramentas gratuitas lidas parte da descrição da empresa e da área de atuação e devolve as mudanças aplicáveis e o que ajustar na nota (f-2026-0151, ausência com escopo de busca).
- Sobreposições parciais: simuladores por CNAE (Sebrae, Contábeis) devolvem carga tributária e cenários, não ajustes de preenchimento (f-2026-0116, f-2026-0119); consulta gratuita de cClassTrib por NCM/NBS existe em nível de produto (f-2026-0125, f-2026-0126); a calculadora oficial, segundo análise de terceiro, verifica conformidade de XML antes do envio (f-2026-0115).
- Conteúdo genérico (artigos, cartilhas, FAQs de emissores) não foi contado como ferramenta personalizada.

## Alegação 3: recorrência das mudanças que exigem ação do emitente

Método: lista de notas técnicas do Portal Nacional da NF-e (leitura integral do texto da página, 311 entradas), notícias e notas da NFS-e nacional, atos de cronograma citados por emissores e imprensa. O texto individual das NTs não foi lido.

### Dentro do cronograma da reforma (2026 a 2033)

Datas que constam nas fontes lidas, com quem se aplica:

| Data | O que passa a valer | Aplica-se a | Ids |
|---|---|---|---|
| 01/01/2026 | Preenchimento de IBS/CBS na NF-e/NFC-e (NT 2025.002 v1.30), com flexibilização técnica | Regime Normal (CRT=3) | f-2026-0138 |
| 03/08/2026 | Campos de IBS/CBS obrigatórios na NF-e/NFC-e, com rejeição automática | Regime regular | f-2026-0140, f-2026-0141 |
| 01/09/2026 | Referenciamento da nota original na nota de devolução (DFeReferenciado) | Emitentes de NF-e de devolução | f-2026-0141 |
| 01 a 30/09/2026 | Janela de opção do Simples Nacional pelo regime regular de IBS/CBS (Res. CGSN 186/2026) | Optantes do Simples | f-2026-0142 |
| 01/10/2026 | IBS/CBS na NFS-e padrão nacional (serviços sujeitos ao ISS da lista LC 116 não incluídos nos grupos do 01/12) | Prestadores de serviço | f-2026-0136, f-2026-0145 |
| 01/12/2026 | IBS/CBS na NFS-e dos demais serviços; obrigação de emitir nota para quem passa a fazer fornecimentos sujeitos a IBS/CBS, movimentar bens materiais ou fazer devoluções (relato do JOTA) | Prestadores de serviço, locações, condomínios; novos emitentes | f-2026-0136, f-2026-0145, f-2026-0146 |
| 01/01/2027 | Destaque de IBS/CBS por Simples Nacional e MEI (04/01/2027 na NF-e segundo o Bling); tributação monofásica e importação de bens materiais; cobrança efetiva da CBS | Simples/MEI (NF-e e NFS-e para quem optou), operações monofásicas e de importação | f-2026-0136, f-2026-0139, f-2026-0141, f-2026-0143 |
| 2029 a 2033 | Cobrança do IBS cresce progressivamente; extinção de ICMS e ISS em 2033 | Todos os emitentes | f-2026-0143 |

Outros fatos sobre a dinâmica: a NT 2025.002 do Portal da NF-e tem 14 versões entre 28/03/2025 e 04/08/2026, 9 datadas de 2025 e 5 de 2026 (f-2026-0130, inferência por contagem própria). Na NFS-e nacional constam as NTs 004 (ago/2025; v2.0 em 12/2025), 005 (19/11/2025), 007 (07/02/2026), 008 e 009 (ratificadas pelo Ato Técnico Conjunto RFB/CGIBS 1/2026) (f-2026-0133, f-2026-0134, f-2026-0135). Datas foram alteradas mais de uma vez: a NT 2025.002 v1.30 saiu três dias antes da data prevista de 06/10/2025 (f-2026-0144); a NFS-e nacional para ME/EPP do Simples foi adiada de 01/09 para 01/11/2026 pela Res. CGSN 191/2026 (reutilizado f-2026-0010); a ausência de IBS/CBS na NFS-e até 31/12/2026 não gera rejeição, mas evidencia desconformidade sujeita a sanções (f-2026-0137). Eventos da reforma (devolução, cancelamento, ajuste) exigem registro manual pelo usuário no Bling (f-2026-0095).

### Fora da reforma (2022 a 2025)

- A lista do Portal da NF-e tem entradas (NTs e versões) por ano de publicação: 2022 = 34, 2023 = 26, 2024 = 25, 2025 = 29, 2026 até 25/09 = 30 (f-2026-0131, inferência por contagem própria); a contagem inclui NTs de web service, eventos e impressão e não separa mudanças que alteram o que o emitente preenche.
- Por título, NTs anteriores à reforma tratam de campos ou regras de validação: 2022.003, 2022.004, 2022.005, 2023.004 e 2024.001 (f-2026-0132, inferência por título; texto das NTs não lido).
- CNPJ alfanumérico: NT Conjunta 2025.001 (08/05/2025) e NT 2026.004 (f-2026-0148, f-2026-0147).
- Não encontrei fonte que conte, por ano, as mudanças que alteram o que o emitente preenche, nem que separe as da reforma das demais (f-2026-0153, ausência com escopo de busca).

## O que procurei e não encontrei

- Recurso incluído na mensalidade dos emissores lidos que explique em linguagem simples, pelo perfil da empresa, o que mudou e o que ajustar (f-2026-0152).
- Ferramenta gratuita que parta da descrição da empresa e da área de atuação e devolva mudanças aplicáveis e ajustes na nota (f-2026-0151).
- Contagem publicada, por ano, de mudanças que exigem ação do emitente, com separação entre reforma e demais (f-2026-0153).

## Registro para o mapa competitivo (ferramentas pagas; fora do status da alegação 2)

- Omie.IA Fiscal (app do ERP Omie): sugere tributação para NF-e de venda de mercadorias, não cobre NFS-e; preço de R$199,90/mês (até 100 itens) a R$1.299,90/mês (4.001 a 5.000 itens) segundo f-2026-0082 (leitura anterior); descrição funcional relida em f-2026-0101 e f-2026-0102.
- TribuMap: consulta de cClassTrib por NCM/NBS, análise em lote, validador de XML, parecer em PDF; "a partir de R$ 79,90/mês" (f-2026-0125, f-2026-0127).
- Automação Fiscal da Conta Azul (para escritórios e BPOs): gratuita até outubro/2026 (f-2026-0083).
- Nomes que apareceram em resultados de busca sem leitura do produto (sem fato): Taxcel (a página lida era a home, não a calculadora), Tecnospeed/PlugNotas (API), Contmatic/Simplifique, e-Auditoria, Buscador NCM (consulta com cClassTrib), "IA da Reforma" da V360, agente de IA da Invent Software.

## Lacunas e fatos vencidos

- Páginas gov.br (Receita: BotRTC, orientações 2026; Emissor Nacional da NFS-e; lista de NTs da NFS-e; NT 009) devolveram só banner de cookies, erro do leitor por reputação de IP ou conteúdo em JavaScript; não é ausência de conteúdo. O BotRTC entrou por matéria de imprensa (f-2026-0128, tier 3).
- Telas "Assistente de Validação" e "Assistente de Busca Semântica" da calculadora oficial: não lidas na fonte primária (aplicativo em JavaScript); só a análise de terceiro (f-2026-0115, tier 3).
- eNotas: material de reforma para clientes não acessado (ajuda.enotas.com.br com erro de certificado; uma URL de blog testada devolveu página não encontrada) (f-2026-0112). Os fatos antigos f-2026-0004 e f-2026-0008 tratam de fonte não oficial ou de trecho não confirmado.
- CGIBS (cgibs.gov.br): leitura com timeout; o cronograma foi lido em CGNFS-e, JOTA e páginas de emissores, não no ato original.
- Notas técnicas individuais (NF-e e NFS-e) de 2022 a 2026 não foram abertas; contagens de f-2026-0130, 0131 e 0132 são de lista e títulos.
- Faixa de preço do Omie.IA Fiscal depende de f-2026-0082, cuja `verificacao` está `nao_verificavel`.
- Consulta de status do proxy foi negada pelo classificador de permissões e não foi repetida.
- Fatos reutilizados dentro da validade em 2026-09-29: f-2026-0003 (90 dias, de 2026-09-24), f-2026-0010 (60 dias, de 2026-09-24), f-2026-0082 (120 dias, de 2026-09-25), f-2026-0083 (90 dias, de 2026-09-25). Todos os fatos criados nesta rodada têm validade de 60 a 90 dias.

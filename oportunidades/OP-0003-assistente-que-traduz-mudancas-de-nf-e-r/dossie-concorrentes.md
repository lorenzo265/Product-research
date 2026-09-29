# Dossiê: que emissores de NF-e e NFS-e e que ferramentas de orientação tributária existem hoje no Brasil, a que preço, para quem e com que assistentes de IA?

Data: 2026-09-29 · Modo: mapa-competitivo · Escopo: Brasil, preços e páginas lidos em 2026-09-29 · Nº de buscas nativas: 9 (as leituras integrais por curl ou r.jina.ai não contam como busca)

Reformulação neutra da pergunta (método): "que emissores e ferramentas de orientação/classificação tributária existem para pequenas empresas, quanto cobram, o que dizem incluir sobre reforma tributária e mudanças de leiaute, e que assistentes de IA e emissores gratuitos oficiais existem?" A pergunta não pressupõe existência nem inexistência de concorrente.

Parâmetros da proposta registrados no cartão depois do contrato: tipo de nota = NF-e e NFS-e; preço ~R$99/mês (aproximado). Onde a tabela cita "até ~R$150/mês", o corte segue o pedido do orquestrador.

Convenções: `Tier` e `leitura` entre parênteses vêm do registro do fato. Cálculos de mensalidade equivalente feitos pelo harness estão marcados como tal. Fatos criados nesta rodada estão com `verificacao: pendente`. Fatos `contradita` (f-2026-0004, 0005, 0008, 0084) não foram usados.


## Correções da verificação (2026-09-29)

Nota do orquestrador, acrescentada depois da verificação e antes dos memorandos. O texto deste dossiê foi escrito antes dela. Onde ele diverge do fato gravado em `data/fatos.jsonl`, vale o fato. O status de cada fato está no campo `verificacao`.

Nenhum fato novo ficou `contradita`. Correções feitas pelo verificador:

- **f-2026-0131 e f-2026-0226 a 0230 (NTs da NF-e por ano).**
  - Entradas totais na lista do Portal: 2022 = 36 e 2024 = 27; os demais anos conferem (315 entradas no total).
  - NTs fora da reforma que tratam de campos, regras ou leiaute: 2022 = 8, 2023 = 7, 2024 = 6, 2025 = 6, 2026 = 7 (antes: 9, 8, 8, 7 e 6).
- **f-2026-0142 (opção do Simples Nacional pelo regime regular de IBS/CBS).** A página atual diz que o prazo foi estendido pelo CGSN até 30/10/2026, e não 1 a 30/09/2026. O f-2026-0176 (07/09/2026) é anterior à prorrogação.
- **f-2026-0141 x f-2026-0172.** As duas estão confirmadas e divergem entre si:
  - a Conta Azul (página atualizada em 29/09/2026) descreve rejeição da NF-e sem IBS/CBS desde 03/08/2026;
  - o comunicado da Receita e do CGIBS (01/08/2026, atualizado em 03/08/2026) diz que um Ato Técnico Conjunto a aprovar suspenderá a obrigatoriedade e que os documentos não serão rejeitados sem esses campos.
- **f-2026-0177 e f-2026-0178.** O autor do artigo no Portal Contábeis (06/05/2026) é o fundador do nomos-ia.app, um assistente de IA para a reforma tributária em beta. Não é "contador" sem vínculo comercial.
- **f-2026-0168 (Olist/Tiny).** R$159,30 (Construa) e R$312 (Impulsione) são ofertas de Black Friday nos 3 primeiros meses. Os preços cheios são R$177 e R$390.
- **f-2026-0162 (NFE.io).** Os preços conferem. A página também cobra taxa de adesão (R$199 a R$499, conforme o plano).
- **f-2026-0166 (Omie.IA Fiscal).** Os trechos sobre "empresas que vendem em diferentes estados" e "gestores" estão na loja de apps (store.omie.com.br), não na página citada. A alegação foi reduzida ao que a página citada sustenta.
- **f-2026-0181 e f-2026-0184.** A websérie da Omie está na URL do f-2026-0180, e o chatbot "Cami" da Conta Azul está em /planos. Os dois foram retirados desses fatos.
- **f-2026-0183 (Conta Azul).** "Gratuitamente" vale só para o diagnóstico, os materiais e o simulador de impacto.
- **f-2026-0174 e f-2026-0191.** "Gratuitos" / "gratuitas" não consta nas páginas e foi retirado.
- **f-2026-0185 (Taxcel).** Os preços são de 1 usuário; o descritor "(cloud)" não está na página.
- **f-2026-0206 (Tax Prático).** São 7 planos, de R$2.119,89 a R$9.202,14 (antes: maior plano R$4.388,63).
- **f-2026-0214 (Invent/SEGS).** A página diz "mais de 152 empresas" e "mais de 1500 interações, segundo a companhia". A menção ao Grupo Studio e a "200 empresários" vinha do resumo de busca e foi retirada.
- **f-2026-0200 (TOTVS).** O acesso ao chatbot pelo Portal de Clientes não é descrito como restrito.
- **f-2026-0221 (RT PRO)** e **f-2026-0220 (Omie IA.Fiscal).** As alegações foram reduzidas ao que a página citada mostra.
- **f-2026-0106 (Conta Azul).** Acrescentado o qualificador "NFS-e (Padrão Nacional)".
- **f-2026-0205 (LWSA).** O PDF tem 56 páginas, com cerca de 28 em português.

Ficaram `nao_verificavel`:
- páginas de ajuda do Bling (403 do Cloudflare, não contornado): f-2026-0091 a 0096, 0138 a 0140, 0143 e 0149;
- aplicações montadas por JavaScript: f-2026-0113 e 0114;
- fatos vindos de resumo de busca: f-2026-0213 (GPT "Consultor Tributário", URL 404) e f-2026-0216 (emissores gratuitos das SEFAZ).

## 1. Emissores e ERPs com NF-e e/ou NFS-e

### 1.1 Preços públicos lidos na página (plano de entrada e vizinhos)

| Produto | Preço lido | O que a página lista de emissão | Público declarado na página | Ids |
|---|---|---|---|---|
| Meu Emissor | R$37,90/mês (plano mensal) | NF-e, NFS-e, NFC-e, NFP-e; usuários e notas ilimitados | Não informado no trecho lido | f-2026-0050 (Tier 1, integral; valor mensal reconfirmado em releitura de 2026-09-29) |
| Nota Simples | R$79,90/mês (até 200 notas), R$109,90 (até 400), R$139,90 (Avançado) | Emissor de NF-e com controle de estoque | Emissor com estoque | f-2026-0049 (Tier 1, integral) |
| Focus NFe, Solo e Start | R$89,90/mês (1 CNPJ, 100 notas, R$0,10 por nota extra); R$113,90/mês (3 CNPJs) | NF-e, NFS-e, NFC-e, CT-e, MDF-e, NFCom, DCe; recebimento de NF-e, CT-e e NFS-e Nacional | API para desenvolvedores ("economizem tempo de seus desenvolvedores"); suporte por e-mail | f-2026-0170 (Tier 1, integral); Growth R$548/mês em f-2026-0044 |
| Simplifique (Contmatic), plano Emissores | R$99,90/mês (30 emissões/mês); Essencial R$159,90 (ilimitado + gestão); Completo R$299,90 | NF-e, NFS-e, CT-e, MDF-e; validador de notas Sefaz; suporte por chat | Pequenas empresas que só emitem notas | f-2026-0190 (Tier 1, integral). Trimestral do Emissores: R$269,73, equivalente a R$89,91/mês (cálculo do harness) |
| Bling, Cobalto | R$60/mês no pagamento mensal (R$720/ano); equivalente a R$50/mês no plano anual; oferta Black de 5% na 1ª mensalidade (R$57). Titânio R$120/mês; Diamante R$650/mês | Notas fiscais ilimitadas; NF-e, NFC-e, NFS-e (700+ municípios); certificado A1 ou A3 | ERP para venda multicanal; planos definidos por pedidos de marketplace/API (Cobalto até 200) | f-2026-0156, 0157, 0158 (Tier 1, integral) |
| Olist ERP (Tiny), Avance | R$66/mês; Construa R$177 (R$159,30 indicado); Impulsione R$390 (R$312/mês mensal); oferta Black de até 30% | ERP com emissão de notas; IA Lis em todos os planos | ERP para vendedores multicanal | f-2026-0168 (Tier 1, integral) |
| NFE.io | R$190/mês (até 250 notas/mês), R$265 (500), R$375 (1.000); no anual, Plano Inicial R$1.075/ano (até 100 notas/mês, até 2 CNPJs), equivalente a R$89,58/mês (cálculo do harness) | Somente NFS-e; API e emissão em lote | Empresas e desenvolvedores; MCP para agentes de IA (seção 3) | f-2026-0162 (Tier 1, integral) |
| eNotas | Basic R$1.227/ano (720 notas/ano, R$0,77 por nota extra), equivalente a R$102,25/mês (cálculo do harness); Plus R$2.297/ano (6.000 notas/ano) | NFS-e e NF-e; integração Hotmart | Produtor digital, coprodutor, afiliado | f-2026-0161 (Tier 1, integral) |
| Conta Azul, Essencial (MEI) e Controle (ME) | Essencial "a partir de 179,90/mês" (anual) ou 269,90/mês (outro ciclo); Controle 349,90/mês (anual) ou 499,90/mês | ERP com NF-e e NFS-e; planos por faixa de faturamento (MEI até R$81 mil/ano; ME até R$360 mil/ano) | Dono do negócio; há produto separado (Conta Azul Mais) para contadores | f-2026-0160 (Tier 1, integral) |
| Omie, ERP Padrão | "A partir de R$309,00 por mês"; Multivarejo a partir de R$419,00; valor definido pela receita bruta mensal | Emissão de notas fiscais; captura automática de notas de compra e de serviços | ERP para empresas; usuários ilimitados | f-2026-0159 (Tier 1, integral) |
| Nibo Gestão Financeira | Light R$208/mês, Plus R$312, Premium R$479 (mensal, sem desconto) | Emissão de NFS-e dentro da gestão financeira | Empresas e escritórios contábeis | f-2026-0051 (Tier 1, integral); f-2026-0221 |

Faixa até ~R$150/mês, só com valor lido na página: Meu Emissor (R$37,90), Nota Simples (R$79,90 a R$139,90), Focus Solo e Start (R$89,90 e R$113,90), Simplifique Emissores (R$99,90), Bling Cobalto e Titânio (R$60 e R$120), Olist Avance (R$66), NFE.io Inicial anual (equivalente a R$89,58) e eNotas Basic (equivalente a R$102,25). Conta Azul (a partir de R$179,90) e Omie (a partir de R$309) começam acima desse corte.

### 1.2 O que cada emissor diz sobre reforma tributária e mudanças de leiaute

Base já gravada na verificação (leituras de 2026-09-29, Tier 1, integral): Bling preenche IBS/CBS no Regime Normal com CST 000, cClassTrib 000001 e alíquotas de transição, e deixa ao usuário as regras diferentes do padrão (f-2026-0091, 0092, 0093, 0096); a Omie oferece consulta à tabela de impostos da reforma dentro do ERP e pede CST e classificação "conforme as orientações da sua contabilidade" (f-2026-0097, 0100); a Conta Azul sugere o cClassTrib pelo NCM e atribui a confirmação ao usuário e à contabilidade (f-2026-0103, 0104); o ERP da Olist tem regras por produto, NCM ou natureza de operação e responde à pergunta sobre qual CST usar com "confirmar com a contabilidade" (f-2026-0107, 0108); a NFE.io calcula os novos tributos e deixa a indicação de classificação ao usuário (f-2026-0109, 0110); a Focus NFe pede revisão da regra de negócio do ERP do cliente (f-2026-0111). Síntese da ausência na mensalidade: f-2026-0152.

Acrescentado nesta rodada:

- Omie: a página "Reforma Tributária no seu Omie" afirma alíquotas "atualizadas em tempo real", preenchimento automático da alíquota simbólica de 1% e envio de tributos com "configuração padrão tributável" mesmo sem cenário fiscal específico (f-2026-0180, Tier 1, integral).
- Conta Azul: a Central da Reforma afirma que o ERP "atualiza automaticamente as regras fiscais" e que a adequação foi feita "sem nenhuma configuração manual por parte do usuário" (f-2026-0182, Tier 1, integral; afirmação do próprio fornecedor). A mesma central oferece calculadora de impacto, simulador de regime do Simples, diagnóstico gratuito, manual e "Encontre um Contador" (f-2026-0183). A frase da central e a do FAQ de suporte (f-2026-0104) aparecem em páginas diferentes do mesmo fornecedor.
- Simplifique: blog com artigos explicativos, por exemplo "IBS e CBS na NF-e: Campos Obrigatórios a Partir de 03/08/2026" (07/07/2026), e calculadora gratuita (f-2026-0191, Tier 1, integral).
- Omie mantém o "Radar Reforma Tributária" com notícias de 29/09/2026, e-books gratuitos, websérie semanal e o canal CERTO, com curso e mentorias para contadores (f-2026-0181, Tier 1, integral).
- Nas páginas de preço lidas de Bling, Simplifique, Focus, NFE.io, Olist e eNotas, nenhum plano até ~R$150/mês descreve, entre seus itens, orientação sobre mudanças fiscais por perfil da empresa (f-2026-0217, ausência com escopo).

### 1.3 Emissor gratuito oficial

| Ferramenta | O que consta | Ids |
|---|---|---|
| Emissor Nacional da NFS-e (gov.br) | Gratuito, web ou API; obrigatório para ME/EPP do Simples a partir de 01/11/2026 (Res. CGSN 191/2026) | f-2026-0003 (leitura por resumo de busca, Tier 1); f-2026-0010 |
| Emissor web da NFS-e com campos de IBS/CBS | Lançado em 10/08/2026 pela Receita e pelo Comitê Gestor do IBS; matéria cita uso "especialmente por empresas menores"; 44% das NFS-e sem preenchimento dos campos nos últimos 30 dias; Fisco notificou contribuintes | f-2026-0193 (Tier 3, imprensa, integral) |
| Emissor de NF-e do Sebrae | Página diz "de forma segura e gratuita" para notas de mercadorias e produtos; aplicativo em JavaScript, só o texto de abertura foi lido; não consta se preenche IBS/CBS | f-2026-0215 (Tier 1, integral) |
| Emissores gratuitos de NF-e de SEFAZ estaduais | Páginas de SEFAZ-PB e SEFAZ-MS aparecem em busca; não foram lidas | f-2026-0216 (resumo de busca) |
| Visão de um emissor concorrente sobre os gratuitos | Blog do Simplifique diz que os gratuitos do governo têm "limitações" e os indica a MEIs de 1 a 5 notas por mês; texto de fornecedor com interesse comercial, sem fonte oficial | f-2026-0192 (Tier 3) |
| Calculadora de Tributos RTC (piloto oficial) | Simula tributos de operações; análise de terceiro lista verificação de XML antes do envio | f-2026-0114, 0115 |

## 2. Ferramentas pagas de orientação, classificação e automação fiscal

| Ferramenta | O que faz | Para quem (segundo a página) | Preço lido | Ids |
|---|---|---|---|---|
| Omie.IA Fiscal (app do ERP Omie) | Sugere tributos, CST, alíquotas, reduções de base e textos legais na NF-e de venda de mercadorias; cruza dados da empresa, operação, produto e UF de destino; monitora mais de 30 publicações legais; IBS e CBS contemplados; não cobre NFS-e, devoluções, transferências, importação nem NFC-e; "não determina ou sugere a Regra de Cálculo dos Tributos"; pode não capturar regimes especiais | Clientes Omie (exclusivo); empresas que vendem ou revendem produtos em vários estados; a página cita "você e seu contador" | R$199,90/mês (até 100 itens), R$399,90 (101 a 500), R$499,90 (501 a 1.000), R$599,90 (1.001 a 2.000), R$699,90 (2.001 a 3.000), R$799,90 (3.001 a 4.000), R$1.299,90 (4.001 a 5.000); cobrado na mesma NFS-e do ERP; reajuste anual por IGPM | f-2026-0165, 0166, 0167, 0199, 0220 (Tier 1, integral); f-2026-0082 (leitura anterior, `nao_verificavel`, faixa igual) |
| TribuMap | Consulta de cClassTrib, CST e alíquotas por NCM ou NBS com base legal; análise em lote (CSV/XLSX); validador de XML de NF-e; parecer em PDF com marca do escritório; base atualizada em até 48 horas úteis após nova NT (meta declarada); API; página diz que não presta aconselhamento tributário nem substitui contador | Contadores, escritórios e departamentos fiscais; plano "Individual" para o profissional autônomo | Gratuito para 5 NCMs em lote e consultas básicas; Individual R$79,90/mês; Escritório R$129/mês (até 5 usuários); teste de 7 dias | f-2026-0125, 0127, 0163, 0164, 0171 (Tier 1, integral); f-2026-0126 |
| Taxcel (TaxSheets, Studio, Hub, Olyve AI) | Análise e conciliação de arquivos fiscais (SPED, DF-e), transformação de dados com IA, dashboards, simulador da reforma 2026-2033 sob demonstração; Olyve AI responde "fundamentadas nos seus SPEDs e DFes reais" | Corporações de médio e grande porte, consultorias tributárias, BPOs e contabilidades; mais de 750 empresas clientes | TaxSheets Starter R$10.500/ano; Studio Starter R$18.000/ano; Hub com Olyve Light a partir de R$12.140/ano (R$30.350 com Tax Analytics); Teams, Pro e Enterprise sob consulta | f-2026-0185, 0186 (Tier 1, integral) |
| TecnoSpeed PlugNotas | API de emissão de NF-e, NFC-e, NFS-e, NFCom e MDF-e; a empresa "cuida de tudo que muda no fiscal" (IBS, CBS, novos layouts) | Software houses (4.100+ integradas, 2.200+ municípios) | Sem preço na página inicial | f-2026-0187, 0218 |
| TecnoSpeed DecisionIT | Plataforma de "Inteligência Fiscal" para IBS e CBS, consultoria, motor tributário, SPED; "empresa oficial do Projeto Piloto da CBS" | Empresas Enterprise | Sem preço nas páginas lidas | f-2026-0188, 0218 |
| Contmatic (Contábil Phoenix e ERP Simplifique) | Sistema contábil para escritórios e ERP com emissores; o Simplifique consta na seção 1.1 | Escritórios contábeis (Phoenix); pequenas empresas (Simplifique) | Phoenix sem preço na página lida; Simplifique R$99,90 a R$299,90/mês | f-2026-0189, 0190, 0218 |
| Automação Fiscal da Conta Azul (Conta Azul Mais) | Busca automática de NF-e, NFS-e, NFC-e e CT-e nas bases da SEFAZ e prefeituras, integração a sistemas contábeis e relatório de crédito IBS/CBS | Escritórios contábeis e BPOs (14.000+ escritórios parceiros segundo a página) | Gratuita até outubro/2026 (post de 26/08/2026) | f-2026-0083 (Tier 1, integral, reutilizado) |
| ROIT START | Plataforma de preparação para a reforma (videoaulas, simulador de impactos, checklists) | Empresas e equipes (Bronze até 5 usuários) | R$499, R$1.197 e R$1.897/mês | f-2026-0055 (Tier 1, integral; `verificacao: nao_verificavel`) |
| RT PRO (Reforma Tributária, Tax Capital) | Plataforma de conteúdo com "IA treinada com nosso acervo" e "Monitor automático de notas técnicas" | Profissionais (revista, cursos, legislação) | Preço não consta na página lida; teste de 7 dias | f-2026-0221 (Tier 3) |
| Nibo (Gestão Financeira, Emissor) | Gestão financeira com "IA do Nibo" e emissão de NFS-e; o texto lido não trata de tributação | Empresas, escritórios contábeis, BPO | Ver seção 1.1 | f-2026-0051, 0221 |
| Simuladores gratuitos (Sebrae, Portal Contábeis, Conta Azul, Simplifique) | Carga tributária e cenários por CNAE, faturamento ou NCM; não devolvem ajustes na nota | Donos de empresa e contadores | Gratuitos | f-2026-0116 a 0124, 0183, 0191 |

## 3. Defensibilidade de IA: assistentes já lançados e ferramentas gerais

### 3.1 Assistentes de emissores e ERPs (com data)

| Empresa | Assistente | Data | O que a fonte descreve | Trata de dúvida fiscal ou sugestão de tributação? | Ids |
|---|---|---|---|---|---|
| Omie | Omie.IA Fiscal | Lançamento não localizado; artigo de ajuda de 13/03/2026; "novo nome" da IA Fiscal anterior | Sugestão de tributação na NF-e de venda de mercadorias | Sim, sugestão de tributação (seção 2) | f-2026-0166, 0167, 0199, 0220 |
| Olist (Tiny) | Lis, agentes de IA | Anunciada em 28/07/2025 (Exame) | Consulta a base do ERP e executa ações; agentes para emissão de notas fiscais, preços, relatórios, estoque; créditos mensais de 10, 20 e 40 por plano, inclusa em todos os planos | O texto lido de olist.com/agentes e tiny.com.br/precos não menciona dúvidas fiscais, sugestão de tributação, IBS ou CBS | f-2026-0168, 0169, 0195, 0196, 0198 |
| Conta Azul | Conta Azul IA | Publicada em 13/08/2025 (atualizada em 15/09/2026) | Importação de documentos, notificações (mais de 30 alertas, entre eles "nota rejeitada") e automações, no financeiro | Descrição não inclui dúvidas fiscais nem tributação | f-2026-0184, 0197 |
| Bling | Assistente do Bling | Anunciado em 15/04/2026 (AdNews) | Agentes de estoque e preço, anúncios em marketplaces e imagem | Matéria não lista dúvidas fiscais nem tributação | f-2026-0194 |
| Nibo | "IA do Nibo" | Data não localizada | Gestão financeira | Texto lido da página inicial não trata de tributação | f-2026-0221 |
| NFE.io | Servidor MCP com 21 ferramentas para ChatGPT, Claude, Gemini e Copilot | Post de 28/08/2026 | Emissão de NFS-e por conversa; 13 ferramentas gratuitas, entre elas validação de CST/CSOSN por regime e ICMS interestadual; conta gratuita | Validações de CST/CSOSN por regime sim; orientação sobre mudanças não consta no texto lido | f-2026-0212 |
| TOTVS | Chatbot Especialista em reforma tributária | 20/10/2025 (Tax Capital) | Responde sobre legislação e regras, preparação dos ERPs TOTVS e pacotes; no Portal de Clientes, 24x7 | Sim, sobre legislação e produtos TOTVS; acesso de clientes TOTVS | f-2026-0200 (Tier 3) |
| Taxcel | Olyve AI | Data não localizada | Respostas sobre SPEDs e DF-e do próprio cliente | Consultivo sobre arquivos fiscais reais; público corporativo | f-2026-0186 |
| eNotas, Focus NFe, Simplifique | Não localizei assistente de IA nas páginas lidas | n/d | n/d | n/d | Ver seção "O que procurei e não encontrei" |

### 3.2 Poder público

- BotRTC (Receita Federal): disponibilizado em 06/02/2026, junto com o Portal da Reforma Tributária; IA generativa; acesso pelo botão "Fale Conosco" em consumo.tributos.gov.br; a Receita diz que ele "não dá orientações sobre casos concretos", não acessa dados fiscais e pode ter imprecisões (f-2026-0211, Tier 3, integral; f-2026-0128, Tier 3, integral).
- Portal Nacional de Tributação de Bens e Serviços (Receita e CGIBS): "Orientação ao Contribuinte" com atendentes para dúvidas sobre tributação do consumo; a página não cita preço (f-2026-0113, Tier 1, integral).
- Não localizei assistente de IA do CGIBS separado do BotRTC (ver ausências).

### 3.3 Assistentes e GPTs gerais usados para dúvidas de reforma e NF-e

- Grupo Studio: IA gratuita por WhatsApp para dúvidas de empresários sobre a reforma, matéria da CNN Brasil de 20/05/2025 (f-2026-0129, Tier 3, integral).
- Invent Software: agente de IA gratuito por WhatsApp sobre a reforma; a síntese do buscador cita a matéria do SEGS, que não foi lida (f-2026-0214, Tier 3, resumo de busca). A síntese do buscador atribui ao Grupo Studio mais de 200 empresários usuários; o número não foi confirmado em página.
- GPTs no ChatGPT: um GPT público "CONSULTOR TRIBUTÁRIO" aparece em resultado de busca; a página não foi lida; autor, descrição e uso são desconhecidos (f-2026-0213, Tier 3, resumo de busca). Blogs de Tecnospeed, Taxcel, Qive e NFE.io publicam guias de uso do ChatGPT na área fiscal (títulos em resultado de busca, f-2026-0213).
- Cada assistente acima responde a perguntas ou executa tarefas; nenhuma das páginas lidas descreve um assistente que receba a descrição da empresa e a nota atual e devolva o que ajustar (base: f-2026-0151, 0152, 0198).

## O que procurei e não encontrei

- Recurso incluído nos planos de emissor até ~R$150/mês, descrito na página de preços, que oriente ou traduza mudanças fiscais por perfil da empresa (f-2026-0217; síntese anterior em f-2026-0152).
- Uso da Lis, da Conta Azul IA ou do Assistente do Bling para dúvidas fiscais: o texto lido das páginas de Olist não os menciona (f-2026-0198); Conta Azul IA e Bling constam na seção 3.1 sem menção fiscal nas fontes lidas (f-2026-0194, 0197).
- Preço público do Contábil Phoenix (Contmatic), do PlugNotas e da DecisionIT (f-2026-0218).
- Número de usuários ou métrica de adoção de GPTs e chatbots gerais para dúvidas de NF-e e reforma: só a síntese de buscador cita "mais de 200 empresários" para uma IA no WhatsApp (f-2026-0214); não há dado de uso de GPTs gerais (buscas 6 e 8 desta rodada).
- Assistente de IA do CGIBS distinto do BotRTC: não apareceu nas buscas 7 e 8 desta rodada; a busca não usou "CGIBS" como termo de consulta, então a ausência tem escopo limitado.
- Assistente de IA de eNotas, Focus NFe e Simplifique: não foi buscado por nome nesta rodada e as páginas lidas não citam (lacuna de busca, não ausência verificada).

## Lacunas e fatos vencidos

- Bling: a central de ajuda sobre o Assistente do Bling devolveu bloqueio (HTTP 403, verificação do navegador); uma síntese de buscador diz que o assistente estava em "testes controlados" e sem disponibilidade para todas as contas, sem fonte lida. Não virou fato.
- Bling e Olist: os preços têm ofertas Black Friday e alternância mensal/anual; o valor lido pode não ser o de tabela para todos os ciclos. Bling Cobalto mostra R$720, R$60, R$57 e "equivalente a R$50/mês" juntos; a leitura adotada (R$60 mensal, R$50 anual) é interpretação do harness sobre o layout.
- Conta Azul: os dois valores por plano dependem do ciclo (anual e outro); a página não rotula qual é qual no texto extraído; a leitura adotada (menor valor = anual) segue a ordem do texto e o botão "Anual".
- Olist: o valor R$66 do Avance aparece com a alternância "Mensal / Até 30% OFF / Anual"; o ciclo do valor não está rotulado no texto extraído.
- eNotas: página de preço lida por r.jina.ai mostra planos anuais; valor mensal equivalente é cálculo do harness. O material de reforma para clientes não foi lido (f-2026-0112, verificação anterior).
- Meu Emissor e Nota Simples: preços de f-2026-0050 e f-2026-0049 (leitura de 2026-09-25, dentro da validade de 180 dias); o que suas páginas dizem sobre reforma tributária não foi lido nesta rodada.
- Leitura direta de páginas de SEFAZ estaduais (PB, MS) falhou e o leitor r.jina.ai devolveu bloqueio por reputação de IP; a página do Sebrae é aplicativo em JavaScript. Se o emissor gratuito de NF-e preenche IBS/CBS não consta em nenhuma leitura.
- Emissor Nacional da NFS-e (f-2026-0003): leitura por resumo de busca; releitura bloqueada anteriormente. O emissor web de 10/08/2026 entra por imprensa (f-2026-0193, Tier 3).
- Página do GPT "CONSULTOR TRIBUTÁRIO": leitura direta devolveu 404; página do SEGS não lida (f-2026-0213, 0214).
- Data de lançamento do Omie.IA Fiscal e da "IA do Nibo": não localizadas.
- Divergência de data que afeta fatos da verificação: a Central da Reforma da Conta Azul (lida em 2026-09-29) indica opção do Simples pelo regime regular "até 30 de outubro de 2026", e o Radar da Omie (2026-09-29) tem manchete "CGSN prorroga prazos para opção do Simples Nacional 2027 e IBS/CBS"; o fato f-2026-0142 registra janela de 1º a 30 de setembro de 2026 (Res. CGSN 186/2026). Não verifiquei o ato original; f-2026-0142 pode estar defasado.
- Fatos reutilizados dentro da validade: f-2026-0003 (90 dias, 2026-09-24), f-2026-0010 (60 dias, 2026-09-24), f-2026-0044, 0049, 0050, 0051 (180 dias, 2026-09-25), f-2026-0055 (180 dias, 2026-09-25, `nao_verificavel`), f-2026-0082 (120 dias, 2026-09-25, `nao_verificavel`), f-2026-0083 (90 dias, 2026-09-25) e os de f-2026-0091 a 0155 citados (60 a 90 dias, 2026-09-29). Os fatos criados nesta rodada têm validade de 90 dias.

## Fatos criados nesta rodada

f-2026-0156 a 0171, f-2026-0180 a 0200, f-2026-0211 a 0221 (os intervalos 0172 a 0179 e 0201 a 0210 pertencem a outro pesquisador). Todos com `verificacao: pendente`. O texto da alegação de f-2026-0220 foi ajustado por `atualizar` (valor anterior guardado em `historico`).

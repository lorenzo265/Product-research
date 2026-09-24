# As 11 lentes de sinal (modo varredura)

Cada lente é uma forma independente de detectar dinheiro mal servido. Um setor que
dispara várias lentes tem sinal composto, mais forte. Para cada lente, devolva todo sinal
que ela capturar, com evidência: o filtro e o ranking acontecem num passo separado, não
aqui. Esforço de referência: ~5–10 buscas por lente, mais aprofundamento nos candidatos
que aparecem.

Cada sinal é gravado com `python3 -m harness adicionar sinal '{...}'`, citando os ids
dos fatos que o sustentam. Sinal com **cifra** (dinheiro já gasto ou perdido) ou
**recorrência** vale mais que sinal sem: prefira as fontes cuja estrutura já obriga uma
das duas.

As fontes vêm do relatório `research/Fontes de dados e ferramentas.md`. Marcações:
**coletor** (script próprio, quando existir), **MCP** (consulta pontual, se ligado),
**busca** (busca web), **evitar** (termos de uso, custo ou LGPD).

## Lente 1 · Baixa penetração de software × tamanho do setor

Setor com faturamento alto e gasto em software desproporcionalmente baixo opera em
planilha, papel e WhatsApp.
- **Fontes:** contagem de CNPJ por CNAE × porte × UF (denominador); IBGE CEMPRE (tabelas
  9509 e 9528); PAS, PAC e PIA do IBGE; estudos ABES/FGV; relatórios setoriais (CNI, CNC,
  CNT, CBIC, ABAD). O numerador (quem já usa software) sai da busca: base de clientes
  declarada por fornecedores.
- **Queries:** "[setor] gestão planilha", "[setor] digitalização atraso", "software para
  [setor] brasil" (avalie qualidade e idade do que aparece).
- **Evitar:** listas de sócios, telefones e e-mails do cadastro de CNPJ (fora da
  finalidade, LGPD).

## Lente 2 · Incumbente caro e mal avaliado

Onde o líder cobra caro e é mal avaliado, há espaço.
- **Fontes:** consumidor.gov.br (reclamações finalizadas por empresa, dado aberto);
  avaliações em português no Google Play; G2/Capterra (reviews de 1–2 estrelas de
  ferramentas dominantes no BR); Reclame Aqui só por busca (`site:reclameaqui.com.br`).
- **Queries:** "[líder] ruim", "[líder] alternativa", "cansado do [software]", "migrar do
  [software]".
- **Nota de método:** a nota do Reclame Aqui mede o processo de resposta, não a
  satisfação com o produto. Melhores proxies: % "voltaria a fazer negócio", nota do
  consumidor e teor recorrente. Em B2B, 150–250 reclamações em 6 meses já é volume
  relativamente alto.
- **Registre também o sinal invertido:** players bem avaliados no vertical. É evidência
  tão valiosa quanto, porque indica mercado bem servido.
- **Evitar:** raspagem em massa do Reclame Aqui; mineração de avaliações do Google Places.

## Lente 3 · Fragmentação sem líder competente

Maior player com menos de 10% do mercado vendendo produto tecnologicamente velho.
- **Fontes:** CNPJ por porte (fatia de micro e EPP); CEMPRE; mapeamentos setoriais
  (Distrito, Liga Ventures, ABStartups); Crunchbase e dealbooks; sites dos players (idade
  da stack visível no produto).
- **Sinal confirmatório:** ausência de rodadas de VC relevantes no vertical em 5 anos,
  ou rodadas recentes pequenas (mercado recém-descoberto).

## Lente 4 · Choque regulatório compulsório com data

Migração forçada cria uma coorte inteira de compradores com prazo. Historicamente o sinal
mais forte do método, e o "por que agora" que toda tese precisa responder.
- **Fontes:** DOU via INLABS (Seções 1 e 3, XML oficial); Querido Diário (diários
  municipais; cobertura parcial, confira as cidades); agendas regulatórias anuais
  (obrigatórias pela Lei 13.848/2019: ANVISA, ANS, ANEEL, ANTT, BACEN, CVM, MAPA, CNJ);
  calendário da Reforma Tributária (LC 214/2025); eSocial/EFD; PNCP (planos anuais de
  contratação mostram o que o governo vai comprar).
- **Queries:** "nova obrigação [ano] empresas", "prazo adequação [norma]", "multa
  descumprimento [norma]", "obrigatoriedade a partir de".
- **Registrar:** norma (link primário), data de vigência, população obrigada (nº de
  empresas ou CNAEs), penalidade e quem já vende solução.
- **Evitar:** raspagem da página de busca do DOU (use o INLABS); Seção 2 (atos de
  pessoal).

## Lente 5 · Trabalho manual em escala (vagas como proxy)

Setor contratando gente para fazer o que software faria está pagando salário onde
poderia pagar assinatura.
- **Fontes:** Novo CAGED e RAIS por CBO × CNAE (via Base dos Dados); páginas de empresa
  na Gupy; Catho (páginas de vaga, depois de ler os termos); descrições de vagas (a
  descrição descreve o fluxo a automatizar).
- **Queries:** vagas de "assistente de digitação", "conferente de notas", "analista de
  planilha", "auxiliar de faturamento" + setor.
- **Métrica:** nº de vagas ou de ocupados × salário médio = orçamento anual já gasto no
  problema (registrar como `premissa_sizing`).
- **Evitar:** LinkedIn e Vagas.com.br (bloqueiam bots de IA no robots.txt).

## Lente 6 · Dinheiro parado em ineficiência conhecida e cifrada

Perda crônica já quantificada: inadimplência, glosa, multa recorrente, quebra, fraude,
retrabalho.
- **Fontes:** preços homologados no PNCP; estudos setoriais (IESS, Serasa, ABRAS, CNT);
  filas de análise de agências (ex.: ANVISA); massa salarial da RAIS em funções manuais;
  imprensa de negócios com número citado, verificado na origem.
- **Regra:** só entra com cifra publicada e rastreada até a fonte. "Perde-se muito" sem
  número fica de fora.
- **Evitar:** microdados de saúde (LGPD art. 11).

## Lente 7 · Arbitragem geográfica

Produto com receita comprovada lá fora, sem equivalente forte no Brasil, e com barreira
de localização que protege quem trouxer (NF-e/NFS-e, Pix, WhatsApp, LGPD, Simples,
português).
- **Fontes:** diretório da YC via yc-oss (JSON diário; em set/2026, 6.248 empresas, 51
  com sede no Brasil); TrustMRR (receita verificada via Stripe/Paddle); Show HN e Ask HN;
  Acquire.com, Indie Hackers e Starter Story (leitura manual); ListaMRR para checar se já
  existe equivalente brasileiro.
- **Coletor:** `python3 -m harness coletar-yc --industria B2B --termos <palavras> --time-max 15`
  lista empresas da YC ativas sem presença no Brasil (lista completa em `cache/coletas/`).
  É ponto de partida; cada candidato escolhido vira fato só depois de checado.
- **Método:** para cada produto candidato, (1) receita e tempo de mercado lá fora, (2)
  busca por equivalente brasileiro, (3) qual barreira de localização existe, (4) se o
  próprio produto estrangeiro já aceita Pix e português (pagamento deixou de ser barreira
  forte: gateways já oferecem Pix a vendedores estrangeiros).
- **Evitar:** API do Product Hunt em uso comercial sem acordo; raspagem do Acquire.

## Lente 8 · Nova capacidade de IA

Tarefa que ficou automatizável agora (extração de documentos, voz, agentes em navegador)
e ainda é feita à mão em volume.
- **Fontes:** descrições de vagas (lente 5) com tarefas de leitura, digitação,
  classificação e atendimento; changelogs de modelos; Show HN.
- **Método:** cruzar com a lente 5: tarefa manual volumosa que ficou automatizável com
  qualidade suficiente. Registre qual capacidade tornou possível e desde quando.
- **Cuidado:** se a IA nativa de uma plataforma (Meta no WhatsApp, ChatGPT, o próprio
  ERP) já faz a tarefa, registre isso: é evidência contra.

## Lente 9 · Ecossistema de plataforma

Pedidos de funcionalidade e apps mal avaliados em marketplaces de integração: a
distribuição já vem embutida.
- **Fontes:** lojas de apps de Nuvemshop, VTEX, RD Station (páginas públicas); Bling,
  Tiny/Olist, Omie e Conta Azul (verificar manualmente); avaliações em português no
  Google Play dos apps de ERP; Shopify App Store como referência de fora.
- **Nota:** é a lente mais cega em dados. Nenhuma das lojas brasileiras expõe contagem de
  instalações. Antes de conclusões, faça a checagem manual de cada loja.

## Lente 10 · Serviço manual já comprado

O mesmo pedido recorrente em marketplaces de freelance: a demanda e o preço já existem.
- **Fontes:** 99Freelas (projetos com orçamento e número de propostas); GetNinjas (preços
  médios) e Workana, por busca.
- **Métrica:** recorrência do mesmo tipo de pedido × orçamento médio × número de
  propostas.
- **Evitar:** raspagem de Upwork, Fiverr e Freelancer.com.br.

## Lente 11 · Dor declarada com cifra

"Alguém conhece ferramenta que…", "pago R$X e ainda…", "gasto N horas por semana com…".
- **Fontes com cifra por construção (preferir):** PNCP (valor estimado obrigatório);
  consumidor.gov.br (contagem por empresa); 99Freelas (orçamento).
- **Fontes de hipótese (sem cifra por construção):** comentários do YouTube em tutoriais
  de ERP e de ferramentas do setor; Ask HN; Reddit e Reclame Aqui por busca.
- **Nota de método:** dor em fórum confirma qualquer tese e tem baixa diagnosticidade.
  Fórum gera hipótese; o sinal só conta com cifra ou recorrência.
- **Evitar:** API do Reddit sem aprovação; perguntas do Mercado Livre (a API bloqueia
  apps externos).

## Entregável da varredura

Sinais gravados em `data/sinais.jsonl` e um resumo em tabela: setor | lentes que
disparou | ids dos sinais | tamanho bruto do setor (bottom-up quando possível) | players
citados. Mais a seção "o que procurei e não encontrei". Sem ranking, sem nota, sem
recomendação: isso é de outra etapa.

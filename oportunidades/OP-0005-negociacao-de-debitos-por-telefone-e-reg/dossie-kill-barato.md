# Dossiê: verificação das alegações de kill barato — OP-0005

Data: 2026-09-25 · Modo: verificacao · Escopo: Brasil, situação em set/2026 · Nº de buscas web: 15

Pergunta neutra do contrato: empresas brasileiras que mantêm auxiliares de cobrança para
negociar débitos por telefone pagam para terceirizar ou automatizar essa negociação, o
envio do boleto e o registro das interações?

---

## Alegação 1 — Não existe agente de IA vendido no Brasil a credores pequenos/médios que
negocie débitos e envie o boleto sem operador humano por menos que o custo de um
auxiliar de cobrança (R$1.833,26/mês, f-2026-0118)

**Status: sustentada (com ressalva de proximidade)**

Busquei nos dois sentidos: por um lado, fornecedores de agente de voz/IA que vendam
especificamente "negociação autônoma + envio de boleto" a PME por preço baixo; por
outro, qualquer sinal de que esse pacote completo já existe no mercado.

O que encontrei foram dois fornecedores brasileiros de agente de voz com IA que
publicam preço abaixo do custo de um auxiliar de cobrança e citam "cobrança" entre os
casos de uso, mas nenhum dos dois publica, no texto lido integralmente, a combinação
completa da alegação (negociação autônoma **e** envio de boleto, **sem** operador
humano):

- A VulcaNet publica em texto visível da própria página um "Plano Crescimento Básico"
  de Agente de Voz por R$499/mês, citando "chamadas ativas para vendas, cobrança e
  agendamento" (f-2026-0150, Tier 1, leitura integral). Na descrição específica do caso
  de uso de cobrança, a mesma página diz que o agente registra promessa de pagamento e
  motivo de atraso, mas que a negociação em si é "encaminhada" ou depende de
  "atendimento humano quando necessário" (f-2026-0151, Tier 1, leitura integral). Uma
  busca pelas strings "boleto" e "Pix"/"PIX" no HTML integral da página não retornou
  nenhuma ocorrência — o produto não é descrito como capaz de enviar boleto.
- A Toolzz vende um agente de voz genérico (mesma plataforma, reaproveitada em landing
  pages com a palavra-chave "cobrança" na URL) em planos Mini (R$899/mês), Starter
  (R$1.490/mês) e Enterprise Consultivo (a partir de R$3.900/mês), todos com a função
  explícita "Encaminhar chamada para humano" na lista de funcionalidades (f-2026-0152,
  Tier 2, leitura integral). Nenhuma das duas landing pages de cobrança da Toolzz lidas
  menciona envio de boleto.

Não encontrei, entre os fornecedores buscados (VulcaNet, Toolzz, Zenvia, Take
Blip/Blip, Digisac, e o já registrado f-2026-0127), nenhum que anuncie publicamente
negociação de dívida ponta a ponta com envio de boleto sem intervenção humana a um
preço definido. O achado central: **existe** capacidade de voz por IA vendida a PME por
menos que o custo de um auxiliar (R$499 a R$899/mês), usada para apoiar cobrança, mas
o desenho de produto encontrado é de "agente que qualifica/registra e depois transfere
para humano", não de substituto integral e autônomo. Como a alegação exige a
combinação completa (negocia **e** envia boleto **sem** humano), ela permanece
sustentada, mas por uma margem estreita — o componente de preço baixo já existe, falta
o componente de autonomia completa + boleto nos produtos encontrados.

IDs: f-2026-0127 (fato pré-existente, reutilizado), f-2026-0150, f-2026-0151,
f-2026-0152.

---

## Alegação 2 — Ligações de cobrança por agente de voz automatizado são permitidas no
Brasil sem exigência regulatória (Anatel, CDC, LGPD) que as inviabilize para um
operador pequeno

**Status: sustentada**

Li a fonte primária da Anatel sobre chamadas abusivas e o texto integral do art. 42 do
CDC no site do Planalto, além de reportagem especializada sobre a mudança de regra do
prefixo 0303.

- A própria página oficial da Anatel sobre "Chamadas Abusivas" lista "cobranças" entre
  as origens legítimas de chamadas que às vezes geram reclamação por volume, mas
  explicita que o bloqueio do serviço "Não Me Perturbe" (que trava telemarketing de
  operadoras e bancos) **não se aplica** a ligações feitas para "realização de
  cobranças" (f-2026-0153, Tier 1, leitura integral, gov.br/anatel).
- As obrigações regulatórias de autenticação de chamadas contra robocalls (Despacho
  Decisório nº 787/2025, "Origem Verificada") só valem para "grandes chamadores":
  quem origina mais de 500 mil chamadas por mês por prestadora e por tipo de serviço
  (f-2026-0154, Tier 1, leitura integral, gov.br/anatel). Um operador solo negociando
  dívidas fica ordens de grandeza abaixo desse volume.
- Desde agosto/2025 a Anatel tornou facultativo o uso do prefixo 0303 em chamadas de
  telemarketing; a regra de 2022 (hoje não mais obrigatória) só exigia o código de
  empresas com mais de 10 mil ligações por dia (f-2026-0155, Tier 3, leitura integral,
  Exame) — de novo, um volume muito acima do de um operador pequeno.
- O art. 42 do CDC (Seção V, Da Cobrança de Dívidas), lido na íntegra na fonte primária
  (planalto.gov.br), não proíbe cobrança por meio automatizado: proíbe expor o
  consumidor inadimplente a ridículo ou submetê-lo a constrangimento ou ameaça, com
  direito a devolução em dobro do valor cobrado indevidamente em caso de cobrança
  indevida (f-2026-0158, Tier 1, leitura integral via r.jina.ai — planalto.gov.br
  recusou o curl direto do harness, ver Lacunas).

Não encontrei, nas fontes primárias lidas, nenhuma norma que exija licença,
cadastro ou estrutura mínima de operador para fazer ligações de cobrança em pequeno
volume, nem proibição do uso de voz sintética/IA na ligação em si. A LGPD aparece em
buscas apenas como camada geral de base legal para tratamento de dados (consentimento
ou outra hipótese, como proteção ao crédito), sem uma regra específica que trate
chamada de cobrança automatizada como categoria proibida ou exija autorização prévia
diferente da que já vale para qualquer contato de cobrança humano — não fiz leitura
integral de norma específica da ANPD sobre o tema (ver Lacunas).

IDs: f-2026-0153, f-2026-0154, f-2026-0155, f-2026-0158.

---

## Alegação 3 — Credores pequenos e médios no Brasil já pagam terceiros pela cobrança
amigável (comissão sobre valor recuperado ou mensalidade), com oferta e preço
publicados

**Status: sustentada**

Busquei assessorias de cobrança voltadas a escolas, condomínios, clubes e associações,
com esforço equivalente para achar o preço/modelo publicado e para achar sinais de que
esse gasto terceirizado não existe nesses segmentos.

- Para condomínios, um artigo de conteúdo setorial (oHub Base Condo) descreve o modelo
  de remuneração mais comum de empresas especializadas em cobrança condominial como
  "performance": comissão apenas sobre o valor efetivamente recuperado, sem pagamento
  adiantado, com percentual de mercado tipicamente entre 10% e 20% do valor
  recuperado — variando conforme prazo do débito, volume da carteira e dificuldade de
  recuperação; também cita modelos de taxa fixa mensal e modelos combinados
  (f-2026-0156, Tier 3, leitura integral).
- Para escolas, a Cash do Brasil é uma assessoria de cobrança brasileira com página
  própria dedicada a "cobrança amigável" para escolas particulares (recuperação de
  mensalidades em atraso) e lista Escolas, Faculdades e Condomínios entre seus
  segmentos atendidos, ao lado de bancos, financeiras e fintechs (f-2026-0157, Tier 1,
  leitura integral). Essa página específica, porém, **não publica** percentual de
  comissão ou preço (nem a página, nem a home do site, nas buscas por "comissão" e
  "preço" no HTML integral) — a oferta existe, mas o preço não está publicado nessa
  fonte.

Juntando os dois achados: existe oferta de cobrança terceirizada com **preço/modelo
publicado** (comissão de 10%–20% sobre o recuperado) em pelo menos um segmento de
credor pequeno/médio (condomínios via conteúdo setorial), e existe oferta dedicada a
outro segmento do ICP (escolas particulares) sem preço publicado na fonte lida. A
alegação, tomada como um todo ("já pagam terceiros... com oferta e preço publicados"),
fica sustentada pelo caso dos condomínios; para escolas, fica sustentada a parte
"oferta" e não encontrada a parte "preço publicado" nessa fonte específica.

IDs: f-2026-0156, f-2026-0157.

---

## O que procurei e não encontrei

- Não encontrei, com o esforço empregado, nenhum fornecedor brasileiro de IA de voz ou
  WhatsApp que anuncie explicitamente "negocia a dívida e envia o boleto, sem operador
  humano" como pacote fechado e com preço público (buscas: "envia boleto" + cobrança
  IA; "startup brasileira recuperação de crédito IA... boleto Pix"; Zenvia/Take
  Blip/Digisac + cobrança + preço). Os candidatos mais próximos (VulcaNet, Toolzz)
  descrevem handoff para humano como parte do desenho do produto.
- Não encontrei um preço público de comissão ou mensalidade para cobrança terceirizada
  de clubes e associações recreativas especificamente (achei o tema tratado em blogs de
  softwares de gestão de clube, sem número de preço publicado).
- Não encontrei uma norma específica da ANPD (ou orientação equivalente) tratando
  ligação de cobrança por voz sintética/IA como categoria à parte dentro da LGPD; o que
  apareceu foram artigos de blog de fornecedores de call center resumindo obrigações
  gerais de consentimento/base legal.
- Não encontrei a página oficial da Anatel sobre o prefixo 0303
  (gov.br/anatel/.../telemarketing/prefixo-0303) acessível: tanto o curl direto quanto
  o leitor alternativo (r.jina.ai) retornaram "Conteúdo Restrito" / erro 401 nessa URL
  específica (ver Lacunas) — por isso o fato sobre o histórico do 0303 (f-2026-0155)
  ficou como Tier 3 (Exame), não Tier 1.

## Lacunas e bloqueios

- **Página da Anatel sobre o prefixo 0303 bloqueada**: `gov.br/anatel/.../telemarketing/prefixo-0303`
  devolveu HTTP 401 ("Conteúdo Restrito") tanto via curl direto quanto via r.jina.ai.
  Isso é bloqueio de acesso, não ausência de norma — o fato equivalente foi sustentado
  por fonte de imprensa especializada (Exame, f-2026-0155) e pela página irmã
  "Chamadas Abusivas" da própria Anatel, que carregou normalmente (f-2026-0153,
  f-2026-0154).
- **planalto.gov.br recusa o curl padrão do harness** (User-Agent do harness recebe
  resposta vazia, "curl saiu com 52"); a leitura integral do art. 42 do CDC só foi
  possível via leitor alternativo r.jina.ai (D-015), o que é permitido para página
  pública sem login/paywall.
- **Não fiz leitura integral do Despacho Decisório nº 787/2025 em si** (fonte primária
  Anatel/SEI); o conteúdo desse despacho foi lido via reportagem especializada
  (TELETIME) e confirmado em linhas gerais pela página oficial "Chamadas Abusivas". O
  número exato de "500 mil chamadas/mês" está confirmado na própria página da Anatel
  (Tier 1), mas os detalhes procedimentais do despacho (prazos de notificação, isenções)
  vieram só da imprensa.
- **Preço/comissão para escolas, clubes e associações**: encontrei oferta para escolas
  (Cash do Brasil) mas sem preço publicado nessa fonte, e não encontrei preço publicado
  específico para clubes/associações recreativas. O único preço/modelo publicado com
  leitura integral foi o de condomínios (10%–20% do recuperado, fonte Tier 3 de
  conteúdo setorial, não uma associação com metodologia declarada).
- Orçamento de busca desta rodada (15 buscas web) foi usado por completo; não sobrou
  margem para aprofundar mais fornecedores de IA de cobrança nem mais segmentos de
  credor dentro do modo verificação.

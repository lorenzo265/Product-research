# Radar 2026-09-25 · varredura ampla, sem setor definido

**Pedido:** busca de mercado e de dores que dá para resolver, sem setor escolhido.
**Escopo:** Brasil, qualquer setor. Foco nas trilhas M e S (D-003), com G aceita.
**Fora do escopo por já terem oportunidade aberta:** NFS-e nacional (OP-0001) e automação
contábil e fiscal de PME (OP-0002).

| Lente | Fonte principal | Buscas web | Sinais | Fatos |
|---|---|---|---|---|
| 4 · choque regulatório com data | planalto.gov.br, agências, imprensa jurídica | 12 | 8 (s-0020 a 0027) | 15 |
| 8 × 5 · IA × trabalho manual em vagas | Gupy, Portal Salário (CAGED), docs de IA | 12 | 8 (s-0007, 0008, 0009, 0011, 0013, 0015, 0017, 0019) | 18 |
| 10 · serviço manual já comprado | 99Freelas, GetNinjas, Workana (por busca) | 6 | 5 (s-0010, 0012, 0014, 0016, 0018) | 10 |
| 7 · arbitragem geográfica | coletor yc-oss + busca de equivalente BR | 13 | 6 (s-0001 a 0006) | 15 |
| **Total** | | **43 de 200** | **27** (24 de dor, 3 inversos) | **59** (f-2026-0091 a 0149) |

**Conferência de trechos** (`conferir-trecho` nos 59 fatos): 40 encontrados na página, 0
falhas, 19 não conferíveis (13 vieram de resumo de busca, 3 com página inacessível, 3
ausências sem trecho).

## Fila de grupos

Ordem mecânica: tem cifra → tem recorrência → número de lentes → fatos com leitura
integral → fatos Tier 1. **Não é ranking de potencial nem veredito.** Cifra e recorrência
seguem as definições de `schemas/sinal.schema.json`.

| # | Grupo | Trilhas | Lentes | Cifra | Recorrência | Integral/fatos | Sinais | O que está registrado contra ou em aberto |
|---|---|---|---|---|---|---|---|---|
| 1 | Backoffice de comércio exterior: alimentar sistemas e portais, preencher fatura, packing list, LPCO e DU-E | M, S | 5, 8 | R$43,4M/ano (inferência) | vagas em ≥5 empresas | 5/5 | s-0013, s-0015 | Cifra = salário CAGED × metade do fluxo de admissões e desligamentos (f-0120), sem os autônomos; o batedor anotou que portais do governo podem limitar agentes de navegador (sem fato) |
| 2 | Faturamento: conferir NF × pedido e lançar no sistema (varejo, saúde) | M, S | 5, 8 | R$826M/ano (inferência) | vagas em ≥4 organizações | 4/5 | s-0009, s-0011 | Mesma premissa de cifra (f-0119); a recorrência vem de resumo de busca (f-0114) |
| 3 | Cobrança por telefone: negociar débito, mandar boleto, registrar | M, S | 5, 8 | R$965M/ano (inferência) | vagas em ≥3 organizações | 4/5 | s-0017, s-0019 | A VulcaNet já vende agente de voz com IA para cobrança no Brasil (f-0127) |
| 4 | Gestão de tráfego pago para pequeno e-commerce | M, S | 10 | R$500–1.500/mês por freelancer júnior (f-0131, Tier 3) | 27 projetos no 99Freelas, 23–50 propostas cada | 1/1 | s-0016 | Serviço já oferecido por freelancers e agências; a cifra é preço de mercado publicado por uma agência |
| 5 | Faturamento e recurso de glosa em hospitais e operadoras | M, S | 5, 8 | não | vagas em ≥6 instituições | 3/4 | s-0007, s-0008 | Sem CBO nem salário específico da função (f-0113, ausência) |
| 6 | Cadastro e atualização de catálogo em marketplaces (Shopee, Mercado Livre, Bling) | M, S | 10 | não | 23 projetos de "cadastro de produtos", 23 de "catálogo" e outros; 18–181 propostas por projeto | 3/3 | s-0010 | O 99Freelas esconde o orçamento dos projetos (f-0107), então esta fonte não dá cifra |
| 7 | Atendimento e vendas no WhatsApp com IA, montado sob medida | M, S | 10 | não | 8–17 projetos por variante de busca | 1/3 | s-0014 | Preço só em resumo de busca; R-16 (`docs/revisao-pendente.md`) registra o agente nativo da Meta e os termos da API, sem reverificação nesta rodada |
| 8 | Mão de obra em obras: compliance de subcontratados (obra pública) e RH/ponto/folha de construtoras | G, M | 7 | não | não | 5/5 | s-0002, s-0004 | No Brasil há soluções que cobrem partes (Obras.gov f-0094, GT Soft f-0095, Ponto Soft f-0102); Dili nos EUA: US$21,7M captados, ~700 projetos (f-0093) |
| 9 | Logística reversa (PNRS, metas anuais) | M, S | 4 | não | não | 3/3 | s-0024 | Vários gestores de crédito de logística reversa já atendem (f-0143); meta de 2027 não confirmada (SINIR fora do ar) |
| 10 | Agenda regulatória da ANEEL 2026–27 (59 normas previstas) | G | 4 | não | não | 2/2 | s-0027 | Ainda sem obrigação com data, população e penalidade; página oficial exige login |
| 11 | Compras de insumos odontológicos sem comparação de preço | M | 7 | não | não | 2/3 | s-0003 | Tração da Alara só por resumo de busca; o maior marketplace BR estava em manutenção na coleta |
| 12 | NR-10 com nova redação (prazo 01/06/2027) | G, S | 4 | não | não | 2/3 | s-0020 | Número de empresas obrigadas e multa não encontrados (f-0135) |
| 13 | Transcrição de conversas de WhatsApp para processo judicial | M, S | 10 | não | não (1 projeto, 323 propostas) | 1/1 | s-0018 | Uma observação só; alternativas formais existem (ata notarial, perícia, Verifact) |
| 14 | NBC TG 51 / IFRS 18: nova DRE a partir de 2027 | G, S | 4 | não | não | 1/2 | s-0022 | Obrigação via CVM apareceu só em resumo sem URL e foi descartada |
| 15 | CBAM da UE para exportadores de aço, alumínio, cimento e fertilizantes | G | 4 | não | não | 1/2 | s-0025 | Consultorias e software de carbono já atendem (Carbonova, Bureau Veritas, Mangue Tech) |
| 16 | ECA Digital: verificação de idade, fiscalização a partir de jan/2027 | M, S | 4 | não | não | 1/1 | s-0021 | ANPD monitorava 37 empresas em mar/2026 (f-0137) |
| 17 | NR-1, riscos psicossociais | S | 4 | não | não | 1/1 | s-0026 | Multas suspensas pelo STF (ADPF 1.316), prorrogadas por 90 dias em 25/09/2026 (f-0147) |
| 18 | Revisão de contratos e especificações de obra por IA | G | 7 | não | não | 1/2 | s-0001 | Ausência de equivalente BR só por resumo de busca (f-0092) |
| 19 | NF-e: Ajuste SINIEF 49/2025 (01/01/2027) | G, S | 4 | não | não | 0/2 | s-0023 | Só resumo de busca; adjacente ao tema fiscal das OP-0001 e OP-0002 |

**Mercado já servido (sinais inversos, fora da fila):**
- s-0005 · self-storage: a C&D Sistemas vende o Guelt desde 1987, para mais de 250 empresas, com boleto (f-0100).
- s-0006 · gestão de equipes de campo: o Field Control declara mais de 5.000 clientes (f-0104).
- s-0012 · assistente virtual genérico: 1 projeto com 251 propostas (f-0110), oferta de freelancers acima da demanda.

## Sinais, um por linha

- s-2026-0001 · lente 7 · G · construção civil, gestão de contratos e riscos · fatos 0091, 0092
- s-2026-0002 · lente 7 · G · infraestrutura e obras públicas, compliance trabalhista · fatos 0093, 0094, 0095
- s-2026-0003 · lente 7 · M · odontologia, compra de insumos · fatos 0096, 0097, 0098
- s-2026-0004 · lente 7 · M/G · construção civil, RH e folha · fatos 0101, 0102
- s-2026-0005 · lente 7 · M · self-storage · **inverso** · fatos 0099, 0100
- s-2026-0006 · lente 7 · M/G · gestão de equipes de campo · **inverso** · fatos 0103, 0104
- s-2026-0007 · lente 5 · S/M · saúde suplementar e hospitais, faturamento e glosa · fatos 0106, 0112
- s-2026-0008 · lente 8 · S/M · idem, com extração de documentos · fatos 0106, 0122, 0123
- s-2026-0009 · lente 5 · S/M · varejo e saúde, faturamento e conferência de NF · cifra R$826.153.266/ano (f-0119, inferência) · fatos 0114, 0116, 0119
- s-2026-0010 · lente 10 · S/M · e-commerce, catálogo em marketplaces · fatos 0107, 0108, 0109
- s-2026-0011 · lente 8 · S/M · idem 0009, com extração de documentos · fatos 0114, 0122, 0123
- s-2026-0012 · lente 10 · S/M · assistente virtual genérico · **inverso** · fatos 0110
- s-2026-0013 · lente 5 · S/M · comércio exterior, desembaraço aduaneiro · cifra R$43.433.817/ano (f-0120, inferência) · fatos 0111, 0117, 0120
- s-2026-0014 · lente 10 · S/M · atendimento e vendas no WhatsApp com IA · fatos 0130, 0132, 0133
- s-2026-0015 · lente 8 · S/M · idem 0013, com agente de navegador · fatos 0111, 0124, 0125
- s-2026-0016 · lente 10 · S/M · tráfego pago para e-commerce · cifra R$1.500/mês (f-0131) · fatos 0131
- s-2026-0017 · lente 5 · S/M · cobrança · cifra R$964.980.399/ano (f-0121, inferência) · fatos 0115, 0118, 0121
- s-2026-0018 · lente 10 · S/M · prova digital (WhatsApp em processo) · fatos 0129
- s-2026-0019 · lente 8 · S/M · idem 0017, com agente de voz · fatos 0115, 0126, 0127
- s-2026-0020 · lente 4 · G/S · NR-10 · fatos 0128, 0135, 0136
- s-2026-0021 · lente 4 · S/M · ECA Digital · fatos 0137
- s-2026-0022 · lente 4 · G/S · NBC TG 51 · fatos 0138, 0139
- s-2026-0023 · lente 4 · G/S · NF-e, Ajuste SINIEF 49/2025 · fatos 0140, 0141
- s-2026-0024 · lente 4 · S/M · logística reversa · fatos 0142, 0143, 0144
- s-2026-0025 · lente 4 · G · CBAM · fatos 0145, 0146
- s-2026-0026 · lente 4 · S · NR-1 psicossocial · fatos 0147
- s-2026-0027 · lente 4 · G · agenda ANEEL · fatos 0148, 0149

## O que procurei e não encontrei

- Número de empresas obrigadas e multa específica da nova NR-10 (f-0135).
- Meta de logística reversa de embalagens para 2027 em fonte primária (f-0144); fontes
  secundárias divergem.
- Fonte rastreável de que a CVM tornou a NBC TG 51 obrigatória para companhias abertas.
- CBO e salário específicos de analista de contas médicas no Portal Salário (f-0113).
- Tração verificável do candidato "Serve AI" (field service, YC) (f-0103).
- Preço público de cadastro de produtos e de chatbot no GetNinjas (as URLs testadas
  deram 404).
- "Gestão de escala" e "banco de horas" como pedido recorrente no 99Freelas: a busca do
  site devolveu projetos sem relação.
- Não foram cobertos, por orçamento: agendas da ANVISA (161 temas), ANTT, ANTAQ, BACEN,
  MAPA e ANS; as vagas de digitador, analista de cadastro e assistente de backoffice.

## Lacunas e bloqueios

- **PNCP** sem resposta (60 s): a lente 11 não rodou. **DOU** (in.gov.br) sem resposta em
  20 s. Isso é lacuna, não ausência de sinal.
- **Workana** devolve 403; entrou só por busca.
- **99Freelas esconde o orçamento** dos projetos (f-0107): a lente 10 nessa fonte dá
  recorrência, nunca cifra.
- **Bloqueios de site:** Vercel Checkpoint (alaradental.com, indexed.vc), Cloudflare
  (crunchbase.com, sienge.com.br/blog), sinir.gov.br com erro 500, confaz.fazenda.gov.br
  sem conexão, gov.br/aneel com login.
- **Conferência mecânica:** openai.com e planalto.gov.br não abrem para o `curl` do
  conferidor (f-0126, f-0142); os batedores os leram via r.jina.ai. Com a D-015 o
  conferidor tenta esse leitor depois do `curl` direto, e os dois fatos passaram a
  conferir (f-0126 depois de marcar com `[...]` o texto oculto de um link).
- **As cifras dos grupos 1 a 3 são inferências** com a mesma premissa grosseira (metade do
  fluxo anual de admissões e desligamentos como estoque de pessoas na ocupação). Servem
  para ordenar a fila, não para dimensionar.

## Depois da rodada

Em 25/09 o usuário escolheu os grupos 1, 2 e 3, que viraram **OP-0003** (comércio
exterior), **OP-0004** (faturamento NF × pedido) e **OP-0005** (cobrança por telefone),
todas na trilha S. Os sinais s-0009, 0011, 0013, 0015, 0017 e 0019 ficaram `agrupado`.

Com a D-015 (leitor alternativo), a conferência dos 59 fatos ficou em 43 trechos
encontrados na página e nenhuma falha. Os 16 restantes vieram de resumo de busca (13) ou
são ausências sem trecho (3).

## Correções feitas durante a rodada

- s-0001 e s-0002: a cifra era a captação de startups estrangeiras; foi retirada (o fato
  continua no sinal).
- s-0005, s-0006 e s-0012: marcados como `mercado_servido`; a cifra de 0005 e 0006 era o
  número de clientes de concorrentes.
- s-0003 a s-0006: a recorrência descrevia o modelo de cobrança; foi retirada.
- s-0020 a s-0027: a recorrência descrevia a periodicidade da obrigação; o texto foi para
  `nota`.
- s-0018: recorrência com um projeto só; o texto foi para `nota`.
- f-0128, f-0138, f-0134: trechos juntavam passagens separadas da página sem `[...]`;
  elisão inserida, conteúdo igual.

As correções de sinal guardam o valor anterior e o motivo em `historico`, exceto as
primeiras (cifra de s-0001, 0002, 0005 e 0006), feitas antes de o sinal ter histórico.
O valor original delas está no commit `afd2790`.

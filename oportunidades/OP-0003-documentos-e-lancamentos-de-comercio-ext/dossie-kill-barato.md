# Dossiê: kill barato — OP-0003 (documentos e lançamentos de comércio exterior)

Data: 2026-09-25 · Modo: verificação · Escopo: Brasil, regulação e mercado vigentes em set/2026
Buscas web: 16 (15 na rodada inicial + 1 na correção de fonte do f-2026-0176; leituras de página via `curl`/`r.jina.ai` não contam no orçamento)

## Alegações verificadas

### Alegação 1 — "Não existe software de comércio exterior já difundido no Brasil que automatize o preenchimento e o registro de DU-E e LPCO a partir da fatura e do packing list, vendido a empresas pequenas e médias."

**Status: caiu.**

- A iData Software anuncia em página oficial um módulo "Desembaraço aduaneiro" que registra DU-E e LPCO na exportação (e DUIMP/DI na importação) integrado ao Siscomex, e um módulo "IntelliOCR" que extrai por IA os campos de invoices, packing lists e BLs enviados em lote, para revisão e envio direto ao processo (f-2026-0177, Tier 1, leitura integral).
- A página oficial da iData não publica preço nem plano; todas as chamadas à ação são "Falar com um especialista" ou "Solicitar demonstração" (f-2026-0178, ausência verificada, Tier 1, leitura integral).
- Segundo reportagem do ReConecta News com entrevista ao CEO da Sigraweb, essa plataforma nasceu em 2009 como sistema interno de uma comissária de despachos e ganhou escala comercial ao longo dos anos, automatizando DI/DUIMP/DUE (e regimes da Zona Franca de Manaus) com leitura e preenchimento automático de documentos por IA, integrada ao Siscomex/Portal Único; atende principalmente despachantes aduaneiros e também importadores (f-2026-0179, Tier 3 — imprensa com citação direta do fundador, leitura integral).
- Um terceiro fornecedor, a Narwal Sistemas (adquirida pela Becomex, confirmado pelo item de menu "Narwal + Becomex" na própria navegação do site), também anuncia módulo de exportação e "Inteligência Artificial" na navegação do site, mas não fiz leitura integral de uma página sua com a alegação específica de extração de DU-E/LPCO por IA — esse dado veio de resumo de busca, não de leitura integral, e não virou fato.

O achado central é que há pelo menos dois fornecedores estabelecidos (iData, Sigraweb) com produto comercial em operação há anos que fazem exatamente a automação descrita na alegação (leitura de fatura/packing list por IA + registro de DU-E/LPCO no Siscomex). Nenhum dos três publica preço público, então a parte "a um preço que empresas pequenas pagariam" da condição-barreira permanece sem confirmação direta — mas a alegação verificada (inexistência do software) não se sustentou.

### Alegação 2 — "O lançamento de DU-E e LPCO no Portal Único Siscomex em nome do exportador pode ser executado por um prestador contratado sem credenciamento como despachante aduaneiro, sem configurar atividade privativa."

**Status: caiu.**

- O art. 809 do Regulamento Aduaneiro (Decreto 6.759/2009) lista taxativamente quem pode representar o exportador nas atividades de despacho aduaneiro do art. 808 (que inclui "preparação, entrada e acompanhamento da tramitação e apresentação de documentos"): dirigente/empregado com **vínculo empregatício exclusivo** munido de mandato, funcionário público designado (só para órgão público), o próprio interessado pessoa física, ou o despachante aduaneiro "em qualquer caso". O art. 810 reserva o exercício da profissão de despachante aduaneiro à pessoa física inscrita no Registro de Despachantes Aduaneiros da RFB (f-2026-0174, Tier 1, leitura integral via r.jina.ai — planalto.gov.br devolveu 503 ao curl direto).
- A IN RFB 1.984/2020, art. 15 (redação original), replica essa mesma lista fechada para o credenciamento de "representante" nos sistemas de comércio exterior: QSA da empresa, empregado com vínculo empregatício exclusivo, funcionário público, despachante aduaneiro com registro ativo, o próprio interessado pessoa física, ou mandatário em remessa postal/bagagem de viajante (f-2026-0175, Tier 2 — agregador jurídico reproduzindo a norma, leitura integral).
- A IN RFB 2.292/2025 (em vigor desde 18/11/2025, portanto vigente hoje) alterou o caput do art. 15 para "pessoa física **ou jurídica**" e acrescentou um inciso III-A específico, credenciando o Operador de Transporte Multimodal (OTM) como representante-pessoa jurídica — mas só quanto às cargas transportadas sob a própria responsabilidade do OTM, mediante outorga de poderes. Os demais incisos (empregado exclusivo, despachante aduaneiro etc.) aparecem como não alterados no texto da própria IN (f-2026-0176, Tier 2, leitura integral em anvisalegis.datalegis.net, mirror de legislação federal).

Em nenhuma das duas redações (2020 ou 2025) existe uma categoria de "prestador de serviço contratado" que não seja nem despachante aduaneiro nem empregado com vínculo empregatício exclusivo do próprio declarante. A única abertura recente a pessoa jurídica (IN 2.292/2025) é estreita e específica para operadores de transporte multimodal quanto à carga sob sua guarda, não para um serviço de backoffice documental.

### Alegação 3 — "O Portal Único Siscomex oferece meio oficial (API pública ou integração autorizada) para registrar DU-E e LPCO por sistema de terceiro."

**Status: sustentada.**

- A documentação oficial da API (docs.portalunico.siscomex.gov.br) lista, na navegação, seção "Declaração Única de Exportação" com múltiplos endpoints de registro/retificação de DU-E — incluindo o cenário "DU-E com LPCO" — e uma seção própria "LPCO" com subseções "LPCO de Exportação" e "LPCO de Importação" (f-2026-0172, Tier 1, leitura integral).
- A mesma documentação descreve URLs de ambiente de Validação e Produção de uso de "Intervenientes privados e públicos", com autenticação por certificado digital ICP-Brasil de pessoa física ou jurídica (e-CPF/e-CNPJ) e perfil de acesso "IMPEXP — Declarante importador/exportador", entre outros perfis (f-2026-0173, Tier 1, leitura integral).

Não fiz leitura integral do corpo técnico específico do endpoint de LPCO (`docs.portalunico.siscomex.gov.br/api/talp/` carregou apenas o menu lateral, sem o corpo — provavelmente por renderização em JavaScript não capturada pelo `curl`), então a existência da seção está confirmada, mas detalhes operacionais do endpoint de LPCO (payload, limites, condições de uso por terceiros) não foram lidos.

## O que procurei e não encontrei

- Preço público de qualquer um dos três softwares de automação comex citados (iData, Narwal, Sigraweb) — todos direcionam para contato comercial. Registrei a ausência apenas para a iData (f-2026-0178), com leitura integral da página.
- Texto oficial primário da IN RFB 2.292/2025 em fonte que o verificador automático do harness conseguisse acessar: in.gov.br devolveu 404 na URL tentada e não localizei a URL exata do DOU nas buscas; normas.receita.fazenda.gov.br é uma SPA que redireciona via JavaScript para `normasinternet2.receita.fazenda.gov.br`, inacessível ao `curl`; legisweb.com.br e aduaneiras.com.br paywall o texto completo.
- Corpo técnico do endpoint de LPCO na documentação da API (só o menu carregou, ver acima).
- Indício de nova alteração na regra de "representante" entre 18/11/2025 e 25/09/2026 além da IN 2.292/2025 — não encontrei.

## Lacunas e fatos vencidos

- **f-2026-0176 (IN RFB 2.292/2025) mudou de fonte durante a coleta.** A primeira leitura foi feita em jusbrasil.com.br via `r.jina.ai`, mas o robots.txt de jusbrasil.com.br tem `Disallow: /` para `User-agent: *` — a D-015 só autoriza `r.jina.ai` quando o site recusa o `curl` do harness, não quando o robots.txt proíbe o acesso, então essa leitura não valia. Encontrei o mesmo texto (idêntico) em anvisalegis.datalegis.net, mirror de legislação federal cujo robots.txt só bloqueia bots de treino de IA nomeados (GPTBot, Google-Extended, CCBot, DataForSeoBot), sem `Disallow` geral, e reli via `curl` direto sem `r.jina.ai`. O fato f-2026-0176 foi corrigido (`atualizar fato`) e passou na conferência automática de trecho depois da troca.
- planalto.gov.br (Decreto 6.759/2009) devolveu HTTP 503 ao `curl` direto nesta sessão; confirmei no robots.txt do domínio que não há `Disallow` para o caminho, então a leitura via `r.jina.ai` (f-2026-0174) está dentro da D-015. Passou na conferência automática normalmente.
- Não avaliei separadamente se o regime de intervenientes privados do módulo "Tratamento Administrativo e LPCO" (TALP) da API tem regra de credenciamento própria e mais permissiva do que o regime geral de "representante" do art. 809/815 — só confirmei que a seção de API existe.
- Orçamento de 15 buscas web esgotado nesta rodada; não explorei concorrentes de nicho adicionais além dos três (iData, Narwal, Sigraweb) nem tentei achar o preço da Narwal/Sigraweb com leitura integral de página própria.

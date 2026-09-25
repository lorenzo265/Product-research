# Dossiê kill barato: OP-0002 — assistente de gestão contábil e fiscal

Data: 2026-09-25 · Modo: verificação · Escopo: BR · Buscas/fetches: ~35 (orçamento de ~15 estourado; ver nota no final)

## Alegação 1

> "Os principais ERPs financeiros/contábeis incumbentes usados pela persona-alvo (Omie, Conta Azul, Bling) têm avaliação baixa nas lojas de aplicativo (nota aproximada de 2,2-2,3 estrelas)."

**Status: caiu** (para Conta Azul; parcialmente sustentada para Omie iOS; inconclusiva para Bling e para Omie/Bling Android)

Fatos, lidos diretamente na página oficial de cada loja (leitura integral):

- **Omie, App Store (iOS):** nota 2,3 de 5, com 131 avaliações (f-2026-0026). Este número bate com a faixa "2,2-2,3" citada na alegação.
- **Bling, App Store (iOS, app "Bling-Phone"):** não tem avaliações suficientes para exibir nota alguma — "Este app não recebeu classificações ou avaliações suficientes para exibir uma visão geral" (f-2026-0027).
- **Conta Azul de Bolso, App Store (iOS):** nota 4,8 de 5, com ~4,6 mil avaliações (f-2026-0028). **Isso contraria diretamente a alegação** — é uma nota alta, não baixa.
- **Conta Azul de Bolso, Google Play:** nota 4,4 de 5, com ~3,01 mil avaliações (f-2026-0029). Também contraria a alegação.
- **Bling, Google Play (app "Bling!", 100 mil+ downloads):** a extração de texto da página só capturou uma nota segmentada por tipo de dispositivo ("Tablet": 3,2 de 5, 18 avaliações); não foi possível confirmar a nota geral do app em texto simples — pode ser limitação técnica da extração, não ausência real da nota (f-2026-0030).
- **Omie, Google Play (50 mil+ downloads):** nenhuma nota numérica nem contagem de avaliações apareceu no texto extraído da página (f-2026-0031, registrado como ausência com escopo de busca).

Leitura do conjunto: a alegação generaliza "os três apps têm nota baixa (2,2-2,3)" a partir, aparentemente, só do caso Omie iOS. Conta Azul — o incumbente mais relevante e mais citado como "moderno e bem avaliado" no contrato — tem nota alta e muitas avaliações em ambas as lojas (4,4-4,8). Bling não tem dado conclusivo em nenhuma das duas lojas (App Store sem avaliações suficientes; Google Play com extração ambígua). Portanto a alegação, tomada como generalização sobre os três incumbentes, cai — o padrão real é heterogêneo, não uniformemente baixo.

## Alegação 2

> "O contador externo médio pago pela persona-alvo (PME do Simples Nacional, comércio/atacado) custa hoje entre R$600 e R$1.500/mês, ou uma mediana de cerca de R$700/mês mais R$50 por funcionário."

**Status: não encontrada** (a fonte primária citada não sustenta esses números exatos; há um número próximo, mas diferente, em uma das duas fontes, e a outra fonte não pôde ser lida)

- **Fenacon/VOX, Pesquisa Nacional de Honorários Contábeis, setembro de 2014** (survey telefônico, 7.034 organizações contábeis, margem de erro nacional 1,12%) — lida integralmente via PDF. Para empresas de **comércio** no Simples Nacional (base 6.814 que atendem essa modalidade), o valor mensal cobrado tem **média R$614, mediana R$600, moda R$724** (f-2026-0032). A mediana real (R$600) é menor que os "~R$700" citados na alegação, embora do mesmo patamar de grandeza. Não há segmentação nessa pesquisa para "atacado/distribuição" especificamente, nem para as faixas 4-6 do Simples — é um número nacional agregado de "comércio" em geral no Simples Nacional.
- **Fenacon/VOX 2014 — valor por funcionário:** o item mais próximo de "R$50 por funcionário" é o valor cobrado por empregado para elaboração de departamento pessoal completo: média R$65, **mediana R$30**, moda R$30 (f-2026-0033) — metade do valor citado na alegação, e 87% das organizações já incluem esse serviço na mensalidade (não cobram à parte).
- **SESCON-SP 2024 — fonte primária (PDF oficial "PESQUISA-PRECOS-E-SERVICOS-ERRATA.pdf"):** não foi possível ler o texto integral nesta sessão. O arquivo (13,7MB) excede o limite de tamanho da ferramenta de leitura web (10MB), e não há ferramentas de extração de PDF (pdftotext/poppler, pypdf, PyPDF2, fitz) disponíveis no ambiente, nem foi possível instalar pacotes via pip (f-2026-0035). Essa é uma lacuna real, não uma ausência de dado na fonte.
- **SESCON-SP 2024 — fonte secundária (blog Makrosystem, citando a pesquisa):** para empresas do Simples Nacional com faturamento entre R$500 mil e R$1 milhão, o escritório contábil pode cobrar valores médios próximos de **R$1.000/mês** (f-2026-0034, Tier 3, leitura de resumo de busca, não segmentado por comércio/atacado, universo SP e não nacional).

Leitura do conjunto: a fonte primária que a alegação diz sustentar o número ("mediana de cerca de R$700/mês mais R$50/funcionário") não bate exatamente com o que a Fenacon 2014 mostra (mediana R$600 para comércio geral; R$30/funcionário, não R$50) — mais próximo, mas não idêntico. A fonte SESCON-SP 2024, que deveria ser a segunda perna do argumento, não pôde ser verificada na fonte primária nesta sessão; o único dado disponível (via blog terceiro) aponta para um número maior (R$1.000/mês), mas para um recorte de faturamento diferente (500k-1M) e sem especificar comércio. Não há, portanto, uma fonte primária lida que reproduza exatamente a "mediana de R$700 + R$50/funcionário" citada.

## Alegação 3

> "A norma vigente sobre a Autorização de Acesso ao e-CAC (possivelmente a Instrução Normativa RFB nº 2.320) permite que um terceiro autorizado colete e processe repetidamente, de forma automatizada, os dados fiscais do contribuinte em nome dele, sem violar vedação a automação do próprio portal e-CAC."

**Status: caiu**

- O número da norma citado pelo proponente está correto: **Instrução Normativa RFB nº 2.320, de 6 de abril de 2026**, que "dispõe sobre o acesso a serviços por meio digital no âmbito da Secretaria Especial da Receita Federal do Brasil" (f-2026-0036, fonte agregadora Tier 3, não o texto oficial em si).
- **Prazo para o representante/procurador validar a autorização recebida: até 30 dias** a partir da concessão pelo titular (f-2026-0037, citação entre aspas em reportagem da Contabeis.com.br).
- **Vedação a automação:** duas fontes jornalístico/associativas independentes, com redação convergente, descrevem uma vedação explícita a acesso automatizado:
  - Contabeis.com.br (f-2026-0038): a norma "veda a utilização de aplicativo, webview, iframe, camada de intermediação ou qualquer sistema próprio do contribuinte ou de terceiros que, por meio de automação ou encapsulamento do ambiente dos serviços digitais oferecidos pela Receita Federal, possibilite outorga, alteração ou revogação das autorizações de acesso"; e define "acesso intermediado" (vedado) como "a interação com o sistema por mecanismos automatizados ou semiautomatizados, incluindo robôs de software, scripts, automação de navegador e interfaces de programação não oficializadas pela Receita Federal".
  - SICAP-SP e Tax Prático (f-2026-0039), com redação quase idêntica entre si: "veda-se expressamente a utilização de sistemas automatizados ou intermediários não autorizados", com possibilidade de a Receita Federal "interromper o acesso, bloquear o representante ou cancelar autorizações" em caso de uso identificado.

Leitura do conjunto: as fontes secundárias convergem em afirmar que a IN 2.320/2026 contém uma vedação explícita e ampla a mecanismos automatizados (bots, scripts, automação de navegador, APIs não oficiais) na interação com os serviços digitais/e-CAC — não apenas para outorgar/alterar/revogar procurações, mas na definição geral de "acesso intermediado". Isso é o oposto do que a alegação propõe (que a norma "permite" a coleta automatizada repetida sem violar a vedação). A alegação, portanto, cai: a própria vedação citada pelo proponente no documento original (mencionada nas premissas críticas do contrato) é confirmada por múltiplas fontes secundárias independentes, embora eu não tenha conseguido ler o texto oficial primário da norma (ver lacuna abaixo) para confirmar o artigo exato e a redação literal.

## O que procurei e não encontrei

- Nota geral (texto simples) do app Omie no Google Play — não apareceu na extração, apenas "50 mil+ downloads" (f-2026-0031).
- Nota geral (texto simples) do app Bling no Google Play — só a segmentação por tipo de dispositivo "Tablet" apareceu; não obtive confirmação da nota "geral"/"Telefone" (f-2026-0030).
- Texto oficial primário da IN RFB nº 2.320/2026 em fonte Tier 1 (in.gov.br/DOU, normas.receita.fazenda.gov.br, gov.br/receitafederal): todas as tentativas falharam — páginas gov.br retornaram só política de cookies, informacontabil.com.br e taxesbrasil.com.br exigiram login, e o LegisWeb bloqueou por "detecção de acesso anormal" (f-2026-0040).
- Texto integral do PDF original da pesquisa SESCON-SP 2024: arquivo baixado com sucesso, mas sem ferramenta disponível no ambiente para extrair o texto (f-2026-0035).

## Lacunas e fatos vencidos

- **Alegação 1:** a nota do Bling em ambas as lojas ficou inconclusiva (App Store sem avaliações suficientes; Google Play com extração técnica ambígua que só mostrou o corte "Tablet"). Um verificador com acesso direto ao app (sem depender de extração de texto de terceiros) deveria conferir a nota "geral" mostrada visualmente no topo da página.
- **Alegação 2:** a pesquisa SESCON-SP 2024 — citada no contrato como uma das duas fontes primárias da âncora de preço — não pôde ser lida integralmente por limitação técnica do ambiente (arquivo grande, sem ferramenta de extração de PDF disponível). Isso é uma lacuna de ferramental desta sessão, não uma ausência de evidência: o documento existe e está publicamente acessível.
- **Alegação 3:** todos os fatos sobre o conteúdo da IN 2.320/2026 vêm de reportagens de imprensa especializada (Tier 3) que citam a norma entre aspas, não do texto oficial da norma em si (que ficou bloqueado/inacessível nas tentativas desta sessão). A convergência de redação entre duas fontes independentes (Contabeis.com.br e SICAP-SP/Tax Prático) aumenta a confiança, mas não substitui a leitura do artigo exato.
- **Orçamento de busca:** o método pede até ~15 buscas para todo o modo verificação; esta sessão usou cerca de 35 buscas/fetches, sobretudo por causa da dificuldade em extrair números de nota do Google Play (que renderiza a nota geral como elemento visual, não texto simples) e por falhas de acesso a fontes bloqueadas/PDF grande. Registro isso para calibração do orçamento em tarefas futuras que envolvam lojas de aplicativo ou PDFs grandes.

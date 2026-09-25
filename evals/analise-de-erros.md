# Análise de erros

Leitura de execuções reais: para cada uma, o **primeiro erro** encontrado. É daqui que
nascem os próximos evals e as correções de método. Uma linha por execução; detalhe quando
o erro virar correção.

| Data | Execução | Primeiro erro | Correção | Vira eval? |
|---|---|---|---|---|
| 2026-09-24 | OP-0001 (NFS-e nacional), `/oportunidade` + `/kill`, headless, sem usuário | Alegação 2 do contrato escrita invertida: sua confirmação enfraquece a tese, mas a regra a contou como "se sustentou" | `/kill`, `metodo-julgamento` e schema do contrato: toda alegação é condição que a tese precisa que seja verdadeira, com checagem explícita antes de gravar. Veredito v-2026-0001 corrigido: 1 de 3 caiu, e a regra continua GO | Sim: caso de roteamento de alegações (dado um contrato, cada alegação confirmada fortalece a tese?) com juiz binário |
| 2026-09-24 | OP-0001, `/validar` completo, headless, com rede | Memorandos escritos antes da verificação usaram 4 fatos que o verificador depois achou contraditos pela fonte (preços de eNotas e Focus NFe, atribuição à Conta Azul, anúncio do GetNinjas) | Verificador passa para antes dos memorandos (`/validar`, `metodo-julgamento`, arquitetura); memorando não usa fato contradito e declara quando usa fato não verificado | Sim: invariante de ordem nas transcrições (E1) e taxa de fatos contraditos por tipo de leitura |
| 2026-09-25 | OP-0002 (Arkan), `/kill` 1ª tentativa, a partir do SDD do proponente | Contrato distorceu a tese: inverteu o preço ("mais caro que o contador" quando o SDD diz "mais barato"), testou uma alegação que o proponente nega (automação do e-CAC) e usou nota de app de concorrente como condição-barreira | `contrato --anular` auditável; subagente `revisor-de-enquadramento` antes de gravar; alegação do kill só de condição-barreira de dano fatal/alto, citando a seção do material. Veredito v-2026-0003 inválido; kill refeito (v-2026-0004 GO) | Sim: fidelidade de enquadramento (SDD sintético → as alegações reproduzem o material?) |
| 2026-09-25 | OP-0002, `/validar` completo, headless | O pesquisador gravou o dossiê como `dossie.md`, e o `pacote-juiz` só listava `dossie-*.md`: o juiz julgou sem o dossiê completo, só com o do kill barato. Na mesma rodada: `conferir-trecho` quebrou em páginas gzip (a conferência mecânica não rodou), um fato atribuiu ao produto da Conta Azul funções que a página descreve para a categoria (f-2026-0083, base da objeção mais forte) e os dois memorandos passaram de 1.500 palavras e foram truncados numa linha só | `pacote-juiz` e validação leem `dossie*.md`; curl `--compressed` e conferência por partes; verificador confere atribuição e literalidade e corrige o fato; truncamento preserva linhas e avisa. Memorandos e juiz refeitos pela regra de fato corrigido, com `--substitui` | Sim: E1 "o juiz recebeu todo dossiê da pasta" e E2 com páginas gzip, PDF e trecho com elisão |

## Observações da execução OP-0001

- **Bom:** a pergunta neutralizada tirou a convicção ("tenho quase certeza que dá
  dinheiro") e a tese ficou em terceira pessoa. As alegações foram falsificáveis e
  baratas. A taxa-base foi declarada com classe de referência, e o teto teve conta
  explícita. As suposições feitas sem o usuário foram registradas no histórico.
- **Limitação do ambiente:** os 9 fatos têm `leitura: resumo_de_busca`, porque a leitura
  de páginas falhou na nuvem (R-02). O validador avisou corretamente que o veredito se
  apoia em fatos sem leitura integral.
- **Custo:** US$0,48 até o limite de uso, mais US$1,22 na retomada.

## Observações da execução OP-0001 /validar

- **Funil funcionou:** o kill barato (grosso) deixou passar, e a validação completa
  recomendou KILL com p_sucesso 0,066 (bruta do juiz 0,055) contra taxa-base 0,10. Hipótese
  mais provável: "dor real mas não paga" (0,42). Objeção mais forte: contadores já fazem
  a adequação dentro do pacote ou como isca, e o Emissor Nacional é gratuito.
- **Resumo de busca não é evidência:** 4 de 9 fatos coletados só por resumo de busca no
  kill barato estavam errados quando a página foi lida (44%). Com rede, o kill barato deve
  ler as páginas das 3 alegações.
- **Juiz se comportou como desenhado:** descontou os fatos contraditos e deixou
  previsões de horizonte curto com critério de resolução (pré-venda até nov/2026).
- **Custo:** US$5,77 (12 turnos).

## Observações da execução OP-0002 (Arkan)

- **Dois vereditos, um substituído.** A rodada 1 (v-2026-0005, ITERAR, p 0,04) teve a
  entrada do juiz defeituosa em três pontos (dossiê fora do pacote, fato com
  atribuição errada, memorandos truncados). A rodada 2 (v-2026-0006, REFORMULAR, p
  0,037) usou o dossiê completo, 24 fatos relidos e memorandos dentro do teto. A regra
  de refazer foi gravada antes do novo resultado (`/validar`, "fato corrigido depois do
  veredito").
- **Citação literal que não é literal.** Dos 24 fatos `confirmada` que falharam na
  conferência mecânica, 12 tinham o trecho traduzido, parafraseado, sem acentos ou
  misturando duas páginas (f-2026-0064, f-2026-0071). O conteúdo se sustentou em
  todos; a citação não. A causa provável é o coletor transcrever o resumo da WebFetch
  em vez da página.
- **Mudança em definição de agente não vale na sessão corrente.** A regra de atribuição
  foi escrita no `verificador.md` antes de lançá-lo, e o verificador não a aplicou até
  receber a pergunta explícita. O mesmo vale para `maxTurns`: 40 não bastou para 24
  fatos, e o novo limite de 80 só entra na próxima sessão.
- **Conferência mecânica cobre pouco.** Mesmo depois das correções (gzip, elisão,
  acentos, PDF, JSON-LD), 9 de 24 passam. O resto falha por layout de tabela, marcação
  copiada no trecho e dados montados em elementos separados. `FALHOU` serve de triagem
  para leitura, não de veredito.
- **Custo:** kill barato (2 tentativas) ~US$6; `/validar` headless US$8,14;
  re-verificação e rodada 2 nesta sessão, sem busca.


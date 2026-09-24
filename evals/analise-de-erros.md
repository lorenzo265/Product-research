# Análise de erros

Leitura de execuções reais: para cada uma, o **primeiro erro** encontrado. É daqui que
nascem os próximos evals e as correções de método. Uma linha por execução; detalhe quando
o erro virar correção.

| Data | Execução | Primeiro erro | Correção | Vira eval? |
|---|---|---|---|---|
| 2026-09-24 | OP-0001 (NFS-e nacional), `/oportunidade` + `/kill`, headless, sem usuário | Alegação 2 do contrato escrita invertida: sua confirmação enfraquece a tese, mas a regra a contou como "se sustentou" | `/kill`, `metodo-julgamento` e schema do contrato: toda alegação é condição que a tese precisa que seja verdadeira, com checagem explícita antes de gravar. Veredito v-2026-0001 corrigido: 1 de 3 caiu, e a regra continua GO | Sim: caso de roteamento de alegações (dado um contrato, cada alegação confirmada fortalece a tese?) com juiz binário |
| 2026-09-24 | OP-0001, `/validar` completo, headless, com rede | Memorandos escritos antes da verificação usaram 4 fatos que o verificador depois achou contraditos pela fonte (preços de eNotas e Focus NFe, atribuição à Conta Azul, anúncio do GetNinjas) | Verificador passa para antes dos memorandos (`/validar`, `metodo-julgamento`, arquitetura); memorando não usa fato contradito e declara quando usa fato não verificado | Sim: invariante de ordem nas transcrições (E1) e taxa de fatos contraditos por tipo de leitura |

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

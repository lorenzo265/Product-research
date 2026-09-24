# Análise de erros

Leitura de execuções reais: para cada uma, o **primeiro erro** encontrado. É daqui que
nascem os próximos evals e as correções de método. Uma linha por execução; detalhe quando
o erro virar correção.

| Data | Execução | Primeiro erro | Correção | Vira eval? |
|---|---|---|---|---|
| 2026-09-24 | OP-0001 (NFS-e nacional), `/oportunidade` + `/kill`, headless, sem usuário | Alegação 2 do contrato escrita invertida: sua confirmação enfraquece a tese, mas a regra a contou como "se sustentou" | `/kill`, `metodo-julgamento` e schema do contrato: toda alegação é condição que a tese precisa que seja verdadeira, com checagem explícita antes de gravar. Veredito v-2026-0001 corrigido: 1 de 3 caiu, e a regra continua GO | Sim: caso de roteamento de alegações (dado um contrato, cada alegação confirmada fortalece a tese?) com juiz binário |

## Observações da execução OP-0001

- **Bom:** a pergunta neutralizada tirou a convicção ("tenho quase certeza que dá
  dinheiro") e a tese ficou em terceira pessoa. As alegações foram falsificáveis e
  baratas. A taxa-base foi declarada com classe de referência, e o teto teve conta
  explícita. As suposições feitas sem o usuário foram registradas no histórico.
- **Limitação do ambiente:** os 9 fatos têm `leitura: resumo_de_busca`, porque a leitura
  de páginas falhou na nuvem (R-02). O validador avisou corretamente que o veredito se
  apoia em fatos sem leitura integral.
- **Custo:** US$0,48 até o limite de uso, mais US$1,22 na retomada.

# Product Research: Harness de Oportunidades

Harness em Claude Code para encontrar oportunidades de negócio, validá-las com evidência e
com compradores reais, e ajudar a construir e lançar as que sobrevivem.

Três trilhas: **G** (grandes problemas, SaaS B2B vertical), **M** (micro-SaaS / nicho) e
**S** (serviço com IA). Mercado: Brasil + arbitragem.

## Como usar

Abra o Claude Code na raiz do repositório e fale normalmente, ou use os comandos:

| Comando | Para quê |
|---|---|
| `/radar [setor] [lente] [trilha]` | Varrer um setor ou tema atrás de dores com dinheiro mal servido |
| `/oportunidade <ideia>` | Abrir um cartão a partir de uma ideia sua ou de sinais do radar |
| `/kill OP-NNNN` | Kill barato: 3 alegações mais baratas de falsificar; 2 ou mais caem → reformular |
| `/validar OP-NNNN` | Dossiê → memorandos a favor e contra → verificação → juiz isolado → veredito |
| `/teste OP-NNNN` | Test Card com regra de decisão calculada antes, e material do teste |
| `/resultado t-AAAA-NNNN` | Registrar o resultado do teste e aplicar a regra |
| `/portfolio` | Painel de tudo, pendências e foco da semana |
| `/calibrar` | Resolver previsões e ver se as probabilidades do harness significam algo |

Por baixo, o estado é gravado pela CLI `python3 -m harness` (veja `--help`), que valida
tudo antes de gravar.

## Status

| Fase | Estado |
|---|---|
| 1 · Arquitetura | ✅ (v2 depois da pesquisa) |
| 2 · Pesquisa | ✅ 5 relatórios em `research/` |
| 3 · Fatia vertical | 🔶 comandos até `/teste`, CLI, hooks, evals E0/E1/E4; falta rodar com rede e coletores |
| 4 · Funil completo | ⏳ |
| 5 · Operação | ⏳ |

**Para revisar primeiro:** [`docs/revisao-pendente.md`](docs/revisao-pendente.md).

## Documentos

- [Arquitetura](docs/01-arquitetura.md): o que é o harness, funil, trilhas, papéis, estado, evals, roteiro
- [Decisões](docs/decisoes.md): decisões tomadas, provisórias e em aberto
- [Revisão pendente](docs/revisao-pendente.md): o que decidi sem você, com impacto e alternativa
- [Plano de pesquisa](docs/02-plano-de-pesquisa.md) e relatórios em `research/`
- [Evals](evals/README.md)

## Estrutura

```
CLAUDE.md                  mapa para a sessão principal
.claude/agents/            batedor, pesquisador, memorando, verificador, juiz
.claude/skills/            metodo-pesquisa, metodo-julgamento e 8 comandos
.claude/settings.json      hooks (proteção e validação do estado)
harness/                   CLI e núcleo em Python
schemas/                   JSON Schema dos registros
data/                      fatos, sinais, vereditos, testes (JSONL)
oportunidades/             uma pasta por oportunidade
radar/                     relatórios do /radar (fila de grupos, lacunas)
evals/                     casos congelados e runners
research/                  relatórios e notas da Fase 2
tests/                     pytest
```

## Desenvolvimento

```bash
pip install -r requirements.txt
ruff format harness tests evals && ruff check harness tests evals
python3 -m pytest
```

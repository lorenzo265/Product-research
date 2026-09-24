"""E1 · invariantes do protocolo que dá para checar sem rodar modelo.

Se alguém editar um agente e abrir um canal de vazamento (juiz com busca, memorando com
CLAUDE.md, subagente que fala com outros), estes testes quebram antes de qualquer eval pago.
"""

from pathlib import Path

import pytest
import yaml

RAIZ = Path(__file__).resolve().parents[2]
AGENTES = RAIZ / ".claude" / "agents"
SKILLS = RAIZ / ".claude" / "skills"
LIMITE_DESCRICAO_SKILL = 1024
FERRAMENTAS_DE_LEITURA = {"Read", "Grep", "Glob"}
FERRAMENTAS_EXTERNAS = {"WebSearch", "WebFetch", "Bash"}


def _frontmatter(caminho):
    _, bruto, corpo = caminho.read_text(encoding="utf-8").split("---\n", 2)
    return yaml.safe_load(bruto), corpo


def _ferramentas(frontmatter):
    return {nome.strip() for nome in str(frontmatter.get("tools", "")).split(",") if nome.strip()}


@pytest.mark.parametrize("nome", ["juiz", "memorando"])
def test_avaliadores_nao_carregam_claude_md(nome):
    frontmatter, _ = _frontmatter(AGENTES / f"{nome}.md")

    assert frontmatter.get("omitClaudeMd") is True


def test_juiz_so_le_arquivos():
    frontmatter, _ = _frontmatter(AGENTES / "juiz.md")

    assert _ferramentas(frontmatter) <= FERRAMENTAS_DE_LEITURA


def test_memorando_nao_busca_fora_do_dossie():
    frontmatter, _ = _frontmatter(AGENTES / "memorando.md")

    assert not _ferramentas(frontmatter) & FERRAMENTAS_EXTERNAS


@pytest.mark.parametrize("nome", ["juiz", "memorando"])
def test_avaliadores_tem_modelo_fixado(nome):
    frontmatter, _ = _frontmatter(AGENTES / f"{nome}.md")

    assert str(frontmatter.get("model", "")).startswith("claude-")


@pytest.mark.parametrize("caminho", sorted(AGENTES.glob("*.md")), ids=lambda p: p.stem)
def test_nenhum_agente_cria_agentes_ou_conversa_com_outros(caminho):
    frontmatter, _ = _frontmatter(caminho)

    assert not _ferramentas(frontmatter) & {"Agent", "SendMessage"}


@pytest.mark.parametrize("caminho", sorted(AGENTES.glob("*.md")), ids=lambda p: p.stem)
def test_nome_do_agente_bate_com_o_arquivo(caminho):
    frontmatter, _ = _frontmatter(caminho)

    assert frontmatter["name"] == caminho.stem


@pytest.mark.parametrize("caminho", sorted(SKILLS.glob("*/SKILL.md")), ids=lambda p: p.parent.name)
def test_skill_tem_nome_da_pasta_e_descricao_dentro_do_limite(caminho):
    frontmatter, _ = _frontmatter(caminho)

    assert frontmatter["name"] == caminho.parent.name
    assert 0 < len(frontmatter["description"]) <= LIMITE_DESCRICAO_SKILL


@pytest.mark.parametrize("caminho", sorted(SKILLS.glob("*/SKILL.md")), ids=lambda p: p.parent.name)
def test_skills_nao_usam_caixa_alta_como_enfase(caminho):
    _, corpo = _frontmatter(caminho)
    enfases = [p for p in ("SEMPRE", "NUNCA", "OBRIGATÓRIO", "CRÍTICO", "IMPORTANTE") if p in corpo]

    assert enfases == []


def test_referencias_citadas_pelo_juiz_existem():
    referencias = SKILLS / "metodo-julgamento" / "references"
    for nome in ("formato-veredito", "pacote-mercado", "pacote-micro-saas", "pacote-servico-ia"):
        assert (referencias / f"{nome}.md").exists()

"""Hierarquia de erros do harness."""


class HarnessError(Exception):
    """Base de todos os erros do harness."""


class TipoDesconhecido(HarnessError):
    """O tipo de registro pedido não existe."""


class RegistroInvalido(HarnessError):
    """O registro não passa no schema ou nas regras do tipo."""

    def __init__(self, tipo: str, erros: list[str]) -> None:
        """Guarda o tipo e a lista de erros legíveis."""
        self.tipo = tipo
        self.erros = erros
        super().__init__(f"{tipo} inválido: " + "; ".join(erros))


class IdDuplicado(HarnessError):
    """Já existe um registro com este id."""


class RegistroNaoEncontrado(HarnessError):
    """Nenhum registro com este id."""


class ArquivoCorrompido(HarnessError):
    """Um arquivo de estado não pode ser lido (JSON ou frontmatter quebrado)."""

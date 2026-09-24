"""O estado real versionado no repo precisa estar sempre válido."""

from datetime import date

from harness.estado import Repositorio
from harness.validacao import ERRO, validar


def test_estado_versionado_nao_tem_erros():
    erros = [str(p) for p in validar(Repositorio().snapshot(), date.today()) if p.nivel == ERRO]

    assert erros == []

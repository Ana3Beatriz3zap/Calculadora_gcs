# calc_percentual.py
# Módulo C - Percentual
# Autor: Amanda Jesus
# Branch: feature/percentual

from typing import Union
import math

Number = Union[int, float]


def _validate_inputs(valor: Number, porcentagem: Number) -> None:
    if not isinstance(valor, (int, float)) or not isinstance(porcentagem, (int, float)):
        raise TypeError("valor e porcentagem devem ser numeros (int ou float)")
    if not (math.isfinite(valor) and math.isfinite(porcentagem)):
        raise ValueError("valor e porcentagem devem ser numeros finitos")


def percentual(valor: Number, porcentagem: Number) -> float:
    """Retorna o valor correspondente a uma porcentagem de `valor`.

    Exemplo: `percentual(200, 10)` -> 20.0
    """
    _validate_inputs(valor, porcentagem)
    return float(valor) * float(porcentagem) / 100.0


def acrescimo(valor: Number, porcentagem: Number) -> float:
    """Retorna o valor com acréscimo percentual."""
    _validate_inputs(valor, porcentagem)
    return float(valor) + percentual(valor, porcentagem)


def desconto(valor: Number, porcentagem: Number) -> float:
    """Retorna o valor com desconto percentual."""
    _validate_inputs(valor, porcentagem)
    return float(valor) - percentual(valor, porcentagem)

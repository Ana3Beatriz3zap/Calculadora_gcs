# calc_basico.py 
# Módulo A — Básico
# Autor: Nahie Herradon Meres
# Branch: feature/modulo-basico

import math
from typing import Union

Number = Union[int, float]

def _validate_inputs(a: Number, b: Number) -> None:
    """Valida se as entradas são numéricas e finitas."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos os argumentos devem ser números (int ou float).")
    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("Os argumentos devem ser números finitos (não NaN ou Infinito).")

def somar(a: Number, b: Number) -> float:
    """Retorna a soma de a e b."""
    _validate_inputs(a, b)
    return float(a + b)

def subtrair(a: Number, b: Number) -> float:
    """Retorna a diferença de a e b."""
    _validate_inputs(a, b)
    return float(a - b)

def multiplicar(a: Number, b: Number) -> float:
    """Retorna o produto de a e b."""
    _validate_inputs(a, b)
    return float(a * b)

def dividir(a: Number, b: Number) -> float:
    """Retorna a divisão de a por b.
    Lança ValueError se b == 0.
    """
    _validate_inputs(a, b)
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return float(a / b)
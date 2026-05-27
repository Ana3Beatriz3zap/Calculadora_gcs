# calc_basico.py
# Módulo C - Cálculo de percentual
# Autor: Amanda Jesus
# Branch: feature/percentual

def percentual(valor, porcentagem):
    """Retorna o valor correspondente a uma porcentagem de `valor`."""
    return valor * porcentagem / 100


def acrescimo(valor, porcentagem):
    """Retorna o valor com acréscimo percentual."""
    return valor + percentual(valor, porcentagem)


def desconto(valor, porcentagem):
    """Retorna o valor com desconto percentual."""
    return valor - percentual(valor, porcentagem)

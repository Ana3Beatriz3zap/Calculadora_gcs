# Arquivo que carrega os módulos gradualmente

try:
    import calc_basico
except ImportError:
    print("Módulo calc_basico ainda não disponível")

try:
    import calc_potencia
except ImportError:
    print("Módulo calc_potencia ainda não disponível")

try:
    import calc_percentual
except ImportError:
    print("Módulo calc_percentual ainda não disponível")

try:
    import calc_estatistica
except ImportError:
    print("Módulo calc_estatistica ainda não disponível")

try:
    import calc_conversao
except ImportError:
    print("Módulo calc_conversao ainda não disponível")

#chamar para os testes assim: calc_basico.somar(10, 5)
# calc_estatistica.py 
# Módulo D — Operações Estatísticas 
# Autor: Isabela Fernandes Lopes
# Branch: feature/modulo-estatistica 

import statistics

def media(lista):
    return statistics.mean(lista)

def mediana(lista):
    return statistics.median(lista)

def moda(lista):
    return statistics.mode(lista)

# calc_conversao.py 
# Módulo E — Conversão 
# Autor: Maria Eduarda da Silva Gonçalves
# Branch: feature/calculadora-conversao

import math

def celsius_para_fahrenheit(celsius):
     
     if celsius is None:
        raise ValueError("Temperatura não pode ser nula")
     
     if not isinstance(celsius, (int, float)):
        raise TypeError(f"Esperado número, recebido {type(celsius).__name__}")
     
     if math.isnan(celsius):
        raise ValueError("Valor inválido: NaN")
     
     if math.isinf(celsius):
        raise ValueError("Valor inválido: infinito")
     
     if celsius < -273.15:
        raise ValueError(f"Temperatura {celsius}°C está abaixo do zero absoluto (-273.15°C)")
     
     return (celsius * 9 / 5) + 32


def km_para_milhas(km):
    
    if km is None:
        raise ValueError("Distância não pode ser nula")
    
    if not isinstance(km, (int, float)):
        raise TypeError(f"Esperado número, recebido {type(km).__name__}")
    
    if math.isnan(km):
        raise ValueError("Valor inválido: NaN")
    
    if math.isinf(km):
        raise ValueError("Valor inválido: infinito")
    
    if km < 0:
        raise ValueError(f"Distância não pode ser negativa: {km}km")
    
    return km * 0.621371


def kg_para_libras(kg):
    
    if kg is None:
        raise ValueError("Peso não pode ser nulo")
    
    if not isinstance(kg, (int, float)):
        raise TypeError(f"Esperado número, recebido {type(kg).__name__}")
    
    if math.isnan(kg):
        raise ValueError("Valor inválido: NaN")
    
    if math.isinf(kg):
        raise ValueError("Valor inválido: infinito")
    
    if kg < 0:
        raise ValueError(f"Peso não pode ser negativo: {kg}kg")
    
    return kg * 2.20462
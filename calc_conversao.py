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

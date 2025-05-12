# Cálculos relacionados a circunferencias

import math

pi = math.pi

def perimetro_circunferencia(r):
    resultado = 2 * pi * r
    return resultado

def area_circunferencia(radio):
    resultado = pi * radio ** 2
    return resultado

def volumen_esfera(r):
    resultado = 4/3 * pi * r ** 3
    return resultado
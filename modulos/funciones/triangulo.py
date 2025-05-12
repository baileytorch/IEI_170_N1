# Cálculos relacionados a triángulos
from funciones.cuadrilatero import area_cuadrilatero

def perimetro_triangulo(a,b,c):
    return a + b + c

def area_triangulo(a,b):
    return a * b / 2

def volumen_prisma(a,b,c):
    area = area_cuadrilatero(a,b)
    return area * c
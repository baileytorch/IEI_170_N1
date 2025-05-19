# Ejercicio 1.-
# Se desea calcular la distancia recorrida (m) por un móvil que
# tiene velocidad constante (m/s) durante un tiempo t (s),
# considerar que es un MRU (Movimiento Rectilíneo
# Uniforme). 
# Solicitar velocidad y tiempo al usuario.

# velocidad = float(input("Ingrese su velocidad: "))
# tiempo = float(input("Ingrese tiempo de recorrido: "))
# distancia = velocidad * tiempo
# print(f"La distancia recorrida por el móvil es: {distancia}")

# Ejercicio 2.-
# Dada la siguiente lista, calcule el promedio de cada estudiante y muestre sus notas y su promedio final.
estudiantes = [
    ['Aquiles Baeza', [5.5, 4.7, 7.0]],
    ['Armando Casas', [4.3, 5.2, 3.8]],
    ['Wendy Sulca', [5.5, 7.0, 6.2]],
    ['Soyla Dolores', [4.0, 4.7, 5.1]]
]

suma = 0
for estudiante in estudiantes:
    for notas in estudiante[1]:
        suma = notas + suma
    print(suma)
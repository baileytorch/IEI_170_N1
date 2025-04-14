diccionario = {
    'nombre':'erick',
    'apellido':'bailey',
    'edad':49
}

for clave in diccionario:
    print(f"La clave del elemento es: {clave}")

print()
for elemento in diccionario.items():
    print(f"El elemento es: {elemento}")

print()
for elemento in diccionario.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f"La clave del elemento es: {clave}")
    print(f"El valor del elemento es: {valor}")
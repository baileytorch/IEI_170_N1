diccionario = {
    'nombre' : 'Erick',
    'apellido' : 'Bailey',
    'edad' : 49,
    'Estudiante' : False
}

# Ontener las claves del diccionario
print(diccionario.keys())

# Obtener el valor del dato por su nombre
print(diccionario.get('edad'))

# Eliminar un dato por su nombre
diccionario.pop('Estudiante')
print(diccionario)

# Obtener cada uno de los elementos por separado
print(diccionario.items())
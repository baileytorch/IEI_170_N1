lista_1 = ["erick Bailey", 49, True]
lista_2 = list(["erick Bailey", 49, True])

print(lista_1)
print(type(lista_1))

print(lista_2)
print(type(lista_2))

# Agregar un nuevo elemento a la lista
lista_1.append("Desarrollador Fullstack")
print(lista_1)

# Agregar un nuevo elemento en una posición específica
lista_1.insert(1, 56)
print(lista_1)

# Elimina un elemento en una posición específica
print(lista_1.pop(1))
print(lista_1)

# Elimina todos los elementos de la lista, pero la lista sigue existiendo
lista_1.clear()
print(lista_1)

print(f"Contar Elementos: {len(lista_1)}")

lista_3 = [3,5,2,9,0,1]

# Ordena de MENOR a MAYOR
lista_3.sort()
print(lista_3)

# Ordena de MAYOR a MENOR
lista_3.reverse()
print(lista_3)
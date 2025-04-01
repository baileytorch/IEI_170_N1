# Colecciones de datos

# LISTAS, colecciones ordenadas por ÍNDICE de datos o elementos mutables
lista = ["Erick Bailey", 49, True]
print(lista)
print(type(lista))

print([45,46,47])
print(type([45,46,47]))

print(lista[1])
lista[1] = 35
print(lista)

# DICCIONARIOS, colecciones ordenadas por NOMBRE de pares datos o elementos mutables
diccionario = {'nombre':'Erick Bailey','edad':49,'es_profesor':True}
print(diccionario)
print(type(diccionario))
print(diccionario['edad'])
diccionario['edad'] = 45
print(diccionario)

# CONJUNTOS, colección desordenada de elementos
conjunto = {"Erick Bailey", 49, True}
print(conjunto)
print(type(conjunto))

conjunto.add(45)
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.pop()
print(conjunto)

# TUPLA, colección INMUTABLE de elementos
tupla = ("Erick Bailey", 49, True)
print(tupla)
print(type(tupla))

#tupla[2]=45
print(tupla[2])
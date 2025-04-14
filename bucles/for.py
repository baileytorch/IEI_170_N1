# El ciclo FOR se usa para recorrer elementos, pueden ser listas, diccionarios y tuplas

frutas = ["banana","papaya","manzana","naranja"]
for fruta in frutas:
    print(f"Frutas con A: {fruta}")

print()
numeros = [20,30,40,50]
for numero in numeros:
    resultado = numero * numero
    print(f"{numero} * {numero} = {resultado}")
    
print()
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

# Inicia el rango en 0 y cuenta hasta el valor indicado -1
print()
for numero in range(6):
    print(numero)

# Inicia el rango en primer valor y cuenta hasta el segundo valor -1
print()
for numero in range(5,51):
    print(numero)

# Inicia el rango en primer valor y cuenta hasta el segundo valor -1, 
# indicando el valor de avance
print()
for numero in range(5,51,5):
    print(numero)
    
for fruta in frutas:
    if fruta == 'naranja':
        print(f"{fruta} es la mejor fruta que hay")

for caracter in 'espectacular':
    print(caracter)
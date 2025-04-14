animales = {'michis','peritos','canarios','osos polares'}
numeros = {20,30,40,50}

for animal in animales:
    print(f"El animal es: {animal}")

print()
for numero in numeros:
    resultado = numero * numero
    print(f"{numero} * {numero} = {resultado}")

# Ordenando CONJUNTOS en python       
print()
print(type(sorted(numeros)))
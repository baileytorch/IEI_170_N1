# Datos de tipo STRING o cadenas de texto
nombre = 'Erick Bailey'
asignatura = "Introducción a la Programación"

variable1 = '''Introducción a la
Programación'''

print(variable1)
print(type(variable1))

# Datos de tipo numéricos enteros INT y decimales FLOAT
numero_1 = 49
print(numero_1)
print(type(numero_1))

numero_2 = 49.5
print(numero_2)
print(type(numero_2))

# Datos de valor lógico TRUE FALSE o dato BOOLEANO BOOL
nueva_variable = True
print(nueva_variable)
print(type(nueva_variable))

nombre = "Erick"
apellido = "Bailey"
edad = 49
print(nombre + " " + apellido)
print(nombre, apellido)

print("Saludos", nombre, apellido, " Su edad es" , edad)
print("Saludos " + nombre + " " + apellido + ". Su edad es " + str(edad) + ".")
print(f"Saludos {nombre} {apellido}. Su edad es {edad}.")

numero_1 = 35
numero_2 = '44 '
resultado = numero_1 + int(numero_2)
print(resultado)

print(numero_2 * numero_1)
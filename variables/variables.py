# Asignación
nombre_completo = 'Erick Bailey'
print("Hola " + nombre_completo + " SOS UN CRACK!!")

# Contactenación usando método FORMAT STRING
print(f"Hola {nombre_completo} SOS UN CRACK!!")

numero_1 = 6
numero_2 = 7
resultado = numero_1 + numero_2
print(resultado)

# Borrando variables con método DEL
print("Borrando la variable nombre_completo...")
del nombre_completo
# print(f"Hola {nombre_completo} SOS UN CRACK!!")

# Buscando información dentro de una variable
nombre_completo = 'Erick Bailey'
print("Buscando un texto dentro de una variable...")
print("Erick" in nombre_completo)
print("Mesa" not in nombre_completo)
print("ck" in nombre_completo)
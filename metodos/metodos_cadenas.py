nombre_completo = "erick bailey"
titulo_profesional = "Desarollador de Sistemas"
texto_mayusculas = "TEXTO EN MAYUSCULAS"
texto_multilinea = """
línea 1
línea 2
línea 3
"""

# print(dir(nombre_completo))
print(f"Texto capitalizado: {nombre_completo.capitalize()}")
print(f"Texto como título: {nombre_completo.title()}")
print(f"Texto en MAYÚSCULAS: {nombre_completo.upper()}")
print(f"Testo en MINÚSCULAS: {texto_mayusculas.lower()}")
print(f"Contar caracteres: {len(nombre_completo)}")
print(f"Contar caracteres: {len(texto_multilinea)}")
print(f"Reemplazando texto: {nombre_completo.replace("erick", "Torch")}")

texto_separado = nombre_completo.split(" ")
print(texto_separado)
print(type(texto_separado))
print(texto_separado[0])
print(nombre_completo.index("b"))
print(nombre_completo.count("i"))
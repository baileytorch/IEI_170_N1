def saludar(nombre, apellido, genero):
    if genero.lower() == "hombre":
        print(f"Buen día Don {nombre} {apellido}")
    elif genero.lower() == "mujer":
        print(f"Buen día Doña {nombre} {apellido}")
    else:
        print("Genero no ingresado")
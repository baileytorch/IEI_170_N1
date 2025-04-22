def saludar(nombre, apellido, genero):
    if genero.lower() == "hombre":
        print(f"Buen día Don {nombre} {apellido}")
    elif genero.lower() == "mujer":
        print(f"Buen día Doña {nombre} {apellido}")
    else:
        print("Genero no ingresado")
    
saludar("Erick Bailey")

nombre_ingresado = input("Ingrese su nombre: ")
apellido_ingresado = input("Ingrese su apellido: ")
genero_ingresado = input("Ingrese su genero (hombre/mujer): ")

saludar(nombre = nombre_ingresado, genero = genero_ingresado, apellido = apellido_ingresado)

numero1= int(input("Ingrese primer número."))
numero2 = int(input("Ingrese segundo número."))

def sumar(a,b):
    resultado = a + b
    print(f"{a}+{b} = {resultado}")

sumar(numero1,numero2)

num_1 = int(input("Ingrese primer número: "))
op = input("Ingrese su operación: ")
num_2 = int(input("Ingrese segundo número: "))

def calculadora(a,b,operacion):
    resultado = 0
    if operacion == "+":
        resultado = a + b
    elif operacion == "*":
        resultado = a * b
    elif operacion == "-":
        resultado = a - b
    elif operacion == "/":
        resultado = a / b
    else:
        print("Operación Incorrecta...")
    print(f"{a} {operacion} {b} = {resultado}")

calculadora(num_1,num_2,op)
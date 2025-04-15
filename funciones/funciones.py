def saludar(nombre):
    print(f"Buen día maravilloso {nombre}")
    
saludar("Erick Bailey")

nombre_ingresado = input("Ingrese su nombre:")
saludar(nombre_ingresado)

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
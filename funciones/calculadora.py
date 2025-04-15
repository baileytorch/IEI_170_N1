numeros = ["0","1","2","3","4","5","6","7","8","9","."]
operaciones = ["+","-","/","*"]
igual = "="

def calculadora_OP():
    resultado = 0  
    operacion = ""
    
    while True:
        entrada = input("")
        try:
            if entrada in numeros or entrada in operaciones:
                operacion = operacion + entrada
            elif entrada in igual:
                print(operacion)
            else:
                print("Ingrese un valor numérico o de operación...")
        except:
            print("Operación terminada...")
    print(resultado)

calculadora_OP()
# Crear un programa que convierta unidades de temperatura.
# 1.- El usuario deberá ingresar el valor de T°.
# 2.- El usuario deberá ingresar escala de T° original.
# 3.- El usuario deberá ingresar escala de T° final.
# 4.- El sistema deberá entregar resultados de conversión.

# de °C a °K => °C + 273.15
# de °C a °F => (°C * 9/5) + 32

# de °K a °C => °K - 273.15
# de °K a °F => ((°K - 273.15)* 9/5) + 32

# de °F a °C => (°F -32) * 5/9
# de °F a °K => (°F -32) * 5/9 + 273.15

def convertidor_temperatura(temperatura, escala_inicial, escala_final):
    respuesta = 0
    
    if escala_inicial == "C":
        if escala_final == "K":
            respuesta = temperatura + 273.15
        elif escala_final == "F":
            respuesta = (temperatura * 9/5) + 32
        else:
            print("Escala final inválida.")
    elif escala_inicial == "K":
        if escala_final == "C":
            respuesta = temperatura - 273.15
        elif escala_final == "F":
            respuesta = ((temperatura - 273.15)* 9/5) + 32
        else:
            print("Escala final inválida.")
    elif escala_inicial == "F":
        if escala_final == "K":
            respuesta = (temperatura -32) * 5/9 + 273.15
        elif escala_final == "C":
            respuesta = (temperatura -32) * 5/9
        else:
            print("Escala final inválida.")
    else:
        print("Escala inicial inválida.")
    
    print(f"La temperatura {temperatura}°{escala_inicial} convertida es: {respuesta}°{escala_final}")

temperatura = float(input("Ingrese la temperatura: "))
escala_1 = input("Ingrese la escala de T° inicial C, F o K: ").upper().strip()
escala_2 = input("Ingrese la escala de T° final C, F o K: ").upper().strip()
convertidor_temperatura(temperatura, escala_1, escala_2)
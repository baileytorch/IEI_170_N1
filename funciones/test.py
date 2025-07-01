# cadena = "Esto es un texto largo para probar el split"
# separador = ["t","l"]
# resultado = cadena.split("t" and "l")
# print(resultado)


try:
    numero1 = int(input('Ingrese el valor del numerador: '))
    numero2 = int(input('ingrese el valor del denominador: '))

    division = numero1 / numero2
    print(division)
except ValueError:
    print('El valor ingresado no se puede convertir a entero.')
except ZeroDivisionError:
    print('No se puede dividir por cero.')
except:
    print('No se puede ejecutar su operación.')
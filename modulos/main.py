import funciones.cuadrilatero
import funciones.circunferencia
import funciones.triangulo

def sub_menu():
    print()
    print("1: Opción perímetro")
    print("2: Opción área")
    print("3: Opción volumen")
    print("0: Salir")
    print()

def menu_principal():
    titulo = "¡bienvenido a los cálculos geométricos!"
    print()
    print(titulo.title())
    print("1: Opción cuadrilátero")
    print("2: Opción circunferencia")
    print("3: Opción triángulo")
    print("0: Salir")
    print()
    
    while True:
        opcion = input("Seleccione su opción (0-3)")
        
        if opcion == "1":
            sub_menu()
            
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass   
        elif opcion == "0":
            print("Saliendo...")     
            break
        else:
            print("Opción ingresada inválida, trate nuevamente...")
    
menu_principal()
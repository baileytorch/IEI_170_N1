from funciones.cuadrilatero import perimetro_cuadrilatero, area_cuadrilatero, volumen_cubo
from funciones.circunferencia import perimetro_circunferencia, area_circunferencia, volumen_esfera
from funciones.triangulo import perimetro_triangulo, area_triangulo, volumen_prisma

def sub_menu():
    print()
    print("1: Opción perímetro")
    print("2: Opción área")
    print("3: Opción volumen")
    print("0: Salir")
    print()

def menu_principal():    
    while True:
        titulo = "¡bienvenido a los cálculos geométricos!"
        print()
        print(titulo.title())
        print("1: Opción cuadrilátero")
        print("2: Opción circunferencia")
        print("3: Opción triángulo")
        print("0: Salir")
        print()
        opcion = input("Seleccione su opción (0-3): ")
        
        if opcion == "1":
            sub_menu()
    
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
                    
            if opcion_sub_menu == "1":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                respuesta = perimetro_cuadrilatero(lado_1, lado_2)
                print(respuesta)
                print()
                
            elif opcion_sub_menu == "2":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                respuesta = area_cuadrilatero(lado_1, lado_2)
            
            elif opcion_sub_menu == "3":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                altura = float(input("Ingrese la altura del cubo: "))
                respuesta = volumen_cubo(lado_1, lado_2, altura)
            
            elif opcion_sub_menu == "0":
                print("Saliendo...")
                return
            else:
                print("Opción ingresada inválida...")
                return
            
        elif opcion == "2":
            sub_menu()
            
        elif opcion == "3":
            sub_menu()
            
        elif opcion == "0":
            print("Saliendo...")     
            break
        else:
            print("Opción ingresada inválida, trate nuevamente...")
    
menu_principal()
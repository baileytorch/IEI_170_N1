from funciones.cuadrilatero import perimetro_cuadrilatero, area_cuadrilatero, volumen_cubo
from funciones.circunferencia import perimetro_circunferencia, area_circunferencia, volumen_esfera
from funciones.triangulo import perimetro_triangulo, area_triangulo, volumen_prisma

def sub_menu():
    print()
    print("1: Opción cuadrilátero")
    print("2: Opción circunferencia")
    print("3: Opción triángulo")
    print("0: Salir")
    print()

def menu_principal():
    titulo = "¡bienvenido a los cálculos geométricos!"
    print()
    print(titulo.title())
    while True:
        print()
        print("1: Opción perímetro")
        print("2: Opción área")
        print("3: Opción volumen")
        print("0: Salir")
        print()
        opcion = input("Seleccione su opción (0-3): ")
        
        respuesta = 0
        # Opcion 1 Perímetro
        if opcion == "1":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            # Submenu 1 Perímetro Cuadrilátero
            if opcion_sub_menu == "1":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                respuesta = perimetro_cuadrilatero(lado_1, lado_2)
            
            # Submenu 2 Perímetro Circunferencia
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese valor del radio: "))
                respuesta = perimetro_circunferencia(radio)
            
            # Submenu 3 Perímetro Triángulo
            elif opcion_sub_menu == "3":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                lado_3 = float(input("Ingrese valor del lado 3: "))
                respuesta = perimetro_triangulo(lado_1, lado_2, lado_3)
            
            elif opcion_sub_menu == "0":
                print("Saliendo...")
                return
            else:
                print("Opción ingresada inválida...")
                return
        
        # Opción 2 Área   
        elif opcion == "2":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")
            
            # Submenu 1 Área Cuadrilátero
            if opcion_sub_menu == "1":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                respuesta = area_cuadrilatero(lado_1, lado_2)        
            
            # Submenu 2 Área Circunferencia
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese valor del radio: "))
                respuesta = area_circunferencia(radio)
            
            # Submenu 3 Área Triángulo
            elif opcion_sub_menu == "3":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                respuesta = area_triangulo(lado_1,lado_2)
        
        # Opción 3 Volumen
        elif opcion == "3":
            sub_menu()
            opcion_sub_menu = input("Seleccione su opción (0-3): ")            
            
            # Submenu 1 Volumen Cubo
            if opcion_sub_menu == "1":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                altura = float(input("Ingrese la altura del cubo: "))
                respuesta = volumen_cubo(lado_1,lado_2,altura)
            
            # Submenu 2 Volumen Esfera          
            elif opcion_sub_menu == "2":
                radio = float(input("Ingrese valor del radio: "))
                respuesta = volumen_esfera(radio)
            
            # Submenu 3 Volumen Prisma          
            elif opcion_sub_menu == "3":
                lado_1 = float(input("Ingrese valor del lado 1: "))
                lado_2 = float(input("Ingrese valor del lado 2: "))
                altura = float(input("Ingrese la altura del prisma: "))
                respuesta = volumen_prisma(lado_1,lado_2,altura)
            else:
                print("Opción ingresada inválida...")
                return
            
        elif opcion == "0":
            print("Saliendo...")     
            break
        else:
            print("Opción ingresada inválida, trate nuevamente...")
        
        print()
        print(f"Su respuesta es: {respuesta}")
    
menu_principal()
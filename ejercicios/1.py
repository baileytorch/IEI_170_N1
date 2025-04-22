# En un curso debemos ingresar los datos de nombre completo y edad de los estudiantes
# para definir quien es el mayor de ellos. 
# Escribir un código que permita ingresar los datos y entregue finalmente 
# el nombre y la edad del mayor y del menor estudiante. 
# Si las edades se repiten para mayor o menor, muestre el primero de ellos.

def listado_estudiantes(cantidad_estudiantes):
    list_estudiantes = []
    estudiante_mayor = []
    estudiante_menor = []
    
    for estudiante in range(cantidad_estudiantes):
        nombre_str = input("Ingrese nombre del estudiante: ")
        edad_int = int(input("Ingrese la edad del estudiante:"))
        estudiante = [nombre_str,edad_int]
        
        if len(list_estudiantes) == 0:
            estudiante_mayor = estudiante
            estudiante_menor = estudiante
        else:
            if estudiante_mayor[1] < estudiante[1]:
                estudiante_mayor = estudiante
            elif estudiante_menor[1] > estudiante[1]:
                estudiante_menor = estudiante
                
        list_estudiantes.append(estudiante)

        print(list_estudiantes)

listado_estudiantes(3)
from data.asignaturas import asignaturas
from data.crear_data import crear_data

# CREATE
def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input("Ingrese su nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())
    
    crear_data('asignaturas.py','asignaturas',asignaturas)
    
    mensaje = print(f"Asignatura {nueva_asignatura} agregada con éxito!")
    listado_asignaturas()
    return mensaje

# READ todos
def listado_asignaturas():
    contador = 0
    print() 
    print("Lista de Asignaturas")
    print("====================")
    for asignatura in sorted(asignaturas):
        contador+=1
        print(f"{contador}.- {asignatura.title()}")    
    print("====================")

# READ 1 dato   
def buscar_asignatura():
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura
        else:
            return "Asignatura NO encontrada"
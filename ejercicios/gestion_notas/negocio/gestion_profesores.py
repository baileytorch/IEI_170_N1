from data.profesores import profesores
from data.crear_data import crear_data

# CREATE
def agregar_profesor():
    listado_profesores()
    nueva_asignatura = input("Ingrese nuevo profesor: ")
    profesores.append(nueva_asignatura.title())
    
    crear_data('profesores.py','profesores',profesores)
    
    mensaje = print(f"Docente {nueva_asignatura} agregado con éxito!")
    listado_profesores()
    return mensaje

# READ todos
def listado_profesores():
    contador = 0
    print() 
    print("Lista de Docentes")
    print("=================")
    for profesor in sorted(profesores):
        contador+=1
        print(f"{contador}.- {profesor.title()}")    
    print("=================")

# READ 1 dato   
def buscar_profesor():
    busqueda = input("Ingrese docente a buscar: ")
    for profesor in profesores:
        if busqueda.lower() in profesor.lower():
            return profesor
        else:
            return "Docente NO encontrado"
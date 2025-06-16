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

# READ 1 dato
def indice_profesor(busqueda):
    indice = 0
    for i in range(len(profesores)):
        if busqueda.lower() in profesores[i].lower():
            indice = i
    return indice

# UPDATE
def actualizar_profesor():    
    busqueda = input("Ingrese docente a buscar: ")
    numero_profesor = indice_profesor(busqueda)
    if numero_profesor == 0:
        print('Docente NO encontrado')
    else:
        if numero_profesor is not None:
            profesores[numero_profesor] = input('Ingrese nuevo nombre de docente')
    crear_data('profesores.py','profesores',profesores)

# DELETE
def eliminar_profesor():
    busqueda = input("Ingrese docente a buscar: ")
    numero_profesor = indice_profesor(busqueda)
    if numero_profesor == 0:
        print('Docente NO encontrado')
    else:
        if numero_profesor is not None:
            profesores.pop(numero_profesor)
    crear_data('profesores.py','profesores',profesores)
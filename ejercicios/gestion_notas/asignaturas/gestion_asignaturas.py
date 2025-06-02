from data.asignaturas import asignaturas
import os

# CREATE
def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input("Ingrese su nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())
    
    archivo = 'asignaturas.py'
    ruta_relativa = os.path.join('ejercicios/gestion_notas/data', archivo)
    ruta_absoluta = os.path.abspath(ruta_relativa)
    ruta_real = os.path.realpath(ruta_absoluta)
    archivo_final = open(ruta_real,'w+')
    archivo_final.write(f'asignaturas={asignaturas}')
    archivo_final.close()
    
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

agregar_asignatura()
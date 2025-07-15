from data.asignaturas import asignaturas
from data.crear_data import crear_data
from data.conexion import generar_conexion

# CREATE


def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input("Ingrese su nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())

    crear_data('asignaturas.py', 'asignaturas', asignaturas)

    mensaje = print(f"Asignatura {nueva_asignatura} agregada con éxito!")
    listado_asignaturas()
    return mensaje

# READ todos


def listado_asignaturas():
    consulta = '''
        SELECT id_asignatura,codigo_asig,nombre_asig
        FROM asignaturas
        WHERE habilitado = 1
    '''
    asignaturas_db = []
    asignaturas_db = generar_conexion(consulta)
    if asignaturas_db is not None:
        return asignaturas_db
    else:
        print('No se han encontrado asignaturas')


def mostrar_listado_asignatura(asignaturas):
    print()
    print("Lista de Asignaturas")
    print("====================")
    if asignaturas != None:
        for asignatura in asignaturas:
            print(asignatura)
    print("====================")

# READ 1 dato


def buscar_asignatura():
    busqueda = input("Ingrese asignatura a buscar: ")
    for asignatura in asignaturas:
        if busqueda.lower() in asignatura.lower():
            return asignatura
        else:
            return "Asignatura NO encontrada"

# READ 1 dato


def indice_asignatura(busqueda):
    indice = 0
    for i in range(len(asignaturas)):
        if busqueda.lower() in asignaturas[i].lower():
            indice = i
    return indice

# UPDATE


def actualizar_asignatura():
    busqueda = input("Ingrese asignatura a buscar: ")
    numero_asignatura = indice_asignatura(busqueda)
    if numero_asignatura == 0:
        print('Asignatura NO encontrada')
    else:
        if numero_asignatura is not None:
            asignaturas[numero_asignatura] = input(
                'Ingrese nuevo nombre de asignatura')
    crear_data('asignaturas.py', 'asignaturas', asignaturas)

# DELETE


def eliminar_asignatura():
    busqueda = input("Ingrese asignatura a buscar: ")
    numero_asignatura = indice_asignatura(busqueda)
    if numero_asignatura == 0:
        print('Asignatura NO encontrada')
    else:
        if numero_asignatura is not None:
            asignaturas.pop(numero_asignatura)
    crear_data('asignaturas.py', 'asignaturas', asignaturas)

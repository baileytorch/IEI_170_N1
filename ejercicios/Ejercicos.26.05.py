asignaturas = ["Biología","Química","Física"]
notas_bio = []
notas_qui = []
notas_fis = []

# CREATE
def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input("Ingrese su nueva asignatura: ")
    asignaturas.append(nueva_asignatura.title())
    mensaje = print(f"Asignatura {nueva_asignatura} agregada con éxito!")
    print(asignaturas)
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

def ingreso_notas(numero,asignatura):    
    nota = float(input(f"Ingrese nota {numero} {asignatura}: "))
    return nota

def proceso_ingreso_notas():
    for asignatura in asignaturas:
        contador = 0
        for nota in range(3):
            contador += 1
            if asignatura == "Biología":
                nota = ingreso_notas(contador,asignatura)
                notas_bio.append(nota)
            elif asignatura == "Química":
                nota = ingreso_notas(contador,asignatura)
                notas_qui.append(nota)
            elif asignatura == "Física":
                nota = ingreso_notas(contador,asignatura)
                notas_fis.append(nota)

asig = buscar_asignatura()
print(asig)

# print(notas_bio)
# print(notas_qui)
# print(notas_fis)
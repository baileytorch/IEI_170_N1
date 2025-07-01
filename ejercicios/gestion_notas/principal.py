from auxiliares.version import version_actual
from auxiliares.menu import items_menu
from negocio.gestion_asignaturas import listado_asignaturas

def menu_principal():
    print()
    print(f'SISTEMA DE GESTIÓN DE NOTAS v.{version_actual}')
    print('=====================================')
    print()
    
    for clave,valor in items_menu.items():
        print(f'[{clave}] {valor}')
    print()
    opcion_menu = input(f'Seleccione su opción [0-{len(items_menu)-1}]: ')

    if opcion_menu == '1':
        # Sub menú asignaturas
        listado_asignaturas()
    elif opcion_menu == '2':
        # Sub menú docentes
        pass
    elif opcion_menu == '3':
        # Sub menú notas
        pass
    elif opcion_menu == '4':
        # Sub menú estudiantes
        pass
    elif opcion_menu == '0':
        return
    else:
        print('Opción Inválida')
    

menu_principal()
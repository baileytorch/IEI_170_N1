from auxiliares.version import version_actual
from auxiliares.menu import items_menu

def menu_principal():
    print()
    print(f'SISTEMA DE GESTIÓN DE NOTAS v.{version_actual}')
    print('=====================================')
    print()
    
    for clave,valor in items_menu.items():
        print(f'[{clave}] {valor}')
    print()
    opcion_menu = input(f'Seleccione su opción [0-{len(items_menu)-1}]: ')
    

menu_principal()
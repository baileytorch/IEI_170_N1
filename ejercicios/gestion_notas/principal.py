from auxiliares.version import version_actual
from auxiliares.menu import items_menu

def menu_principal():
    print()
    print(f'SISTEMA DE GESTIÓN DE NOTAS v.{version_actual}')
    print('=====================================')
    print()
    
    for i in range(len(items_menu)):
        print(f'[{i}] {items_menu[i]}')
    print()

menu_principal()
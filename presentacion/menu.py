from auxiliares import nombre_aplicacion, version_aplicacion, menu_superior, submenu_categoria 
from presentacion.interaccion_pyme import lista_categorias

def menu_principal():
    while True:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        opcion = input('\nIngrese su opción [0-5]: ').strip()

        if opcion == "1":
            while True:
                for clave, valor in submenu_categoria.items():
                    print(f'[{clave}] - {valor}')

                opcion_sub_menu = input('\nIngrese su opción [0-1]: ').strip()
                if opcion_sub_menu == "1":
                    lista_categorias()
                elif opcion_sub_menu == "0":
                    break
                else:
                    print("Opcion invalida.")   
        elif opcion == "2":     
            pass
        elif opcion == "3":
            print("Programa Finalizado.")
            break
        else:
            print("Opcion invalida.")        

    
from auxiliares import nombre_aplicacion, version_aplicacion, menu_superior, submenu_categoria 
from negocio.negocio_categoria import lista_categorias
from presentacion.presentacion_categoria import solicitar_datos_categoria, solicitar_actualizar_categoria, solicitar_desactivar_categoria, solicitar_activar_categoria


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
                elif opcion_sub_menu == "2":
                    solicitar_datos_categoria()
                elif opcion_sub_menu == "3":
                    solicitar_actualizar_categoria()
                elif opcion_sub_menu == "4":
                    solicitar_desactivar_categoria()
                elif opcion_sub_menu == "5":
                    solicitar_activar_categoria()                                                                      
                elif opcion_sub_menu == "0":
                    break
                else:
                    print("Opcion invalida.")   
        elif opcion == "2":     
            pass
        elif opcion == "0":
            print("Programa Finalizado.")
            break
        else:
            print("Opcion invalida.")        

    
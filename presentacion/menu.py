from auxiliares import nombre_aplicacion, version_aplicacion, menu_superior, submenu_categoria, submenu_proveedor
from negocio.negocio_categoria import lista_categorias
from presentacion.presentacion_categoria import solicitar_datos_categoria, solicitar_actualizar_categoria, solicitar_desactivar_categoria, solicitar_activar_categoria
from presentacion.presentacion_proveedor import solicitar_datos_proveedor
from auxiliares.mensajes import MENSAJE_ID_ENTERO, OPCION_INVALIDA


def menu_principal():
    opcion = -1

    while opcion != 0:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-7]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            menu_categoria()
        elif opcion == 2:
            menu_proveedor()
        elif opcion == 0:
            print("Programa Finalizado.")
        else:
            print(OPCION_INVALIDA)


def menu_categoria():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_categoria.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-2]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            lista_categorias()
        elif opcion == 2:
            solicitar_datos_categoria()
        elif opcion == 3:
            solicitar_actualizar_categoria()
        elif opcion == 4:
            solicitar_desactivar_categoria()
        elif opcion == 5:
            solicitar_activar_categoria()                                          
        elif opcion != 0:
            print(OPCION_INVALIDA)

def menu_proveedor():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_proveedor.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-4]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            print("Aun no estoy creado :C")
        elif opcion == 2:
            solicitar_datos_proveedor()            
        elif opcion != 0:
            print(OPCION_INVALIDA)
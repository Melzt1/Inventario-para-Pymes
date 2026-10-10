from auxiliares import nombre_aplicacion, version_aplicacion, menu_superior, submenu_categoria, submenu_proveedor, submenu_almacen, submenu_producto
from negocio.negocio_categoria import lista_categorias
from negocio.negocio_proveedor import lista_proveedores
from negocio.negocio_almacen import lista_almacenes
from negocio.negocio_producto import lista_productos
from presentacion.presentacion_categoria import solicitar_datos_categoria, solicitar_actualizar_categoria, solicitar_desactivar_categoria, solicitar_activar_categoria, solicitar_consultar_categoria
from presentacion.presentacion_proveedor import solicitar_datos_proveedor, solicitar_actualizar_proveedor, solicitar_actualizar_direccion_proveedor, solicitar_inhabilitar_proveedor, solicitar_habilitar_proveedor, solicitar_consultar_proveedor
from presentacion.presentacion_almacen import solicitar_datos_almacen, solicitar_actualizar_almacen, solicitar_actualizar_direccion_almacen, solicitar_inhabilitar_almacen, solicitar_habilitar_almacen, solicitar_consultar_almacen
from presentacion.presentacion_producto import solicitar_datos_producto
from auxiliares.mensajes import MENSAJE_ID_ENTERO, OPCION_INVALIDA


def menu_principal():
    opcion = -1

    while opcion != 0:
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-5]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            menu_categoria()
        elif opcion == 2:
            menu_proveedor()
        elif opcion == 3:
            menu_producto()            
        elif opcion == 4:
            menu_almacen()            
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
            opcion = int(input('\nIngrese su opción [0-6]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            lista_categorias()
        elif opcion == 2:
            solicitar_datos_categoria()
        elif opcion == 3:
            solicitar_consultar_categoria()            
        elif opcion == 4:
            solicitar_actualizar_categoria()
        elif opcion == 5:
            solicitar_desactivar_categoria()
        elif opcion == 6:
            solicitar_activar_categoria()                                          
        elif opcion != 0:
            print(OPCION_INVALIDA)

def menu_proveedor():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_proveedor.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-7]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            lista_proveedores()
        elif opcion == 2:
            solicitar_datos_proveedor()
        elif opcion == 3:
            solicitar_consultar_proveedor()            
        elif opcion == 4:
            solicitar_actualizar_proveedor()
        elif opcion == 5:
            solicitar_actualizar_direccion_proveedor()   
        elif opcion == 6:
            solicitar_inhabilitar_proveedor()
        elif opcion == 7:
            solicitar_habilitar_proveedor()                                                                     
        elif opcion != 0:
            print(OPCION_INVALIDA)

def menu_almacen():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_almacen.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-7]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            lista_almacenes()
        elif opcion == 2:
            solicitar_datos_almacen()
        elif opcion == 3:
            solicitar_consultar_almacen()            
        elif opcion == 4:
            solicitar_actualizar_almacen()
        elif opcion == 5:
            solicitar_actualizar_direccion_almacen()   
        elif opcion == 6:
            solicitar_inhabilitar_almacen()
        elif opcion == 7:
            solicitar_habilitar_almacen()                                                                     
        elif opcion != 0:
            print(OPCION_INVALIDA) 

def menu_producto():
    opcion = -1

    while opcion != 0:
        for clave, valor in submenu_producto.items():
            print(f'[{clave}] - {valor}')

        try:
            opcion = int(input('\nIngrese su opción [0-8]: ').strip())
        except ValueError:
            print(MENSAJE_ID_ENTERO)
            continue

        if opcion == 1:
            lista_productos()
        elif opcion == 2:
            solicitar_datos_producto()                                                                 
        elif opcion != 0:
            print(OPCION_INVALIDA)     
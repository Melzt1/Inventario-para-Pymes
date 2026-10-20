from auxiliares import (
    nombre_aplicacion, 
    version_aplicacion, 
    menu_superior, 
    submenu_categoria, 
    submenu_proveedor, 
    submenu_almacen, 
    submenu_producto, 
    submenu_producto_proveedor, 
    submenu_inventario, 
    submenu_movimientos
)
from presentacion.presentacion_categoria import (
    solicitar_datos_categoria, 
    solicitar_actualizar_categoria, 
    solicitar_desactivar_categoria,  
    solicitar_consultar_categoria, 
    solicitar_activar_categoria, 
    mostrar_categorias
)
from presentacion.presentacion_proveedor import (
    solicitar_datos_proveedor, 
    solicitar_actualizar_proveedor, 
    solicitar_actualizar_direccion_proveedor, 
    solicitar_desactivar_proveedor, 
    solicitar_consultar_proveedor, 
    solicitar_activar_proveedor, 
    mostrar_proveedores
)
from presentacion.presentacion_almacen import (
    solicitar_datos_almacen, 
    solicitar_actualizar_almacen, 
    solicitar_actualizar_direccion_almacen, 
    solicitar_desactivar_almacen, 
    solicitar_consultar_almacen, 
    solicitar_activar_almacen, 
    mostrar_almacenes
)
from presentacion.presentacion_producto import (
    solicitar_datos_producto, 
    solicitar_actualizar_producto, 
    solicitar_desactivar_producto, 
    solicitar_consultar_producto, 
    solicitar_activar_producto, 
    mostrar_productos
)
from presentacion.presentacion_producto_proveedor import (
    solicitar_asignar_proveedor_principal, 
    solicitar_asignar_proveedor_secundario, 
    solicitar_quitar_proveedor, 
    mostrar_proveedores_producto
)
from presentacion.presentacion_inventario import (
    solicitar_asociar_producto_almacen, 
    consultar_inventario_producto,
    mostrar_inventario_de_almacen, 
    mostrar_productos_stock_critico
)
from presentacion.presentacion_movimiento import (
    solicitar_registrar_entrada, 
    mostrar_historial_movimientos, 
    solicitar_registrar_salida, 
    solicitar_consultar_movimiento, 
    mostrar_movimientos_rango_fecha
)
from auxiliares.mensajes import OPCION_INVALIDA

def menu_principal():
    opcion = ""

    while opcion != "0":
        print(f"{nombre_aplicacion} - {version_aplicacion}")
        for clave, valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(menu_superior)-1}]: ').strip()

        if opcion == "1":
            menu_categoria()
        elif opcion == "2":
            menu_proveedor()
        elif opcion == "3":
            menu_producto()            
        elif opcion == "4":
            menu_almacen()
        elif opcion == "5":
            menu_inventario()                          
        elif opcion == "0":
            print("Programa Finalizado.")
        else:
            print(OPCION_INVALIDA)


def menu_categoria():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de categorías ===")

        for clave, valor in submenu_categoria.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_categoria)-1}]: ').strip()

        if opcion == "1":
            mostrar_categorias()
        elif opcion == "2":
            solicitar_datos_categoria()
        elif opcion == "3":
            solicitar_consultar_categoria()            
        elif opcion == "4":
            solicitar_actualizar_categoria()
        elif opcion == "5":
            solicitar_desactivar_categoria() 
        elif opcion == "6":
            solicitar_activar_categoria()                                                    
        elif opcion != "0":
            print(OPCION_INVALIDA)

def menu_proveedor():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de proveedores ===")

        for clave, valor in submenu_proveedor.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_proveedor)-1}]: ').strip()

        if opcion == "1":
            mostrar_proveedores()
        elif opcion == "2":
            solicitar_datos_proveedor()
        elif opcion == "3":
            solicitar_consultar_proveedor()            
        elif opcion == "4":
            solicitar_actualizar_proveedor()
        elif opcion == "5":
            solicitar_actualizar_direccion_proveedor()   
        elif opcion == "6":
            solicitar_desactivar_proveedor()   
        elif opcion == "7":
            solicitar_activar_proveedor()                                                                               
        elif opcion != "0":
            print(OPCION_INVALIDA)

def menu_almacen():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de almacenes ===")

        for clave, valor in submenu_almacen.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_almacen)-1}]: ').strip()

        if opcion == "1":
            mostrar_almacenes()
        elif opcion == "2":
            solicitar_datos_almacen()
        elif opcion == "3":
            solicitar_consultar_almacen()            
        elif opcion == "4":
            solicitar_actualizar_almacen()
        elif opcion == "5":
            solicitar_actualizar_direccion_almacen()   
        elif opcion == "6":
            solicitar_desactivar_almacen()  
        elif opcion == "7":
            solicitar_activar_almacen()                                                                              
        elif opcion != "0":
            print(OPCION_INVALIDA) 

def menu_producto():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de Productos ===")

        for clave, valor in submenu_producto.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_producto)-1}]: ').strip()

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            solicitar_datos_producto()
        elif opcion == "3":
            solicitar_consultar_producto()
        elif opcion == "4":
            solicitar_actualizar_producto()
        elif opcion == "5":
            solicitar_desactivar_producto()
        elif opcion == "6":
            solicitar_activar_producto()
        elif opcion == "7":
            menu_producto_proveedor()
        elif opcion == "0":
            return
        else:
            print(OPCION_INVALIDA)   

def menu_producto_proveedor():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de Proveedores del Producto ===")

        for clave, valor in submenu_producto_proveedor.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_producto_proveedor)-1}]: ').strip()

        if opcion == "1":
            solicitar_asignar_proveedor_principal()
        elif opcion == "2":
            solicitar_asignar_proveedor_secundario()
        elif opcion == "3":
            solicitar_quitar_proveedor()
        elif opcion == "4":
            mostrar_proveedores_producto()
        elif opcion == "0":
            return
        else:
            print(OPCION_INVALIDA)       

def menu_inventario():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de Inventario ===")

        for clave, valor in submenu_inventario.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_inventario)-1}]: ').strip()

        if opcion == "1":
            solicitar_asociar_producto_almacen()
        elif opcion == "2":
            consultar_inventario_producto()  
        elif opcion == "3":
            mostrar_inventario_de_almacen() 
        elif opcion == "4":
            mostrar_productos_stock_critico()  
        elif opcion == "5":
            menu_movimientos()                                               
        elif opcion == "0":
            return
        else:
            print(OPCION_INVALIDA)

def menu_movimientos():
    opcion = ""

    while opcion != "0":
        print("\n === Gestión de Movimientos ===")

        for clave, valor in submenu_movimientos.items():
            print(f'[{clave}] - {valor}')

        opcion = input(f'\nIngrese su opción [0-{len(submenu_movimientos)-1}]: ').strip()

        if opcion == "1":
            solicitar_registrar_entrada()
        elif opcion == "2":
            solicitar_registrar_salida()
        elif opcion == "3":
            solicitar_consultar_movimiento()
        elif opcion == "4":
            mostrar_movimientos_rango_fecha()
        elif opcion == "5":
            mostrar_historial_movimientos()            
        elif opcion == "0":
            return
        else:
            print(OPCION_INVALIDA)
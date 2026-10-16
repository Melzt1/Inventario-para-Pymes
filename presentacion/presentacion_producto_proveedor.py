from negocio.negocio_producto_proveedor import asignar_proveedor_principal, lista_proveedores_de_producto,asignar_proveedor_secundario, eliminar_relacion, proveedor_principal_de_producto, obtener_relacion
from negocio.negocio_producto import obtener_producto
from negocio.negocio_proveedor import obtener_proveedor

from auxiliares.entradas import forzar_entero
from auxiliares.mensajes import SOLICITUD_ID_PRODUCTO, SOLICITUD_ID_PROVEEDOR, MENSAJE_ID_NO_EXISTE
from prettytable import PrettyTable


def solicitar_asignar_proveedor_principal():
    print("\n=== Asignar proveedor principal ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    if obtener_producto(id_producto) is None:
        print("No existe un producto con ese ID.")
        return

    proveedor = obtener_proveedor(id_proveedor)
    if proveedor is None:
        print("No existe un proveedor con ese ID.")
        return

    principal = proveedor_principal_de_producto(id_producto)

    if principal is not None:
        print(f"El producto ya tiene como proveedor principal a {principal.id_proveedor.nombre}")

    resultado = asignar_proveedor_principal(id_producto, id_proveedor)

    print(f"Proveedor {proveedor.nombre} asignado como principal con exito.") if resultado else print("No se pudo asginar el proveedor.")
    

def solicitar_asignar_proveedor_secundario():
    print("\n=== Asignar proveedor secundario ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    producto = obtener_producto(id_producto)
    if producto is None:
        print("No existe un producto con ese ID.")
        return

    proveedor = obtener_proveedor(id_proveedor)
    if proveedor is None:
        print("No existe un proveedor con ese ID.")
        return

    if obtener_relacion(id_producto, id_proveedor) is not None:
        print(f"El proveedor {proveedor.nombre} ya está asociado a este producto.")
        return

    resultado = asignar_proveedor_secundario(id_producto, id_proveedor)

    print(f"Proveedor {proveedor.nombre} asginado con exito.") if resultado else print("No se pudo asignar el proveedor.")
        

def solicitar_quitar_proveedor():
    print("\n=== Quitar proveedor al producto ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR) 

    if obtener_producto(id_producto) is None:
        print("No existe un producto con ese ID.")
        return

    if obtener_proveedor(id_proveedor) is None:
        print("No existe un proveedor con ese ID.")
        return    

    resultado = eliminar_relacion(id_producto, id_proveedor)
    print(f"El proveedor con ID {id_proveedor} se quitó del producto con ID {id_producto}.") if resultado else print("No se pudo quitar el proveedor.")                 

def mostrar_proveedores_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)

    producto = obtener_producto(id_producto)

    if producto is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    relaciones = lista_proveedores_de_producto(id_producto)

    if not relaciones:
        print("El producto no tine asociado un proveedor.")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID Proveedor', 'Nombre', 'Principal/Secundario']

    for relacion in relaciones:
        proveedor = relacion.id_proveedor
        tabla.add_row([
            proveedor.id_proveedor,
            proveedor.nombre,
            ('Secundario', 'Principal')[relacion.es_principal],
        ])
    print(f"\n=== Proveedores de '{producto.nombre}' ===")
    print(tabla)       
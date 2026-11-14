from prettytable import PrettyTable

from auxiliares.entradas import forzar_entero_positivo, solicitar_confirmacion
from presentacion.presentacion_producto import solicitar_seleccion_producto
from negocio.negocio_producto_proveedor import (
    asignar_proveedor_principal, 
    listar_relaciones_de_producto,
    asignar_proveedor_secundario, 
    quitar_proveedor_de_producto, 
    obtener_proveedor_principal, 
    listar_proveedores_disponibles,
    listar_proveedores_para_principal
)

# Metodo auxiliar
def seleccionar_proveedor(proveedores):
    if not proveedores:
        print("No hay proveedores disponibles.")
        return None

    for i, proveedor in enumerate(proveedores, start=1):
        print(f"[{i}] - {proveedor.nombre} - {proveedor.rut or 'Sin RUT'}")

    opcion_valida = False

    while not opcion_valida:
        seleccion = forzar_entero_positivo("Seleccione: ")

        if 1 <= seleccion <= len(proveedores):
            return proveedores[seleccion - 1]

        print(f"Opción fuera de rango (1-{len(proveedores)}).")

def solicitar_asignar_proveedor_principal():
    print("\n=== Asignar proveedor principal ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    principal = obtener_proveedor_principal(producto.id_producto)

    if principal is not None:
        print(f"El producto ya tiene como proveedor principal a: {principal.id_proveedor.nombre}")

        confirmar = solicitar_confirmacion("Desea reemplazarlo por otro proveedor?")
        if not confirmar:
            print("Operacion cancelada.")
            return

    print(f"\nProveedores disponibles para '{producto.nombre}':")
    disponibles = listar_proveedores_para_principal(producto.id_producto)
    proveedor = seleccionar_proveedor(disponibles)

    if proveedor is None:
        return

    resultado = asignar_proveedor_principal(producto, proveedor)
    print(f"Proveedor {proveedor.nombre} asignado como principal con exito.") if resultado else print("No se pudo asginar el proveedor.")
    
def solicitar_asignar_proveedor_secundario():
    print("\n=== Asignar proveedor secundario ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    print(f"\nProveedores disponibles para '{producto.nombre}':")
    disponibles = listar_proveedores_disponibles(producto.id_producto)
    proveedor = seleccionar_proveedor(disponibles)

    if proveedor is None:
        return

    resultado = asignar_proveedor_secundario(producto, proveedor)
    print(f"Proveedor {proveedor.nombre} asginado como secundario.") if resultado else print("No se pudo asignar el proveedor.")
        
def solicitar_quitar_proveedor():
    print("\n=== Quitar proveedor al producto ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    
    relaciones = listar_relaciones_de_producto(producto.id_producto)
    # Comprension de listas: convierto la lista de relaciones (ProductoProvedor) en una lista de Proveedores
    # para poder reutilizar el metodo auxiliar y no crear otro metodo de seleccion
    proveedores = [relacion.id_proveedor for relacion in relaciones]
    proveedor = seleccionar_proveedor(proveedores)

    if proveedor is None:
        return

    confirmar = solicitar_confirmacion(f"Quitar el proveedor '{proveedor.nombre}' del producto '{producto.nombre}'?")
    if not confirmar:
        print("Operacion cancelada.")
        return
    
    resultado = quitar_proveedor_de_producto(producto, proveedor)
    print(f"El proveedor {proveedor.nombre} se quitó del producto {producto.nombre}.") if resultado else print("No se pudo disolver la relacion producto-proveedor.")                 

def mostrar_proveedores_producto():
    print("\n=== Ver proveedores de un producto ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    relaciones = listar_relaciones_de_producto(producto.id_producto)

    if not relaciones:
        print(f"El producto '{producto.nombre}' no tiene proveedores asociados.")
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
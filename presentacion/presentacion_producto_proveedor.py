from negocio.negocio_producto_proveedor import asignar_proveedor_principal, lista_proveedores_de_producto,asignar_proveedor_secundario, eliminar_relacion, proveedor_principal_de_producto, obtener_relacion, lista_proveedores_disponibles
from prettytable import PrettyTable
from presentacion.presentacion_producto import solicitar_seleccion_producto
from auxiliares.entradas import forzar_entero   

def solicitar_asignar_proveedor_principal():
    print("\n=== Asignar proveedor principal ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    principal = proveedor_principal_de_producto(producto.id_producto)

    if principal is not None:
        print(f"El producto ya tiene como proveedor principal a {principal.id_proveedor.nombre}")
        return

    disponibles = list(lista_proveedores_disponibles(producto.id_producto))

    if not disponibles:
        print("Todos los proveedores activos ya estan asociados a este producto.")
        return

    print(f"\nProveedores disponibles para '{producto.nombre}':")
    for i, proveedor in enumerate(disponibles, start=1):
        print(f"[{i}] - {proveedor.nombre} ({proveedor.rut})")        

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(disponibles):
            proveedor = disponibles[seleccion - 1]
            opcion_valida = True 
        else:
            print(f"Opcion fuera de rango (1-{len(disponibles)}).")    

    resultado = asignar_proveedor_principal(producto.id_producto, proveedor.id_proveedor)

    print(f"Proveedor {proveedor.nombre} asignado como principal con exito.") if resultado else print("No se pudo asginar el proveedor.")
    
def solicitar_asignar_proveedor_secundario():
    print("\n=== Asignar proveedor secundario ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    disponibles = list(lista_proveedores_disponibles(producto.id_producto))

    if not disponibles:
        print("Todos los proveedores activos ya estan asociados a este producto.")
        return

    print(f"\nProveedores disponibles para '{producto.nombre}':")
    for i, proveedor in enumerate(disponibles, start=1):
        print(f"[{i}] - {proveedor.nombre} ({proveedor.rut})")        

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(disponibles):
            proveedor = disponibles[seleccion - 1]
            opcion_valida = True 
        else:
            print(f"Opcion fuera de rango (1-{len(disponibles)}).")

    resultado = asignar_proveedor_secundario(producto.id_producto, proveedor.id_proveedor)
    print(f"Proveedor {proveedor.nombre} asginado como secundario.") if resultado else print("No se pudo asignar el proveedor.")
        

def solicitar_quitar_proveedor():
    print("\n=== Quitar proveedor al producto ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    relaciones = list(lista_proveedores_de_producto(producto.id_producto))
    if not relaciones:
        print(f"El producto '{producto.nombre}' no tiene proveedores asociados.")
        return    

    print(f"\nProveedores asociados a '{producto.nombre}':")
    for i, relacion in enumerate(relaciones, start=1):
        es_principal = "Principal" if relacion.es_principal else "Secundario"
        print(f"[{i}] {relacion.id_proveedor.nombre} ({relacion.id_proveedor.rut})  [{es_principal}]")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(relaciones):
            relacion = relaciones[seleccion - 1] # es objeto ProductoProveedor
            opcion_valida = True 
        else:
            print(f"Opcion fuera de rango (1-{len(relaciones)}).")

    proveedor = relacion.id_proveedor

    confirmar = input(f"Quitar el proveedor '{proveedor.nombre}' del producto '{producto.nombre}'? (S/N): ").strip().upper()
    if confirmar != "S":
        print("Operacion cancelada.")
        return    
    
    resultado = eliminar_relacion(producto.id_producto, proveedor.id_proveedor)
    print(f"El proveedor {proveedor.nombre} se quitó del producto {producto.nombre}.") if resultado else print("No se pudo disolver la relacion producto-proveedor.")                 

def mostrar_proveedores_producto():
    print("\n=== Ver proveedores de un producto ===")

    producto = solicitar_seleccion_producto()
    if producto is None:
        return

    relaciones = list(lista_proveedores_de_producto(producto.id_producto))

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
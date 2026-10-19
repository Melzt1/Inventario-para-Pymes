from prettytable import PrettyTable

from auxiliares.entradas import campo_obligatorio, forzar_positivo, forzar_entero, forzar_fecha
from auxiliares.mensajes import NO_HAY_MOVIMIENTOS
from negocio.negocio_producto import obtener_producto_sku
from negocio.negocio_inventario import listar_inventario_por_producto
from negocio.negocio_movimiento import (
    registrar_entrada, registrar_salida, 
    listar_historial_movimientos, 
    listar_movimientos_de_entrada, 
    listar_movimientos_de_salida, 
    listar_movimientos_por_rango_fecha
)

"""
Para registrar un movimiento, pedire el SKU del producto y el almacen donde se realizara. 
Con esos datos obtendre los objetos Producto y Almacen, y buscare el Inventario (id_inventario) que los relaciona,
si existe, usare el id_inventario (FK) para guardar el movimiento,
asi el usuario no necesita conocer ni digitar el id_inventario, lo cual es cero intuitivo usando la terminal.

PD: TODAVIA LA EXTRANO :c
"""

def solicitar_registrar_entrada():
    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()

    # aca obtengo el objeto Producto por su sku
    producto = obtener_producto_sku(sku)
    if producto is None:
        print("No existe producto con ese SKU.")
        return False

    # obtengo el id_producto del objeto Producto conseguido anteriormente
    id_producto = producto.id_producto 

    # este metodo devuelve todos los inventarios con dicho producto
    # teniendo acceso al objeto Inventareio, tengo acceso al id_almacen (objeto Almacen)
    lista_inventario = listar_inventario_por_producto(id_producto)

    if not lista_inventario:
        print("El producto no esta asociado a ningun almacen.")
        return False
    
    print(f"Producto encontrado: {producto.nombre}")
    print("Almacenes con inventario para este producto:")

    # dado que mi lista contiene la cantidad de objetos (0,1,2,3,4......) usare enumerate
    # OJO: tiene almacenando el objeto, NO el id_inventario
    for i, inventario in enumerate(lista_inventario, start=1):
        almacen = inventario.id_almacen
        print(f"[{i}] - {almacen.nombre} - Stock: {inventario.stock_actual}")

    seleccion = forzar_entero("\nSeleccione el Almacen: ")

    if 1 <= seleccion <= len(lista_inventario):
        inventario = lista_inventario[seleccion-1]
        id_inventario = inventario.id_inventario
    else:
        print(f"Opcion fuera de rango (1-{len(lista_inventario)}).")
        return False
    
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")
    fecha = forzar_fecha("Ingrese la fecha (DD-MM-YYYY): ", obligatorio=True)

    resultado = registrar_entrada(descripcion, cantidad, fecha, id_inventario)
    print("Entrada registrada con exito.") if resultado else print("No se pudo realizar el movimiento")
        
def solicitar_registrar_salida():
    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()

    producto = obtener_producto_sku(sku)
    if producto is None:
        print("No existe producto con ese SKU.")
        return False

    id_producto = producto.id_producto 
    inventarios = listar_inventario_por_producto(id_producto)

    if not inventarios:
        print("El producto no esta asociado a ningun almacen.")
        return False
    
    print(f"Producto encontrado: {producto.nombre}")
    print("Almacenes con inventario para este producto:")

    for i, inventario in enumerate(inventarios, start=1):
        almacen = inventario.id_almacen
        print(f"[{i}] - {almacen.nombre} - Stock: {inventario.stock_actual}")

    seleccion = forzar_entero("\nSeleccione el Almacen: ")

    if 1 <= seleccion <= len(inventarios):
        id_inventario = inventarios[seleccion-1]
    else:
        print(f"Opcion fuera de rango (1-{len(inventarios)}).")
        return False

    if inventario.stock_actual == 0:
        print("No hay stock suficiente")
        return False
        
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")

    if cantidad > inventario.stock_actual:
        print("El stock es insuficiente para esa salida.")
        return False

    fecha = forzar_fecha("Ingrese la fecha (DD-MM-YYYY): ", obligatorio=True)
    
    resultado = registrar_salida(descripcion, cantidad, fecha, id_inventario)
    print("Salida registrada con exito.") if resultado else print("No se pudo realizar el movimiento")

def solicitar_consultar_movimiento():
    print("=== Consulta de Movimientos ===")
    opcion = campo_obligatorio("Ingrese el tipo de movimiento (ENTRADA/SALIDA): ").strip().upper()

    if opcion == "ENTRADA":
        movimientos = listar_movimientos_de_entrada()
    elif opcion == "SALIDA":
        movimientos = listar_movimientos_de_salida()
    else:
        print("Opción invaida. Por favor, escribe ENTRADA o SALIDA.\n")
        return

    if not movimientos:
        print(NO_HAY_MOVIMIENTOS)
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,   
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        

def mostrar_movimientos_rango_fecha():
    fecha_inicio = forzar_fecha("Ingrese la fecha de inicio (DD-MM-YYYY): ", obligatorio=True)
    fecha_termino = forzar_fecha("Ingrese la fecha de termino (DD-MM-YYYY): ", obligatorio=True)       

    if fecha_inicio > fecha_termino:
        print("La fecha de inicio no puede ser posterior a la fecha de termino.")
        return False
    
    movimientos = listar_movimientos_por_rango_fecha(fecha_inicio, fecha_termino)
    if not movimientos:
        print(NO_HAY_MOVIMIENTOS)
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        

def mostrar_historial_movimientos():
    movimientos = listar_historial_movimientos()

    if not movimientos:
        print(NO_HAY_MOVIMIENTOS)
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        
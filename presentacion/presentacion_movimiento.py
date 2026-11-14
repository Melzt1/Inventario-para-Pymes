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

def solicitar_registrar_movimiento(sesion, tipo):
    print(f"\n=== Registrar {tipo} ===")

    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe producto con ese SKU.")
        return False

    lista_inventario = listar_inventario_por_producto(producto.id_producto)

    if not lista_inventario:
        print("El producto no esta asociado a ningun almacen.")
        return False
    
    print(f"Producto encontrado: {producto.nombre}")
    print("Ubicaciones disponibles:")

    for i, inventario in enumerate(lista_inventario, start=1):
        seccion = inventario.id_seccion
        print(f"[{i}] - {seccion.id_almacen.nombre} / {seccion.nombre} - Stock: {inventario.stock_actual}")

    seleccion = forzar_entero("\nSeleccione el Almacen: ")

    if not 1 <= seleccion <= len(lista_inventario):
        print(f"Opción fuera de rango (1-{len(lista_inventario)}).")
        return False
    
    inventario = lista_inventario[seleccion - 1]

    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")    

    if tipo == "SALIDA" and cantidad > inventario.stock_actual:
        print("El stock es insuficiente para esa salida.")
        return False

    if tipo == "ENTRADA":
        resultado = registrar_entrada(descripcion, cantidad, inventario, sesion.usuario_actual)
    else:
        resultado = registrar_salida(descripcion, cantidad, inventario, sesion.usuario_actual)

    print(f"{tipo.capitalize()} registrada con exito") if resultado else print("No se pudo realizar el movimiento")

def solicitar_registrar_entrada(sesion):
    return solicitar_registrar_movimiento(sesion, "ENTRADA")

def solicitar_registrar_salida(sesion):
    return solicitar_registrar_movimiento(sesion, "SALIDA")

def mostrar_tabla_movimientos(movimientos):
    if not movimientos:
        print(NO_HAY_MOVIMIENTOS)
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Seccion', 'Tipo', 'Cantidad', 'Descripcion', 'Trabajador']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_seccion.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,   
            producto.nombre,
            almacen.nombre,
            inventario.id_seccion.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
            movimiento.id_usuario.nombre
        ])
    print(tabla_movimiento)   

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

    mostrar_tabla_movimientos(movimientos)
     

def mostrar_movimientos_rango_fecha():
    fecha_inicio = forzar_fecha("Ingrese la fecha de inicio (DD-MM-YYYY): ", obligatorio=True)
    fecha_termino = forzar_fecha("Ingrese la fecha de termino (DD-MM-YYYY): ", obligatorio=True)       

    if fecha_inicio > fecha_termino:
        print("La fecha de inicio no puede ser posterior a la fecha de termino.")
        return False
    
    movimientos = listar_movimientos_por_rango_fecha(fecha_inicio, fecha_termino)
    mostrar_tabla_movimientos(movimientos)     

def mostrar_historial_movimientos():
    movimientos = listar_historial_movimientos()
    mostrar_tabla_movimientos(movimientos)      
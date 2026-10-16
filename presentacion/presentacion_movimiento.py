from negocio.negocio_movimiento import registrar_entrada, registrar_salida, lista_movimientos, validar_stock_salida, lista_movimientos_entrada, lista_movimientos_salida, lista_movimientos_rango_fecha
from auxiliares.entradas import campo_obligatorio, forzar_positivo, forzar_entero
from datetime import datetime
from prettytable import PrettyTable

def solicitar_registrar_entrada():
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
    fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
    inventario = forzar_entero("Ingrese el ID del inventario: ")
    resultado = registrar_entrada(descripcion, cantidad, fecha, inventario)
    print("Entrada registrada con exito.") if resultado else print("No se pudo realizar el movimiento")
        

def solicitar_registrar_salida():
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
    fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
    id_inventario = forzar_entero("Ingrese el ID del inventario: ")

    if validar_stock_salida(id_inventario, cantidad):
        print("La cantidad no debe superar al stock actual")
        return False
    
    resultado = registrar_salida(descripcion, cantidad, fecha, id_inventario)

    print("Salida registrada con exito.") if resultado else print("No se pudo realizar el movimiento")

def solicitar_consultar_movimiento():
    print("=== Consulta de Movimientos ===")
    opcion = campo_obligatorio("Ingrese el tipo de movimiento (ENTRADA/SALIDA): ").strip().upper()

    if opcion == "ENTRADA":
        movimientos = lista_movimientos_entrada()
    elif opcion == "SALIDA":
        movimientos = lista_movimientos_salida()
    else:
        print("Opción invaida. Por favor, escribe ENTRADA o SALIDA.\n")

    if not movimientos:
        print("No hay movimientos registrados.")
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
    fecha_inicio = input("Ingrese la fecha de inicio (DD-MM-YYYY): ")
    fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y").date()
    fecha_termino = input("Ingrese la fecha de termino (DD-MM-YYYY): ")       
    fecha_termino = datetime.strptime(fecha_termino, "%d-%m-%Y").date() 

    movimientos = lista_movimientos_rango_fecha(fecha_inicio, fecha_termino)
    if not movimientos:
        print("No hay movimientos registrados.")
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
    movimientos = lista_movimientos()

    if not movimientos:
        print("No hay movimientos registrados.")
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
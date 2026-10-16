from negocio.negocio_inventario import asociar_producto_a_almacen, obtener_inventario_producto, lista_inventario, lista_productos_stock_critico
from auxiliares.mensajes import SOLICITUD_ID_PRODUCTO, SOLICITUD_ID_ALMACEN
from auxiliares.entradas import forzar_entero, forzar_positivo
from negocio.negocio_producto import obtener_producto
from negocio.negocio_almacen import obtener_almacen
from prettytable import PrettyTable


def solicitar_asociar_producto_almacen():
    print("\n=== Asociar producto a un almacen ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    stock_actual = forzar_positivo("Ingrese la cantidad inicial: ")
    stock_minimo = forzar_positivo("Ingrese el stock minimo: ")

    resultado = asociar_producto_a_almacen(id_producto, id_almacen, stock_actual, stock_minimo)
    print("Producto asociado al almacen con exito.") if resultado else print("No se pudo asociar.")

def consultar_inventario_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    producto = obtener_producto(id_producto)
    almacen = obtener_almacen(id_almacen)

    inventario = obtener_inventario_producto(id_producto, id_almacen)
    if inventario is None:
        print(f"No hay inventario para el producto '{producto.nombre}' en el almacen '{almacen.nombre}'")
        return
            
    print(f"Producto: {producto.nombre}")
    print(f"Almacen: {almacen.nombre}")
    print(f"Stock Actual: {inventario.stock_actual}")
    print(f"Stock Minimo: {inventario.stock_minimo}")


def mostrar_inventario_almacen():
    
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)
    almacen = obtener_almacen(id_almacen)
    if almacen is None:
        print("No existe un almacén con ese ID.")
        return

    inventarios = lista_inventario(id_almacen)
    if not inventarios:
        print("El almacen esta vacio")
        return

    tabla_inventario = PrettyTable()
    tabla_inventario.field_names = ['ID Producto', 'Producto', 'Stock Actual', 'Stock Minimo']
    for inventario in inventarios:
        producto = inventario.id_producto
        tabla_inventario.add_row([
            producto.id_producto,
            producto.nombre,
            inventario.stock_actual,
            inventario.stock_minimo,
        ])
    print(f"=== Inventario de {almacen.nombre} ===")        
    print(tabla_inventario)        


def mostrar_productos_stock_critico():
    stock_critico = lista_productos_stock_critico()

    tabla_stock_critico = PrettyTable()
    tabla_stock_critico.field_names = ['ID Producto', 'Producto', 'Stock Actual', 'Stock Minimo', 'Almacen']
    for stock in stock_critico:
        producto = stock.id_producto
        almacen = stock.id_almacen
        tabla_stock_critico.add_row([
            producto.id_producto,
            producto.nombre,
            stock.stock_actual,
            stock.stock_minimo,
            almacen.nombre,
        ])
    print("=== Productos bajo stock minimo ===")        
    print(tabla_stock_critico)   

from prettytable import PrettyTable

from auxiliares.entradas import campo_obligatorio, forzar_positivo, forzar_entero
from negocio.negocio_producto import obtener_producto_sku
from negocio.negocio_almacen import listar_almacenes_activos
from negocio.negocio_inventario import listar_inventario_por_producto
from negocio.negocio_inventario import (
    asociar_producto_a_almacen, 
    listar_inventario_por_almacen, 
    listar_productos_stock_critico
)

# ------------ Funcion Auxiliar ------------

def solicitar_almacen():
    # Muestra los almacenes activos y devuelve el elegido o None
    almacenes = list(listar_almacenes_activos())

    if not almacenes:
        print("No hay almacenes registrados.")
        return None

    print("\nAlmacenes disponibles:")
    for i, almacen in enumerate(almacenes, start=1):
        print(f"[{i}] {almacen.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el almacen: ")

        if 1 <= seleccion <= len(almacenes):
            opcion_valida = True
            return almacenes[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(almacenes)}).")


def solicitar_asociar_producto_almacen():
    print("\n=== Asociar producto a un almacen ===")

    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe el producto con ese SKU.")
        return False

    almacen = solicitar_almacen()

    if almacen is None:
        return          
    
    stock_actual = forzar_positivo("Ingrese la cantidad inicial: ")
    stock_minimo = forzar_positivo("Ingrese el stock minimo: ")

    resultado = asociar_producto_a_almacen(producto.id_producto, almacen.id_almacen, stock_actual, stock_minimo)
    print(f"Producto '{producto.nombre}' asociado a '{almacen.nombre}'.") if resultado else print("No se pudo asociar.")

def consultar_inventario_producto():
    print("\n=== Consultar inventario de un producto ===")

    sku = campo_obligatorio("Ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe un producto con ese SKU.")
        return False

    inventarios = list(listar_inventario_por_producto(producto.id_producto))

    if not inventarios:
        print(f"El producto '{producto.nombre}' no está asociado a ningún almacén.")
        return False

    print(f"\nSKU: {producto.sku}")
    print("Almacenes donde se encuentra:")
    for i, inventario in enumerate(inventarios, start=1):
        print(f"[{i}] - {inventario.id_almacen.nombre}")

    opcion_valida = False

    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el almacén: ")

        if 1 <= seleccion <= len(inventarios):
            inventario = inventarios[seleccion - 1]
            opcion_valida = True
        else:
            print(f"Opción fuera de rango (1-{len(inventarios)}).")

    print("\n=== Inventario del producto ===")   
    print(f"Producto: {producto.nombre}")
    print(f"Almacen: {inventario.id_almacen.nombre}")
    print(f"Stock Actual: {inventario.stock_actual}")
    print(f"Stock Minimo: {inventario.stock_minimo}")

def mostrar_inventario_de_almacen():
    almacen = solicitar_almacen()

    if almacen is None:
        return

    inventarios = list(listar_inventario_por_almacen(almacen.id_almacen))

    if not inventarios:
        print("No hay productos registrados en el almacen.")
        return

    tabla_inventario = PrettyTable()
    tabla_inventario.field_names = ['Producto', 'SKU', 'Stock Actual', 'Stock Minimo']
    for inventario in inventarios:
        producto = inventario.id_producto
        tabla_inventario.add_row([
            producto.nombre,
            producto.sku,
            inventario.stock_actual,
            inventario.stock_minimo,
        ])
    print(f"=== Inventario de {almacen.nombre} ===")        
    print(tabla_inventario)        

def mostrar_productos_stock_critico():
    inventarios = list(listar_productos_stock_critico())

    if not inventarios:
        print("No hay productos bajo el stock minimo.")
        return
    
    tabla_stock_critico = PrettyTable()
    tabla_stock_critico.field_names = ['ID Producto', 'Producto', 'Stock Actual', 'Stock Minimo', 'Almacen']
    
    for stock in inventarios:
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

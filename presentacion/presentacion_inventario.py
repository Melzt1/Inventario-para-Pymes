from negocio.negocio_inventario import asociar_producto_a_almacen, lista_inventario, lista_productos_stock_critico
from auxiliares.entradas import campo_obligatorio, forzar_positivo, forzar_entero
from negocio.negocio_producto import obtener_producto_sku
from negocio.negocio_almacen import lista_almacenes
from negocio.negocio_inventario import lista_producto_inventario
from prettytable import PrettyTable


def solicitar_asociar_producto_almacen():
    print("\n=== Asociar producto a un almacen ===")

    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()

    producto = obtener_producto_sku(sku)
    if producto is None:
        print("No existe el producto con ese SKU.")
        return False
    
    id_producto = producto.id_producto

    almacenes = lista_almacenes()

    if not almacenes:
        print("No hay almacenes registrados.")
        return

    print("Almacenes disponibles:")

    for i, almacen in enumerate(almacenes, start=1):
        print(f"[{i}] - {almacen.nombre}")

    seleccion = forzar_entero("\nSeleccione el Almacen: ")  
    if 1 <= seleccion <= len(almacenes):
        almacen = almacenes[seleccion-1]
        id_almacen = almacen.id_almacen
    else:
        print("Opcion fuera de rango.")
        return False          
    
    stock_actual = forzar_positivo("Ingrese la cantidad inicial: ")
    stock_minimo = forzar_positivo("Ingrese el stock minimo: ")

    resultado = asociar_producto_a_almacen(id_producto, id_almacen, stock_actual, stock_minimo)
    print(f"Producto {producto.nombre} asociado al almacen con exito.") if resultado else print("No se pudo asociar.")

def consultar_inventario_producto():
    print("\n=== Consultar inventario de un producto ===")

    sku = campo_obligatorio("Ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe un producto con ese SKU.")
        return False

    inventarios = lista_producto_inventario(producto.id_producto)
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

def mostrar_inventario_almacen():
    almacenes = lista_almacenes()

    if not almacenes:
        print("No hay almacenes registrados.")
        return    

    for i, almacen in enumerate(almacenes, start=1):
        print(f"[{i}] - {almacen.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("Seleccione el almacen: ")

        if 1 <= seleccion <= len(almacenes):
            almacen = almacenes[seleccion - 1]
            opcion_valida = True
        else:
            print(f"Opción fuera de rango (1-{len(almacenes)}).")

    inventarios = lista_inventario(almacen.id_almacen)
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

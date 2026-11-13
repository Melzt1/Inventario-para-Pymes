from prettytable import PrettyTable

from auxiliares.entradas import campo_obligatorio, forzar_entero
from negocio.negocio_producto import obtener_producto_sku
from negocio.negocio_almacen import listar_almacenes_activos
from negocio.negocio_seccion import listar_secciones
from negocio.negocio_minimo_almacen import listar_stock_critico, obtener_minimo
from negocio.negocio_inventario import (
    asociar_producto_a_almacen, 
    listar_inventario_por_almacen,
    listar_inventario_por_producto
)

# ------------ Funcion Auxiliar ------------

def solicitar_almacen():
    # Muestra los almacenes activos y devuelve el elegido o None
    almacenes = listar_almacenes_activos()

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

def solicitar_seccion(almacen):
    secciones = list(listar_secciones(almacen))

    if not secciones:
        print("El almacén no tiene secciones activas.")
        return None
    
    for indice, seccion in enumerate(secciones, start=1):
        print(f"[{indice}] {seccion.nombre}")

    seleccion = forzar_entero("Seleccione la sección: ")

    if not 1 <= seleccion <= len(secciones):
        print(f"Opción fuera de rango (1-{len(secciones)}).")
        return None
    
    return secciones[seleccion - 1]        

def solicitar_asociar_producto_almacen():
    print("\n=== Registrar producto a un almacen ===")

    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe el producto con ese SKU.")     
        return

    almacen = solicitar_almacen()

    if almacen is None:
        return         
    
    seccion = solicitar_seccion(almacen)

    if seccion is None:
        return
    
    resultado = asociar_producto_a_almacen(producto, seccion)
    print(f"Producto '{producto.nombre}' asociado a '{almacen.nombre}'.") if resultado else print("No se pudo asociar.")

def consultar_inventario_producto():
    print("\n=== Consultar inventario de un producto ===")

    sku = campo_obligatorio("Ingrese el SKU del producto: ").strip()
    producto = obtener_producto_sku(sku)

    if producto is None:
        print("No existe un producto con ese SKU.")
        return 

    inventarios = listar_inventario_por_producto(producto.id_producto)

    if not inventarios:
        print(f"El producto '{producto.nombre}' no está asociado a ningún almacén.")
        return 

    tabla = PrettyTable()
    tabla.field_names = ["Almacen", "Seccinn", "Stock actual"]

    for inventario in inventarios:
        seccion = inventario.id_seccion
        tabla.add_row([
            seccion.id_almacen.nombre, 
            seccion.nombre, 
            inventario.stock_actual
        ])
    print(tabla)


def mostrar_inventario_de_almacen():
    almacen = solicitar_almacen()

    if almacen is None:
        return

    inventarios = listar_inventario_por_almacen(almacen.id_almacen)

    if not inventarios:
        print("No hay productos registrados en el almacen.")
        return

    tabla_inventario = PrettyTable()
    tabla_inventario.field_names = ['Seccion', 'Producto', 'SKU', 'Stock Actual', 'Stock Minimo']

    for inventario in inventarios:
        producto = inventario.id_producto
        seccion = inventario.id_seccion
        minimo = obtener_minimo(producto.id_producto, almacen.id_almacen)
        
        tabla_inventario.add_row([
            seccion.nombre,
            producto.nombre,
            producto.sku,
            inventario.stock_actual,
            minimo.stock_minimo
        ])
    print(f"=== Inventario de {almacen.nombre} ===")        
    print(tabla_inventario)        

def mostrar_productos_stock_critico():
    almacen = solicitar_almacen()

    if almacen is None:
        return    
    
    inventarios = listar_stock_critico(almacen)

    if not inventarios:
        print("No hay productos bajo el stock minimo.")
        return
    
    tabla_stock_critico = PrettyTable()
    tabla_stock_critico.field_names = ['Producto', 'Stock Actual', 'Stock Minimo']
    
    for producto, stock_actual, stock_minimo in inventarios:
        tabla_stock_critico.add_row([
            producto.nombre,
            stock_actual,
            stock_minimo,
        ])
    print("=== Productos bajo stock minimo ===")        
    print(tabla_stock_critico)   

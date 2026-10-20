from prettytable import PrettyTable

from auxiliares.mensajes import MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import (
    forzar_entero, 
    campo_obligatorio, 
    campo_opcional, 
    forzar_positivo, 
    forzar_fecha
)
from negocio.negocio_categoria import obtener_categoria
from negocio.negocio_producto import (
    registrar_producto, 
    sku_en_uso, 
    actualizar_producto, 
    desactivar_producto, 
    activar_producto, 
    listar_productos_activos, 
    buscar_productos
)

# Metodo auxiliar 
def solicitar_seleccion_producto():
    nombre = campo_obligatorio("Busque el producto por su nombre: ")

    productos = buscar_productos(nombre)

    if not productos:
        print("No hay productos con ese nombre.")
        return None

    for i, producto in enumerate(productos, start=1):
        print(f"[{i}] - {producto.nombre} ({producto.sku})")

    opcion_valida = False

    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el producto: ")  
        if 1 <= seleccion <= len(productos):
            producto = productos[seleccion-1]
            opcion_valida = True
            return producto
        
        print(f"Opcion fuera de rango (1-{len(productos)}).")

def mostrar_productos():
    productos = listar_productos_activos()

    if not productos:
        print("No hay productos registrados.")
        return

    tabla_productos = PrettyTable()
    tabla_productos.field_names = ['ID', 'Nombre', 'SKU', 'Precio Costo', 'Precio Venta', 'Descripcion', 'Fecha Elaboracion', 'Fecha Vencimiento', 'Estado', 'Categoria']

    for producto in productos:
        tabla_productos.add_row([
            producto.id_producto,
            producto.nombre,
            producto.sku,
            producto.precio_costo,
            producto.precio_venta,
            producto.descripcion,
            producto.fecha_elaboracion or '-',
            producto.fecha_vencimiento or '-',
            ('Inhabilitado', 'Habilitado')[producto.estado],
            producto.id_categoria.nombre,
        ])

    print(tabla_productos)

def solicitar_datos_producto():
    print("\n=== Registrar Producto ===")

    nombre = campo_obligatorio("Ingrese el nombre del producto: ")

    sku_valido = False
    while not sku_valido:
        sku = campo_obligatorio("Ingrese el SKU del producto: ")

        if sku_en_uso(sku):
            print(f"El SKU: '{sku}' ya fue registrado. Ingrese otro.")
            continue

        sku_valido = True

    precio_costo = forzar_positivo("Ingrese el precio costo del producto: ")
    precio_venta = forzar_positivo("Ingrese el precio venta del producto: ")
        
    while precio_venta < precio_costo:
        print("El precio de venta no puede ser menor que el precio costo")
        precio_venta = forzar_positivo("Ingrese el precio venta del producto: ")
    
    descripcion = campo_obligatorio("Ingrese la descripcion del producto: ")

    fecha_elaboracion = forzar_fecha("Ingrese la fecha de elaboracion 'DD-MM-YYYY' (ENTER si no aplica): ", obligatorio=False)
    fecha_vencimiento = forzar_fecha("Ingrese la fecha de vencimiento 'DD-MM-YYYY' (ENTER si no aplica): ", obligatorio=False)
    
    # Obtener el objeto Categoria por su ID para hacer la relacion
    id_categoria = forzar_entero("Ingrese la categoria (Ingrasar por ID):")
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, categoria)
    print("Producto registado con exito.") if resultado else print("No se pudo registrar el producto.")
              
def solicitar_consultar_producto():
    producto = solicitar_seleccion_producto()

    if producto is None:
        return False
    
    # La FK entrega el objeto Categoria
    categoria = producto.id_categoria

    estado = "Habilitado" if producto.estado else "Deshabilitado"
    fecha_elaboracion = producto.fecha_elaboracion or "No aplica"
    fecha_vencimiento = producto.fecha_vencimiento or "No aplica"

    # <18 es para alinear el texto 18 espacios a la izquierda y se vea ordenado
    print("\n=== Producto encontrado ===")
    print(f"{'ID':<18}: {producto.id_producto}")
    print(f"{'Nombre':<18}: {producto.nombre}")
    print(f"{'SKU':<18}: {producto.sku}")
    print(f"{'Precio costo':<18}: {producto.precio_costo}")
    print(f"{'Precio venta':<18}: {producto.precio_venta}")
    print(f"{'Descripcion':<18}: {producto.descripcion}")
    print(f"{'Fecha elaboracion':<18}: {fecha_elaboracion}")
    print(f"{'Fecha vencimiento':<18}: {fecha_vencimiento}")
    print(f"{'Estado':<18}: {estado}")
    print(f"{'Categoria':<18}: {categoria.nombre}\n")

def solicitar_actualizar_producto():
    producto = solicitar_seleccion_producto()

    if producto is None:
        return False

    id_producto = producto.id_producto

    nombre = campo_opcional("Ingrese el nuevo nombre", producto.nombre)
    sku = campo_opcional("Ingrese el nuevo SKU", producto.sku)

    # POR ALGUNA RAZON ESTA ESTUPIDEZ FUNCIONA XD
    if sku != producto.sku and sku_en_uso(sku, id_producto):
        print(f"El SKU '{sku}' ya se encuentra registrado.")
        return False

    precio_costo = input("Ingrese el nuevo precio de costo (ENTER para mantener): ")
    if precio_costo == "":
        precio_costo = producto.precio_costo
    else:
        precio_costo = int(precio_costo)    

    precio_venta = input("Ingrese el nuevo precio de venta (ENTER para mantener): ")
    if precio_venta == "":
        precio_venta = producto.precio_venta
    else:
        precio_venta = int(precio_venta)        

    descripcion = campo_opcional("Ingrese la nueva descripcion", producto.descripcion) 

    resultado =  actualizar_producto(id_producto, nombre, sku, precio_costo, precio_venta, descripcion)
    print("Producto actualizado con exito.") if resultado else print("No se pudo actualizar el producto.")

# FALTA VALIDAR QUE NO SE PUEDAN DESACTIVAR PRODUCTOS CON STOCK > 0    
def solicitar_desactivar_producto():
    producto = solicitar_seleccion_producto()

    if producto is None:
        return False

    id_producto = producto.id_producto

    resultado = desactivar_producto(id_producto)
    print("Producto desactivado con exito.") if resultado else print("No se pudo desactivar el producto.")

# FALTA FILTRAR LA BUSQUEDA SOLO POR PRODUCTO CON ESTADO DESACTIVADO
def solicitar_activar_producto():
    producto = solicitar_seleccion_producto()

    if producto is None:
        return False

    id_producto = producto.id_producto

    resultado = activar_producto(id_producto)
    print(f"Producto: {producto.nombre} Activado con exito") if resultado else print("No se pudo activar el producto.")
    


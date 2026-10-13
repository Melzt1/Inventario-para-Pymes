from negocio.negocio_producto import registrar_producto, sku_en_uso, obtener_producto, actualizar_producto, desactivar_producto, activar_producto, lista_productos
from negocio.negocio_categoria import obtener_categoria
from auxiliares.mensajes import MENSAJE_ID_NO_EXISTE, SOLICITUD_ID_PRODUCTO
from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional, forzar_positivo
from datetime import datetime
from prettytable import PrettyTable

""" Falta crear metodo para validar fechas en el ingreso de productos. """

def mostrar_productos():
    productos = lista_productos()

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
    nombre = campo_obligatorio("Ingrese el nombre del producto: ")
    sku = campo_obligatorio("Ingrese el SKU del producto: ")

    if sku_en_uso(sku):
        print(f"El SKU: '{sku}' ya fue registrado.")
        return False

    precio_costo = forzar_positivo("Ingrese el precio costo del producto: ")
    precio_venta = forzar_positivo("Ingrese el precio venta del producto: ")
        
    while precio_venta < precio_costo:
        print("El precio de venta no puede ser menor que el precio costo")
        precio_venta = forzar_positivo("Ingrese el precio venta del producto: ")
    
    descripcion = campo_obligatorio("Ingrese la descripcion del producto: ")

    fecha_elaboracion = input("Ingrese la fecha de elaboracion (DD-MM-YYYY): ")
    fecha_elaboracion = datetime.strptime(fecha_elaboracion, "%d-%m-%Y").date()

    fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD-MM-YYYY): ")
    fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d-%m-%Y").date()
    
    # Obtener el objeto Categoria por su ID para hacer la relacion
    id_categoria = forzar_entero("Ingrese la categoria (Ingrasar por ID):")
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, categoria)
    print("Producto registado con exito.") if resultado else print("No se pudo registrar el producto.")

def solicitar_consultar_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)

    producto = obtener_producto(id_producto)

    if producto is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    # La FK entrega el objeto Categoria, no el ID
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
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    producto = obtener_producto(id_producto)

    if producto is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    nombre = campo_opcional("Ingrese el nuevo nombre", producto.nombre)
    sku = campo_opcional("Ingrese el nuevo SKU", producto.sku)

    # POR ALGUNA RAZON ESTA ESTUPIDEZ FUNCIONA XD
    if sku != producto.sku and sku_en_uso(sku, id_producto):
        print(f"El SKU '{sku}' ya se encuentra registrado.")
        return False

    # hacklife para recibir un String vacio en una variable INT
    precio_costo = input("Ingrese el nuevo precio de costo (ENTER para mantener): ")
    if precio_costo == "":
        precio_costo = producto.precio_costo
    else:
        precio_costo = int(precio_costo)    
    
    # hacklife para recibir un String vacio en una variable INT
    precio_venta = input("Ingrese el nuevo precio de venta (ENTER para mantener): ")
    if precio_venta == "":
        precio_venta = producto.precio_venta
    else:
        precio_venta = int(precio_venta)        

    descripcion = campo_opcional("Ingrese la nueva descripcion", producto.descripcion) 

    resultado =  actualizar_producto(id_producto, nombre, sku, precio_costo, precio_venta, descripcion)
    print("Producto actualizado con exito.") if resultado else print("No se pudo actualizar el producto.")
    
def solicitar_desactivar_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    producto = obtener_producto(id_producto)

    if not producto:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = desactivar_producto(id_producto)
    print("Producto desactivado con exito.") if resultado else print("No se pudo desactivar el producto.")

def solicitar_activar_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    producto = obtener_producto(id_producto)

    if not producto:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = activar_producto(id_producto)
    print(f"Producto: {producto.nombre} Activado con exito") if resultado else print("No se pudo activar el producto.")
    


from datos.repositorios.repositorio_producto import listado_productos, guardar_productos, obtener_producto_por_id, existe_sku
from datos.modelos.producto import Producto
from prettytable import PrettyTable

def lista_productos():
    tabla_productos = PrettyTable()
    tabla_productos.field_names = ['ID', 'Nombre', 'SKU', 'Precio Costo', 'Precio Venta', 'Descripcion', 'Fecha Elaboracion', 'Fecha Vencimiento', 'Estado', 'ID Categoria']

    productos = listado_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        tabla_productos.add_row([
            producto.id_producto,
            producto.nombre,
            producto.sku,
            producto.precio_costo,
            producto.precio_venta,
            producto.descripcion,
            producto.fecha_elaboracion,
            producto.fecha_vencimiento,
            ('Inhabilitado', 'Habilitado')[producto.estado],
            producto.id_categoria
        ])
    print(tabla_productos)


def validar_precios_negativos(precio_costo, precio_venta):
    # True si ambos precios son positivos
    return precio_costo > 0 and precio_venta > 0

def validar_precio_venta(precio_costo, precio_venta):
    # True si el precio de venta es mayor o igual al costo.
    return precio_venta >= precio_costo

# Metodo CREATE
def registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, id_categoria):

    if not validar_precios_negativos(precio_costo, precio_venta):
        return False
    
    nuevo_producto = Producto()
    nuevo_producto.nombre = nombre
    nuevo_producto.sku = sku
    nuevo_producto.precio_costo = precio_costo
    nuevo_producto.precio_venta =precio_venta
    nuevo_producto.descripcion = descripcion
    nuevo_producto.fecha_elaboracion = fecha_elaboracion
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    nuevo_producto.id_categoria = id_categoria
    return guardar_productos(nuevo_producto)

# Validacion Unique
def sku_en_uso(sku, id_producto=None):
    return existe_sku(sku, id_producto)

# Metodo para obtener el objeto por su id
def obtener_producto(id_producto):
    return obtener_producto_por_id(id_producto)

# Metodo READ

# Metodo UPDATE
def actualizar_producto(id_producto, nombre, sku, precio_venta, descripcion):
    producto = obtener_producto(id_producto)

    # Si no ecuentra el ID dejamos de actualizar
    if producto is None:
        return False

    # Verificamos que otro producto no tenga el nuevo SKU
    if sku != producto.sku and sku_en_uso(sku, id_producto):    
        return False
    
    # Si encuentra el ID seteamos los nuevos parametros 
    producto.nombre = nombre
    producto.sku = sku
    producto.precio_venta = precio_venta
    producto.descripcion = descripcion

    # Reutilizamos la funcion ya que utiliza (.save)
    return guardar_productos(producto)


# Metodo Delete (borrado logico)
def desactivar_producto(id_producto):
    producto = obtener_producto(id_producto)

    if producto is None:
        return False

    producto.estado = False
    return guardar_productos(producto)

def activar_producto(id_producto):
    producto = obtener_producto(id_producto)

    if producto is None:
        return False

    producto.estado = True
    return guardar_productos(producto)
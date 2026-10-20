from peewee import PeeweeException

from datos.modelos.producto import Producto
from datos.repositorios.repositorio_producto import (
    listar_productos, 
    listar_productos_desactivados,
    guardar_producto, 
    obtener_producto_por_id, 
    existe_sku, 
    obtener_producto_por_sku, 
    buscar_productos_por_nombre, 
)

# ------------ Validaciones ------------

def precio_costo_valido(precio_costo):
    return precio_costo > 0

def precio_venta_valido(precio_venta):
    return precio_venta > 0

def precio_venta_mayor_o_igual_al_costo(precio_costo, precio_venta):
    return precio_venta >= precio_costo

# Validacion Unique
def sku_en_uso(sku, id_producto=None):
    return existe_sku(sku, id_producto)

# ------------ Lectura ------------

def listar_productos_activos():
    return listar_productos()

def listar_productos_inactivos():
    return listar_productos_desactivados()

def buscar_productos(nombre):
    return buscar_productos_por_nombre(nombre)

def obtener_producto(id_producto):
    return obtener_producto_por_id(id_producto)

def obtener_producto_sku(sku):
    return obtener_producto_por_sku(sku)

# ------------ Escritura ------------

def registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, id_categoria):
    if sku_en_uso(sku):
        return False

    if not precio_costo_valido(precio_costo):
        return False

    if not precio_venta_valido(precio_venta):
        return False

    if not precio_venta_mayor_o_igual_al_costo(precio_costo, precio_venta):
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

    try:
        return guardar_producto(nuevo_producto)
    except PeeweeException:
        return False

def actualizar_producto(producto: Producto, nombre, sku, precio_costo, precio_venta, descripcion):
    if producto is None:
        return False

    # Verificamos que otro producto no tenga el nuevo SKU
    if sku != producto.sku and sku_en_uso(sku, producto.id_producto):    
        return False

    if not precio_costo_valido(precio_costo):
        return False

    if not precio_venta_valido(precio_venta):
        return False

    if not precio_venta_mayor_o_igual_al_costo(precio_costo, precio_venta):
        return False
        
    producto.nombre = nombre
    producto.sku = sku
    producto.precio_costo = precio_costo
    producto.precio_venta = precio_venta
    producto.descripcion = descripcion

    try:
        return guardar_producto(producto)
    except PeeweeException:
        return False


# ------------ Borrado logico ------------

def desactivar_producto(producto: Producto):
    if producto is None:
        return False

    producto.estado = False

    try:
        return guardar_producto(producto)
    except PeeweeException:
        return False

def activar_producto(producto: Producto):
    if producto is None:
        return False

    producto.estado = True

    try:
        return guardar_producto(producto)
    except PeeweeException:
        return False


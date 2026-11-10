from peewee import PeeweeException

from datos.modelos.inventario import Inventario
from datos.modelos.producto import Producto
from datos.modelos.seccion import Seccion
from datos.repositorios.repositorio_inventario import (
    guardar_inventario, 
    obtener_inventario, 
    listar_inventario_de_almacen,
    listar_inventario_de_producto
)

# ------------ Lectura ------------

# Lista los productos registrados en un Almacen con su Stock
def listar_inventario_por_almacen(id_almacen):
    return listar_inventario_de_almacen(id_almacen)

# Lista el inventario de un producto X
def listar_inventario_por_producto(id_producto):
    return listar_inventario_de_producto(id_producto)

def obtener_inventario_producto_almacen(id_producto, id_almacen):
    return obtener_inventario(id_producto, id_almacen)

def listar_productos_stock_critico():
    return []

# ------------ Escritura ------------

# Regla de negocio:
# al registra un producto en un almacen, el stock siempre parte en 0 y solo cambia con un movimiento
# El stock minimo se mueve a: MinimoAlmacen

def asociar_producto_a_almacen(producto: Producto, seccion: Seccion):
    if producto is None or seccion is None:
        return False

    # Si ya existe la relacion, no se duplica 
    if obtener_inventario(producto.id_producto, seccion.id_seccion) is not None:
        return False

    inventario = Inventario()
    inventario.id_producto = producto
    inventario.id_seccion = seccion
    inventario.stock_actual = 0

    try:
        return guardar_inventario(inventario)   
    except PeeweeException:
        return False


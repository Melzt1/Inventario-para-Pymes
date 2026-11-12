from peewee import PeeweeException

from datos.modelos.minimo_almacen import MinimoAlmacen
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen
from datos.modelos.inventario import Inventario

from datos.repositorios.repositorio_inventario import listar_inventario_producto_almacen
from datos.repositorios.repositorio_minimo_almacen import (
    crear_minimo,
    guardar_minimo,
    obtener_stock_minimo
)

def obtener_minimo(id_producto, id_almacen):
    return obtener_stock_minimo(id_producto, id_almacen)

def definir_minimo(producto: Producto, almacen: Almacen, stock_minimo):
    if producto is None or almacen is None:
        return False

    # validar que no este vacio y que sea mayor igual a cero
    if stock_minimo is None or stock_minimo < 0:
        return False

    # Solo se puede definir 1 stock_minimo por producto de un almacen
    if obtener_minimo(producto.id_producto, almacen.id_almacen) is not None:
        return False

    try:
        return crear_minimo(producto, almacen, producto, stock_minimo)
    except PeeweeException:
        return False

def actualizar_minimo(producto: Producto, almacen: Almacen, stock_minimo):
    if producto is None or almacen is None:
        return False

    if stock_minimo is None or stock_minimo < 0:
        return False

    # obtenemos la instancia para actualizarla
    minimo = obtener_minimo(producto.id_producto, almacen.id_almacen)

    if minimo is None:
        return False

    minimo.stock_minimo = stock_minimo

    try:
        return guardar_minimo(minimo)
    except PeeweeException:
        return False        


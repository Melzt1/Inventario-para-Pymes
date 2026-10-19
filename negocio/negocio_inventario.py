from datos.modelos.inventario import Inventario
from datos.repositorios.repositorio_inventario import (
    guardar_inventario, 
    obtener_inventario, 
    listar_inventario_de_almacen,
    listar_inventario_stock_critico, 
    listar_inventario_de_producto
)
from negocio.negocio_producto import obtener_producto
from negocio.negocio_almacen import obtener_almacen

# ------------ Lectura ------------

def listar_inventario_por_almacen(id_almacen):
    return listar_inventario_de_almacen(id_almacen)

def listar_inventario_por_producto(id_producto):
    return listar_inventario_de_producto(id_producto)

def listar_productos_stock_critico():
    return listar_inventario_stock_critico()

def obtener_inventario_producto_almacen(id_producto, id_almacen):
    return obtener_inventario(id_producto, id_almacen)


# ------------ Escritura ------------

def asociar_producto_a_almacen(id_producto, id_almacen, stock_actual, stock_minimo):
    if obtener_producto(id_producto) is None:
        return False

    if obtener_almacen(id_almacen) is None:
        return False

    if stock_actual < 0 or stock_minimo < 0:
        return False

    # Si ya existe la relacion, no se duplica 
    if obtener_inventario(id_producto, id_almacen) is not None:
        return False

    inventario = Inventario()
    inventario.id_producto = id_producto
    inventario.id_almacen = id_almacen
    inventario.stock_actual = stock_actual
    inventario.stock_minimo = stock_minimo

    return guardar_inventario(inventario)


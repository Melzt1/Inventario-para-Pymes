from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

from negocio.negocio_inventario import consultar_stock_total
from datos.repositorios.repositorio_minimo_almacen import (
    crear_minimo,
    guardar_minimo,
    obtener_stock_minimo,
    listar_minimo_almacen
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

    return crear_minimo(producto, almacen, stock_minimo)


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

    return guardar_minimo(minimo)
   

def listar_stock_critico(almacen: Almacen):
    if almacen is None:
        return []

    stock_critico = []

    minimos = listar_minimo_almacen(almacen.id_almacen)

    for minimo in minimos:
        producto = minimo.id_producto

        # si encuentra un producto deshabilitado lo salta
        if not producto.estado:
            continue 

        stock_actual = consultar_stock_total(producto, almacen)

        if stock_actual is not None and stock_actual < minimo.stock_minimo:
            stock_critico.append((producto, stock_actual, minimo.stock_minimo))

    return stock_critico

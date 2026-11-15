from peewee import PeeweeException

from datos.modelos.inventario import Inventario
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen
from datos.modelos.seccion import Seccion
from datos.modelos.models import database
from datos.repositorios.repositorio_inventario import (
    guardar_inventario, 
    obtener_inventario, 
    listar_inventario_de_almacen,
    listar_inventario_de_producto,
    listar_inventario_producto_almacen
)

# ------------ Lectura ------------

def listar_inventario_por_almacen(id_almacen):
    return listar_inventario_de_almacen(id_almacen)

def listar_inventario_por_producto(id_producto):
    return listar_inventario_de_producto(id_producto)

def obtener_inventario_producto_seccion(id_producto, id_seccion):
    return obtener_inventario(id_producto, id_seccion)

def consultar_stock_total(producto: Producto, almacen: Almacen):
    if producto is None or almacen is None:
        return False

    inventarios = listar_inventario_producto_almacen(producto.id_producto, almacen.id_almacen)

    # expresion generadora, un for que recorre la lista inventarios y va sumando el stock_acutal por cada iteracion
    return sum(inventario.stock_actual for inventario in inventarios)

# ------------ Escritura ------------

def asociar_producto_a_almacen(producto: Producto, seccion: Seccion, stock_minimo):
    # FIX para el error de peewee: circular import
    from negocio.negocio_minimo_almacen import obtener_minimo, definir_minimo

    if producto is None or seccion is None:
        return False

    # Si ya existe la relacion, no se duplica 
    if obtener_inventario(producto.id_producto, seccion.id_seccion) is not None:
        return False

    # Al momento de registrar un producot al inventario se debe definir el stock_minimo

    try:
        with database.atomic():
            minimo = obtener_minimo(producto.id_producto, seccion.id_almacen)
            almacen = seccion.id_almacen

            # El stock minimo solo se define cuando el producto es nuevo (None)
            if minimo is None:
                if not definir_minimo(producto, almacen, stock_minimo):
                    raise ValueError ("No se pudo definir el mi nimo.")
                
            inventario = Inventario()
            inventario.id_producto = producto
            inventario.id_seccion = seccion
            inventario.stock_actual = 0
            guardar_inventario(inventario)   

        return True
    
    except (PeeweeException, ValueError):
        return False            



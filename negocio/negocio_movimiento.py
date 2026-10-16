from datos.modelos.movimiento import Movimiento
from datos.repositorios.repositorio_movimiento import registrar_movimiento, listado_movimientos, obtener_movimiento_entrada, obtener_movimiento_salida, obtener_movimiento_rango_fecha
from datos.repositorios.repositorio_movimiento import sumar_stock, restar_stock
from datos.repositorios.repositorio_inventario import obtener_inventario_id
from datos.modelos.models import database
from peewee import PeeweeException

def lista_movimientos():
    return listado_movimientos()

def registrar_entrada(descripcion, cantidad, fecha, id_inventario):
    if cantidad <= 0:
        return False
    try:
        # atomic() en que caso de que falle el registro se revierta la suma de stock
        with database.atomic():

            # hace la consulta para sumar stock y devuelve cuantas filas modifico (0-1)
            filas_actualizadas = sumar_stock(id_inventario, cantidad)

            # si devuelve 0 es porque no puedo realizar la operacion o no encontro el ID inventario 
            if filas_actualizadas == 0:
                return False # retornamos False para evitar registrar una entrada sin sumar stock

            movimiento = Movimiento()
            movimiento.descripcion = descripcion
            movimiento.cantidad = cantidad
            movimiento.fecha = fecha
            movimiento.id_inventario = id_inventario
            movimiento.tipo = "ENTRADA"

            registrar_movimiento(movimiento)
        return True
    
    except PeeweeException:
        return False

def validar_stock_salida(id_inventario, cantidad):
    if cantidad <= 0:
        return False
    
    inventario = obtener_inventario_id(id_inventario)

    if inventario is None:
        return False
    
    if cantidad > inventario.stock_actual:
        return False
    
    return True

def registrar_salida(descripcion, cantidad, fecha, id_inventario):
    if cantidad <= 0:
        return False
    try:
        # atomic() en que caso de que falle el registro se revierta el descuento de stock
        with database.atomic():

            # hace la consulta para descontar stock y devuelve cuantas filas modifico (0-1)
            filas_actualizadas = restar_stock(id_inventario, cantidad)

            # si devuelve 0 es porque no encontro el ID inventario o no hay stock suficiente
            if filas_actualizadas == 0:
                return False # retornamos False para evitar registrar una salida sin descontar stock

            movimiento = Movimiento()
            movimiento.descripcion = descripcion
            movimiento.cantidad = cantidad
            movimiento.fecha = fecha
            movimiento.id_inventario = id_inventario
            movimiento.tipo = "SALIDA"

            registrar_movimiento(movimiento)
        return True
    
    except PeeweeException:
        return False

def lista_movimientos_entrada():
    return obtener_movimiento_entrada()

def lista_movimientos_salida():
    return obtener_movimiento_salida()

def lista_movimientos_rango_fecha(fecha_inicio, fecha_termino):
    return obtener_movimiento_rango_fecha(fecha_inicio, fecha_termino)
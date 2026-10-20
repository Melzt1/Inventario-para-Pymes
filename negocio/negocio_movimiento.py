from peewee import PeeweeException

from datos.modelos.models import database
from datos.modelos.movimiento import Movimiento
from datos.modelos.inventario import Inventario
from datos.repositorios.repositorio_movimiento import (
    guardar_movimiento, 
    listar_movimientos, 
    listar_movimientos_de_entrada, 
    listar_movimientos_de_salida, 
    listar_movimientos_entre_fechas,
    restar_stock,
    sumar_stock
)

# ------------ Lectura ------------

def listar_historial_movimientos():
    return listar_movimientos()

def listar_movimientos_de_entrada():
    return listar_movimientos_de_entrada()

def listar_movimientos_de_salida():
    return listar_movimientos_de_salida()

def listar_movimientos_por_rango_fecha(fecha_inicio, fecha_termino):
    return listar_movimientos_entre_fechas(fecha_inicio, fecha_termino)

# ------------ Validaciones ------------

def validar_stock_salida(inventario: Inventario, cantidad):
    if inventario is None:
        return False

    if cantidad <= 0:
        return False
    
    if cantidad > inventario.stock_actual:
        return False
    
    return True

# ------------ Escritura ------------

def registrar_entrada(descripcion, cantidad, fecha, id_inventario):
    if cantidad <= 0:
        return False
    try:
        # atomic() si falla el registro del movimient, se revierte la suma de stock
        with database.atomic():

            # Suma el stock y devuelve cuantas filas modifico (0 o 1)
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

            guardar_movimiento(movimiento)
        return True
    
    except PeeweeException:
        return False


def registrar_salida(descripcion, cantidad, fecha, id_inventario):
    if cantidad <= 0:
        return False
    try:
        # atomic: si falla el registro del movimiento, se revierte el descuento de stock
        with database.atomic():

            # Descuenta stock y devuelve cuantas filas modifico (0 o 1)
            filas_actualizadas = restar_stock(id_inventario, cantidad)

            # 0 filas significa que no existe el inventario o no hay stock suficiente
            if filas_actualizadas == 0:
                return False 

            movimiento = Movimiento()
            movimiento.descripcion = descripcion
            movimiento.cantidad = cantidad
            movimiento.fecha = fecha
            movimiento.id_inventario = id_inventario
            movimiento.tipo = "SALIDA"

            guardar_movimiento(movimiento)
        return True
    
    except PeeweeException:
        return False


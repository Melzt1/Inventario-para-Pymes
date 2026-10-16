from datos.modelos.movimiento import Movimiento
from datos.repositorios.repositorio_movimiento import registrar_movimiento, listado_movimientos, obtener_movimiento_entrada, obtener_movimiento_salida, obtener_movimiento_rango_fecha
from datos.repositorios.repositorio_movimiento import sumar_stock, restar_stock
from datos.repositorios.repositorio_inventario import obtener_inventario_id

def lista_movimientos():
    return listado_movimientos()

def registrar_entrada(descripcion, cantidad, fecha, id_inventario):
    movimiento = Movimiento()

    movimiento.descripcion = descripcion
    movimiento.cantidad = cantidad
    movimiento.fecha = fecha
    movimiento.id_inventario = id_inventario
    movimiento.tipo = 'ENTRADA'
    sumar_stock(id_inventario, cantidad)
    return registrar_movimiento(movimiento)

def validar_stock_salida(id_inventario, cantidad):
    inventario = obtener_inventario_id(id_inventario)

    if inventario is None:
        return False
    
    if cantidad > inventario.stock_actual:
        return False

def registrar_salida(descripcion, cantidad, fecha, id_inventario):
    validar_stock_salida(id_inventario, cantidad)

    movimiento = Movimiento()
    movimiento.descripcion = descripcion
    movimiento.cantidad = cantidad
    movimiento.fecha = fecha
    movimiento.id_inventario = id_inventario
    movimiento.tipo = 'SALIDA'
    restar_stock(id_inventario, cantidad)
    return registrar_movimiento(movimiento)

def lista_movimientos_entrada():
    return obtener_movimiento_entrada()

def lista_movimientos_salida():
    return obtener_movimiento_salida()

def lista_movimientos_rango_fecha(fecha_inicio, fecha_termino):
    return obtener_movimiento_rango_fecha(fecha_inicio, fecha_termino)
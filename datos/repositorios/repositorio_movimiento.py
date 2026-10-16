from datos.modelos.movimiento import Movimiento
from datos.modelos.inventario import Inventario
from peewee import IntegrityError, PeeweeException, OperationalError, DataError

def sumar_stock(id_inventario, cantidad):
    return Inventario.update(stock_actual=Inventario.stock_actual + cantidad).where(Inventario.id_inventario == id_inventario).execute()

def restar_stock(id_inventario, cantidad):
    return Inventario.update(stock_actual=Inventario.stock_actual - cantidad).where(Inventario.id_inventario == id_inventario).execute()

def registrar_movimiento(movimiento: Movimiento):
    try:
        movimiento.save()
        return True
    
    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
        
    return False

def listado_movimientos():
    return Movimiento.select()

def obtener_movimiento_entrada():
    return Movimiento.select().where(Movimiento.tipo == "ENTRADA")

def obtener_movimiento_salida():
    return Movimiento.select().where(Movimiento.tipo == "SALIDA")

def obtener_movimiento_rango_fecha(fecha_inicio, fecha_termino):
    return Movimiento.select().where(Movimiento.fecha.between(fecha_inicio, fecha_termino))
from peewee import IntegrityError, PeeweeException, OperationalError, DataError

from datos.modelos.movimiento import Movimiento
from datos.modelos.inventario import Inventario

# ------------ Lectura ------------

def listar_movimientos():
    return Movimiento.select()

def listar_movimientos_de_entrada_repo():
    return Movimiento.select().where(Movimiento.tipo == "ENTRADA")

def listar_movimientos_de_salida_repo():
    return Movimiento.select().where(Movimiento.tipo == "SALIDA")

def listar_movimientos_entre_fechas(fecha_inicio, fecha_termino):
    return Movimiento.select().where(Movimiento.fecha.between(fecha_inicio, fecha_termino))

# ------------ Escritura ------------

def sumar_stock(id_inventario, cantidad):
    return (Inventario
            .update(stock_actual=Inventario.stock_actual + cantidad)
            .where(Inventario.id_inventario == id_inventario)
            .execute())

def restar_stock(id_inventario, cantidad):
    return (Inventario
            .update(stock_actual=Inventario.stock_actual - cantidad)
            .where((Inventario.id_inventario == id_inventario) & 
                   (Inventario.stock_actual >= cantidad))
            .execute())

def guardar_movimiento(movimiento: Movimiento):
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


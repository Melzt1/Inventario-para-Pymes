from datos.modelos.almacen import Almacen
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_almacenes():
    return Almacen.select().where(Almacen.estado == True) #para ocultar las de borrado logico

def guardar_almacen(almacen:Almacen):
    try:
        return almacen.save()
    
    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False

# obtener el objeto almacen por su ID 
# get_or_none me ahorra el try except DoesNotExist y si no encuentra el ID retorna None (es un todo en uno)
def obtener_almacen_por_id(id_almacen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almacen)
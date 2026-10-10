from datos.modelos.almacen import Almacen
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_almacenes():
    return Almacen.select()

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
    finally:
        print("Proceso finalizado.")

    return False

# obtener el objeto almacen por su ID
def obtener_almacen_por_id(id_almacen):
    try:
        return Almacen[id_almacen]
    except Almacen.DoesNotExist:
        return None
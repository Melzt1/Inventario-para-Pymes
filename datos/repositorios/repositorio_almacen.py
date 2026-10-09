from datos.modelos.almacen import Almacen
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_almacenes():
    almacenes = Almacen.select()
    if almacenes:
        return almacenes

def guardar_almacen(almacen:Almacen):
    try:
        guardar = almacen.save()
        if guardar:
            print(f"Almacen guardado con exito con ID: {almacen.id_almacen}")
        return True

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
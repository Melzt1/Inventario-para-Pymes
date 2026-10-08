# from peewee import 
from datos.modelos.direccion import Direccion
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def guardar_direcciones(direccion: Direccion):
    try:
        guardar_direccion = direccion.save()
        return guardar_direccion
    
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
        
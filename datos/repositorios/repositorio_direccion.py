from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.direccion import Direccion

def guardar_direccion(direccion: Direccion):
    try:
        direccion.save()
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
        
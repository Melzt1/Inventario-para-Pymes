from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.seccion import Seccion

# ------------ Lectura ------------

def listar_secciones_de_almacen(id_almacen):
    return Seccion.select().where(Seccion.id_almacen == id_almacen)

# ------------ Escritura ------------

def guardar_seccion(seccion:Seccion):
    try:
        seccion.save()
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

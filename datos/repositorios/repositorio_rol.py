from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.rol import Rol

# ------------ Lectura ------------
def listado_roles():
    return Rol.select().order_by(Rol.nombre)

# ------------ Escritura ------------

# .save() sirve para CREATE y UPDATE 
def guardar_rol(rol:Rol):
    try:
        rol.save()
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

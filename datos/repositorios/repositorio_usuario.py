from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol

# ------------ Lectura ------------
def listar_usuarios():
    return Usuario.select().where(Usuario.estado == True).order_by(Usuario.nombre)

def obtener_usuario_por_nombre(usuario):
    return Usuario.get_or_none(Usuario.usuario == usuario)

# Metodo para preguntar si el usuario tiene algun rol, para poder logearse
def existe_usuario_con_rol(rol):
    return (Usuario
            .select()
            .join(Rol)
            .where(rol.nombre == rol)
            .exists())

# ------------ Escritura ------------

# .save() sirve para CREATE y UPDATE 
def guardar_usuario(usuario:Usuario):
    try:
        usuario.save()
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



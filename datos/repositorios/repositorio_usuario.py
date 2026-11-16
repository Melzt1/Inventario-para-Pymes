from peewee import (IntegrityError,
                    OperationalError,
                    DataError,
                    PeeweeException)

from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol

# ------------ Lectura ------------

def listar_usuarios():
    return Usuario.select().where(Usuario.estado == True)

def listar_trabajores_asignables():
    return (Usuario
            .select(Usuario)
            .join(Rol)
            .where((Usuario.estado == True) & (Rol.nombre != "Administrador")))

def listar_usuarios_desactivados():
    return Usuario.select().where(Usuario.estado == False)

def obtener_usuario_por_id(id_usuario):
    return Usuario.get_or_none(Usuario.id_usuario == id_usuario)

def obtener_usuario_por_nombre_usuario(nombre_usuario):
    return Usuario.get_or_none(Usuario.usuario == nombre_usuario)

# Consultar todos los usuarios administradores exceptuando el que esta logeado
def hay_otro_administrador(id_usuario):
    return (Usuario
            .select()
            .join(Rol)
            .where((Usuario.estado == True) & 
                   (Rol.nombre == "Administrador") &
                   (Usuario.id_usuario != id_usuario))
            .exists())

# ------------ Escritura ------------

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


def existe_nombre_usuario(usuario, id_usuario=None):
    consulta = Usuario.select().where(Usuario.usuario == usuario)

    if id_usuario is not None:
        consulta = consulta.where(Usuario.id_usuario != id_usuario)
    return consulta.exists()
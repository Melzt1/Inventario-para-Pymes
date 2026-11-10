from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.usuario_almacen import UsuarioAlmacen
from datos.modelos.usuario import Usuario
from datos.modelos.almacen import Almacen

# ------------ Lectura ------------

# Listado de usuarios que trabajan en un Almacen
def listado_almacenes_de_usuario(id_usuario):
    return (Usuario
            .select()
            .join(UsuarioAlmacen)
            .where(UsuarioAlmacen.id_usuario == id_usuario))

# Listado de almacenes en los que trabaja X trabajador
def listado_usuarios_de_almacen(id_almacen):
    return (Almacen
            .select()
            .join(UsuarioAlmacen)
            .where(UsuarioAlmacen.id_almacen == id_almacen))

def obtener_asignacion(id_usuario, id_almacen):
    return UsuarioAlmacen.get_or_none(
        (UsuarioAlmacen.id_usuario == id_usuario) &
        (UsuarioAlmacen.id_almacen == id_almacen)
    )

# ------------ Escritura ------------

# .save() sirve para CREATE y UPDATE 
def asignar_usuario(asignacion:UsuarioAlmacen):
    try:
        asignacion.save()
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

def eliminar_asignacion(asignacion: UsuarioAlmacen):
    try:
        return asignacion.delete_instance()
    
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False      


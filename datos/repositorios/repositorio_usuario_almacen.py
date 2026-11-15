from peewee import IntegrityError,OperationalError,DataError,PeeweeException
from datos.modelos.usuario_almacen import UsuarioAlmacen
from datos.modelos.almacen import Almacen
from datos.modelos.usuario import Usuario



# ------------ Lectura ------------
def listar_almacenes_de_usuario(id_usuario):
    return (UsuarioAlmacen
            .select(UsuarioAlmacen, Almacen)
            .join(Almacen)
            .where(UsuarioAlmacen.id_usuario == id_usuario))

def listar_usuarios_de_almacen(id_almacen):
    return (UsuarioAlmacen
            .select(UsuarioAlmacen, Usuario)
            .join(Usuario)
            .where(UsuarioAlmacen.id_almacen == id_almacen))

#validacion 
def existe_usuario_almacen(id_usuario,id_almacen):
    return (UsuarioAlmacen
            .select()
            .where(
                (UsuarioAlmacen.id_usuario == id_usuario) &
                (UsuarioAlmacen.id_almacen == id_almacen))
            .exists())


# ------------ Escritura ------------
# en el diagrama MER, viene por defecto que un usuario no es encargado de un almacen, por eso el default es False
def asignar_usuario(id_usuario,id_almacen,es_encargado=False):
    try:
        UsuarioAlmacen.create(
            id_usuario = id_usuario,
            id_almacen = id_almacen,
            es_encargado = es_encargado
        )
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

def quitar_usuario_almacen(id_usuario, id_almacen):
    return (UsuarioAlmacen
            .delete()
            .where((UsuarioAlmacen.id_usuario == id_usuario) &
                   (UsuarioAlmacen.id_almacen == id_almacen))
            .execute())

def cambiar_encargado(id_usuario,id_almacen,es_encargado):
    return (UsuarioAlmacen
            .update(es_encargado=es_encargado)
            .where(
                (UsuarioAlmacen.id_usuario == id_usuario) &
                (UsuarioAlmacen.id_almacen == id_almacen))
            .execute())
    
def quitar_marca_encargado(id_almacen):
    return (UsuarioAlmacen
            .update(es_encargado=False)
            .where((UsuarioAlmacen.id_almacen == id_almacen) &
                   (UsuarioAlmacen.es_encargado == True))
            .execute())
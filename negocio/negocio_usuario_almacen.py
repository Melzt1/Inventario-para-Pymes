from peewee import PeeweeException

from datos.modelos.usuario import Usuario
from datos.modelos.almacen import Almacen
from datos.modelos.usuario_almacen import UsuarioAlmacen

from datos.repositorios.repositorio_usuario_almacen import(
    asignar_usuario,
    eliminar_asignacion,
    obtener_asignacion
)

def asignar_usuario(usuario: Usuario, almacen: Almacen):

    # Validar que los objetos existan
    if usuario is None or almacen is None:
        return False

    # No permitir asginar usuarios y almacenes en estado desactivado
    if not usuario.estado or not almacen.estado:
        return False

    usuario_almacen = UsuarioAlmacen()
    usuario_almacen.id_usuario = usuario
    usuario_almacen.id_almacen = almacen

    try:
        return asignar_usuario(usuario_almacen)
    except PeeweeException:
        return False


def quitar_usuario(usuario: Usuario, almacen: Almacen):
    if usuario is None or almacen is None:
        return False

    asignacion = obtener_asignacion(usuario.id_usuario, almacen.id_almacen)

    if asignacion is None:
        return False
    try:
        return eliminar_asignacion(asignacion)
    except PeeweeException:
        return False

def cambiar_encargado(usuario: Usuario, almacen: Almacen):
    pass
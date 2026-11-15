from peewee import PeeweeException

from datos.modelos.models import database
from datos.modelos.usuario import Usuario
from datos.modelos.almacen import Almacen


from datos.repositorios.repositorio_usuario_almacen import(
    guardar_asignacion,
    eliminar_asignacion,
    obtener_asignacion,
    listado_almacenes_de_usuario,
    listado_usuarios_de_almacen,
    obtener_encargado,
    quitar_encargado_de_almacen,
    actualizar_asignacion
)

def listar_almacenes_de_usuario(id_usuario):
    return listado_almacenes_de_usuario(id_usuario)

def listar_usuarios_de_almacen(id_almacen):
    return listado_usuarios_de_almacen(id_almacen)

def es_encargado(id_usuario, id_almacen):
    return obtener_encargado(id_usuario, id_almacen)

def asignar_usuario(usuario: Usuario, almacen: Almacen):

    # Validar que los objetos existan
    if usuario is None or almacen is None:
        return False

    if not usuario.estado or not almacen.estado:
        return False

    # Administrador no le asigna almacen, accede a todos por su rol
    if usuario.id_rol.nombre == "Administrador":
        return False

    # No se puede volver asignar un usario 2 veces al mismo almacen
    if obtener_asignacion(usuario.id_usuario, almacen.id_almacen) is not None:
        return False

    try:
        return guardar_asignacion(usuario.id_usuario, almacen.id_almacen)
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
    if usuario is None or almacen is None:
        return False

    # comprobamos que el usuario este asignado al almacen
    asignacion = obtener_asignacion(usuario.id_usuario, almacen.id_almacen)
    if asignacion is None:
        return False

    try:
        # usamos atomic() para ganarantizar que ambos cambios se realicen o se revierta
        with database.atomic():
            # busca si en el almacen hay un encargado y lo cambia a False
            quitar_encargado_de_almacen(almacen.id_almacen)

            # asignamos como encargado al nuevo usuario (asignacion contiene su id_usuario)
            asignacion.es_encargado = True

            # intentamos actualizar y si algo falla se revierte
            if not actualizar_asignacion(asignacion):
                raise ValueError("No se pudo actualizar la asignacion.")
            
        return True
    except (PeeweeException, ValueError):
        return False

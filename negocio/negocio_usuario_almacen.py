from peewee import PeeweeException
from datos.repositorios.repositorio_usuario_almacen import (
    listar_almacenes_de_usuario as listar_almacenes_de_usuario_repo,
    listar_usuarios_de_almacen as listar_usuarios_de_almacen_repo,
    existe_usuario_almacen,
    asignar_usuario,
    quitar_usuario_almacen as quitar_usuario_almacen_repo,
    cambiar_encargado as marcar_encargado_repo,
    quitar_marca_encargado
)
from datos.modelos.models import database
from datos.modelos.usuario import Usuario
from datos.modelos.almacen import Almacen


def listar_almacenes_de_usuario(usuario: Usuario):
    if usuario is None:
        return []
    return listar_almacenes_de_usuario_repo(usuario.id_usuario)

def listar_usuarios_de_almacen(almacen:Almacen):
    if almacen is None:
        return []
    return listar_usuarios_de_almacen_repo(almacen.id_almacen)


def asignar_usuario_almacen(usuario:Usuario, almacen:Almacen):
    if usuario is None or almacen is None:
        return False

    # validar que sean usuarios y almacenes activos
    if not usuario.estado or not almacen.estado:
        return False

    # Administrador no le asigna almacen, accede a todos gracias a su rol
    if usuario.id_rol.nombre == "Administrador":
        return False

    if existe_usuario_almacen(usuario.id_usuario, almacen.id_almacen):
        return False

    try:
        return asignar_usuario(usuario.id_usuario, almacen.id_almacen)
    except PeeweeException:
            return False
    
def quitar_usuario_almacen(usuario: Usuario, almacen: Almacen):
    if usuario is None or almacen is None:
        return False

    if not existe_usuario_almacen(usuario.id_usuario, almacen.id_almacen):
        return False

    try:
        return quitar_usuario_almacen_repo(usuario.id_usuario, almacen.id_almacen) > 0
    except PeeweeException:
        return False
    
def cambiar_encargado(usuario: Usuario, almacen: Almacen):
    if usuario is None or almacen is None:
        return False

    # Solo puede ser encargado alguien que ya esta asignado a ese almacen
    if not existe_usuario_almacen(usuario.id_usuario, almacen.id_almacen):
        return False

    try:
        with database.atomic() as transaccion:
            quitar_marca_encargado(almacen.id_almacen)

            if marcar_encargado_repo(usuario.id_usuario, almacen.id_almacen, True) != 1:
                transaccion.rollback()
                return False

        return True

    except PeeweeException:
        return False
from peewee import PeeweeException

from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol

from datos.repositorios.repositorio_rol import (
    listado_roles as listar_roles_repo,
    obtener_rol_por_id
)
from datos.repositorios.repositorio_usuario import (
    listar_usuarios,
    listar_usuarios_desactivados,
    obtener_usuario_por_id,
    guardar_usuario,
    existe_nombre_usuario
)

# En este archivo:
#   usuario = es el OBJETO Usuario
#   nombre_usuario = es el texto(VARCHAR(50) «Unique») con el que la persona inicia sesion (ej: "ale.g")


# ------------ Auxiliares ------------

def texto_o_none(texto):
    if texto is None:
        return None
    texto = texto.strip()
    return texto if texto else None

# ------------ Validaciones ------------
# La presentacion usa esta funcion para avisar antes de guardar.

def nombre_usuario_en_uso(nombre_usuario, id_usuario=None):
    return existe_nombre_usuario(nombre_usuario, id_usuario)


# Reglas comunes de registrar y actualizar. Devuelve True si se puede guardar.
def datos_usuario_validos(nombre, nombre_usuario, rol: Rol, id_usuario=None):
    if nombre is None or nombre_usuario is None:
        return False

    if rol is None:
        return False

    # Se excluye el propio id para que al actualizar pueda conservar su nombre de usuario
    if nombre_usuario_en_uso(nombre_usuario, id_usuario):
        return False

    return True

# ------------ Lectura ------------

def listar_usuarios_activos():
    return listar_usuarios()

def listar_usuarios_inactivos():
    return listar_usuarios_desactivados()

def obtener_usuario(id_usuario):
    return obtener_usuario_por_id(id_usuario)

def listar_roles():
    return listar_roles_repo()

def obtener_rol(id_rol):
    return obtener_rol_por_id(id_rol)

# ------------ Escritura ------------

def registrar_usuario(nombre, nombre_usuario, contrasena, rol: Rol):
    nombre = texto_o_none(nombre)
    nombre_usuario = texto_o_none(nombre_usuario)
    contrasena = texto_o_none(contrasena)

    # La contrasenia es NOT NULL en el DDL
    if contrasena is None:
        return False

    if not datos_usuario_validos(nombre, nombre_usuario, rol):
        return False

    nuevo_usuario = Usuario()
    nuevo_usuario.nombre = nombre
    nuevo_usuario.usuario = nombre_usuario
    # B4: aplicar hash aqui (por ahora se guarda tal cual)
    nuevo_usuario.contrasena = contrasena
    nuevo_usuario.id_rol = rol
    # En (estado y fecha_creacion) la BD les pone su valor por defecto

    try:
        return guardar_usuario(nuevo_usuario)
    except PeeweeException:
        return False


# La contrasenia no se cambia aqui: en B4 tendra su propio cambiar_contrasenia
def actualizar_usuario(usuario: Usuario, nombre, nombre_usuario, rol: Rol):
    if usuario is None:
        return False

    nombre = texto_o_none(nombre)
    nombre_usuario = texto_o_none(nombre_usuario)

    if not datos_usuario_validos(nombre, nombre_usuario, rol, usuario.id_usuario):
        return False

    usuario.nombre = nombre
    usuario.usuario = nombre_usuario
    usuario.id_rol = rol

    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False

# ------------ Borrado logico ------------

def desactivar_usuario(usuario: Usuario):
    if usuario is None:
        return False

    usuario.estado = False

    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False

def activar_usuario(usuario: Usuario):
    if usuario is None:
        return False

    usuario.estado = True

    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False

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
    obtener_usuario_por_nombre_usuario,
    guardar_usuario,
    existe_nombre_usuario
)
from auxiliares.seguridad import (
    generar_hash,
    verificar_contrasena,
    validar_contrasena
)

# En este archivo:
#   usuario = es el OBJETO Usuario
#   nombre_usuario = es el texto(VARCHAR(50) «Unique») con el que la persona inicia sesion (ej: "ale.g")


# ------------ Auxiliares ------------

# Ojo: no se usa con contraseñas, porque strip() les quitaria espacios
# y despues no coincidirian al iniciar sesion.
def texto_o_none(texto):
    if texto is None:
        return None
    texto = texto.strip()
    return texto if texto else None


# ------------ Validaciones ------------
# La presentacion usa estas funciones para avisar antes de guardar.

#verifica si el nombre de usuario ya esta en uso por otro usuario (excluyendo el propio id_usuario)
def nombre_usuario_en_uso(nombre_usuario, id_usuario=None):
    return existe_nombre_usuario(nombre_usuario, id_usuario)

# Devuelve una lista de errores si la contraseña no cumple las reglas de seguridad.
def errores_contrasena(contrasena):
    return validar_contrasena(contrasena)


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

# ------------ Autenticacion ------------

# Devuelve el objeto Usuario si el nombre de usuario y la contraseña son correctos
# y el usuario esta activo. En cualquier otro caso devuelve None.
def autenticar(nombre_usuario, contrasena):
    nombre_usuario = texto_o_none(nombre_usuario)

    if nombre_usuario is None or contrasena is None:
        return None

    usuario = obtener_usuario_por_nombre_usuario(nombre_usuario)

    if usuario is None:
        return None

    # Un usuario desactivado no puede iniciar sesion
    if not usuario.estado:
        return None

    if not verificar_contrasena(contrasena, usuario.contrasena):
        return None

    return usuario

# ------------ Escritura ------------

def registrar_usuario(nombre, nombre_usuario, contrasena, rol: Rol):
    nombre = texto_o_none(nombre)
    nombre_usuario = texto_o_none(nombre_usuario)

    # La contraseña es NOT NULL en el DDL y debe cumplir las reglas de seguridad.
    if validar_contrasena(contrasena):
        return False

    if not datos_usuario_validos(nombre, nombre_usuario, rol):
        return False

    nuevo_usuario = Usuario()
    nuevo_usuario.nombre = nombre
    nuevo_usuario.usuario = nombre_usuario
    # Se guarda el hash (sal$hash), nunca la contraseña legible
    nuevo_usuario.contrasena = generar_hash(contrasena)
    nuevo_usuario.id_rol = rol
    # En (estado y fecha_creacion) la BD les pone su valor por defecto

    try:
        return guardar_usuario(nuevo_usuario)
    except PeeweeException:
        return False


# La contraseña no se cambia aqui: tiene su propio cambiar_contrasena
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


# Unico lugar donde se cambia una contraseña.
# Pide la contraseña actual para confirmar que es la misma persona.
def cambiar_contrasena(usuario: Usuario, contrasena_actual, contrasena_nueva):
    if usuario is None:
        return False

    if not verificar_contrasena(contrasena_actual, usuario.contrasena):
        return False

    if validar_contrasena(contrasena_nueva):
        return False

    usuario.contrasena = generar_hash(contrasena_nueva)

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

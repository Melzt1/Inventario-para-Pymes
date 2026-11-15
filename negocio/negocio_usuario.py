from peewee import PeeweeException

from datos.modelos.models import database
from auxiliares.seguridad import generar_hash, verificar_contrasena
from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol
from datos.modelos.almacen import Almacen
from datos.repositorios.repositorio_usuario import (
    guardar_usuario,
    listar_usuarios,
    obtener_usuario_por_nombre,
    usuario_en_uso
)
from negocio.negocio_usuario_almacen import asignar_usuario
# ------------ Autenticacion ------------

def autenticar(username, contrasena):
    # Devuelve el objeto Usuario si el nombre de usuario existe
    usuario = obtener_usuario_por_nombre(username)

    if usuario is None or not usuario.estado:
        return None 

    # Verificamos que la contrasena del Usuario coincida con la contrasena ingresada
    if not verificar_contrasena(contrasena, usuario.contrasena):
        return None

    # si todo esta correcto retornamos el objeto (ira a la Clase "Sesion" para logear)
    return usuario


# ------------ Lectura ------------

def listar_usuarios_activos():
    return listar_usuarios()

def existe_nombre_usuario(username, id_usuario = None):
    return usuario_en_uso(username, id_usuario)

# ------------ Escritura ------------

def registrar_usuario(nombre, username, contrasena, rol: Rol, almacen: Almacen):

    if existe_nombre_usuario(username):
        return False

    contrasena_hash = generar_hash(contrasena)
    
    nuevo_usuario = Usuario()
    nuevo_usuario.nombre = nombre
    nuevo_usuario.usuario = username
    nuevo_usuario.contrasena = contrasena_hash
    nuevo_usuario.id_rol = rol.id_rol
    # FIX: Por defecto ya es True pero si no se define da error con asginar_usuario()
    nuevo_usuario.estado = True 

    try:
        with database.atomic():
            if not guardar_usuario(nuevo_usuario):
                raise ValueError ("No se pudo guardar el usuario.")
            if not asignar_usuario(nuevo_usuario, almacen):
                raise ValueError ("No se pudo asignar el almacen.")
            
        return True
    
    except (PeeweeException, ValueError):
        return False

def actualizar_usuario(usuario: Usuario, nombre, username, rol):
    if usuario is None:
        return False

    # Metodo que busca si el username existe para no replicarlo
    if existe_nombre_usuario(username, usuario.id_usuario):
        return False
    
    usuario.nombre = nombre
    usuario.usuario = username
    usuario.id_rol = rol.id_rol

    try:
        return guardar_usuario(usuario) 
    except PeeweeException:
        return False

# Segun el diagrama de clases cambiar la contrasena es un metodo aparte
def actualizar_contrasena(usuario: Usuario, nueva_contrasena):
    if usuario is None:
        return False

    usuario.contrasena = generar_hash(nueva_contrasena)
    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False


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

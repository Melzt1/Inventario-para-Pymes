from peewee import PeeweeException

from auxiliares.validaciones import validar_contrasena
from auxiliares.seguridad import generar_hash, verificar_contrasena
from datos.modelos.usuario import Usuario
from datos.modelos.rol import Rol
from datos.modelos.almacen import Almacen
from datos.repositorios.repositorio_rol import listado_roles
from datos.repositorios.repositorio_usuario import (
    guardar_usuario,
    listar_usuarios,
    listado_usuarios_inactivos,
    obtener_usuario_por_nombre,
    usuario_en_uso,
    hay_otro_administrador
)
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

def listar_usuarios_inactivos():
    return listado_usuarios_inactivos()

def listar_roles():
    return listado_roles()

def existe_nombre_usuario(username, id_usuario = None):
    return usuario_en_uso(username, id_usuario)

def existe_otro_administrador(id_usuario):
    return hay_otro_administrador(id_usuario)

# ------------ Escritura ------------

def registrar_usuario(nombre, nombre_usuario, contrasena, rol: Rol):
    if nombre is None or nombre_usuario is None or rol is None:
        return False

    if validar_contrasena(contrasena):
        return False

    if existe_nombre_usuario(nombre_usuario):
        return False

    nuevo_usuario = Usuario()
    nuevo_usuario.nombre = nombre
    nuevo_usuario.usuario = nombre_usuario
    nuevo_usuario.contrasena = generar_hash(contrasena)
    nuevo_usuario.id_rol = rol

    try:
        return guardar_usuario(nuevo_usuario)
    except PeeweeException:
        return False

def actualizar_usuario(usuario: Usuario, nombre, nombre_usuario, rol: Rol):
    if usuario is None or rol is None:
        return False

    if nombre is None or nombre_usuario is None or rol is None:
        return False    
    
    if existe_nombre_usuario(nombre_usuario, usuario.id_usuario):
        return False
    
    usuario.nombre = nombre
    usuario.usuario = nombre_usuario
    usuario.id_rol = rol.id_rol

    try:
        return guardar_usuario(usuario) 
    except PeeweeException:
        return False

# Segun el diagrama de clases cambiar la contrasena es un metodo aparte
def actualizar_contrasena(usuario: Usuario, nueva_contrasena):
    if usuario is None:
        return False

    if validar_contrasena(nueva_contrasena):
        return False
    
    usuario.contrasena = generar_hash(nueva_contrasena)
    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False


def desactivar_usuario(usuario: Usuario):
    if usuario is None:
        return False

    # Si es el ultimo administrador se cancela
    # Debe existir por lo menos 1 administrador para gestionar el sistema
    if usuario.id_rol.nombre == "Administrador":
        if not existe_otro_administrador(usuario.id_usuario):
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

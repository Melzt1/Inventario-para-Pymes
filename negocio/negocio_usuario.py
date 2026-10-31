from peewee import PeeweeException

from datos.modelos.usuario import Usuario
from datos.repositorios.repositorio_usuario import (
    guardar_usuario,
    listar_usuarios,
    obtener_usuario_por_nombre
)

# ------------ Autenticacion ------------

""" FALTAN METODOS PARA HASHEAR Y VALIDAR CONTRASENA """

def validar_contrasena(contrasena):
    pass

def autenticar(nombre_usuario, contrasena):
    # Devuelve el objeto Usuario si el nombre de usuario existe
    usuario = obtener_usuario_por_nombre(nombre_usuario)

    if usuario is None:
        return False

    # Verificamos que la contrasena del Usuario coincida con la contrasena ingresada
    if not validar_contrasena(contrasena):
        return False

    # si todo esta correcto retornamos el objeto (ira a la Clase "Sesion" para logear)
    return usuario


# ------------ Lectura ------------

def listar_usuarios_activos():
    return listar_usuarios()

# ------------ Escritura ------------

def registrar_usuario(nombre, usuario, contrasena, id_rol, id_almacen):
    nuevo_usuario = Usuario()
    nuevo_usuario.nombre = nombre
    nuevo_usuario.usuario = usuario
    nuevo_usuario.contrasena = contrasena
    nuevo_usuario.id_rol = id_rol
    nuevo_usuario.id_almacen = id_almacen

    try:
        return guardar_usuario(nuevo_usuario)
    except PeeweeException:
        return False

def actualizar_usuario():
    pass      

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


def cambiar_contrasena(usuario: Usuario, nueva_contrasena):
    if usuario is None:
        return False
        
    usuario.contrasena = nueva_contrasena

    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False  

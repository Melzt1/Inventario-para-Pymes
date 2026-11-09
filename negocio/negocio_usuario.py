from peewee import PeeweeException
from datos.modelos.models import database
from datos.modelos.usuario import Usuario
from datos.repositorios.repositorio_usuario import (
    guardar_usuario,
    listar_usuarios,
    obtener_usuario_por_nombre
)

# ------------ Autenticacion ------------

""" FALTAN METODOS PARA HASHEAR CONTRASENA """

def autenticar(nombre_usuario, contrasena):
    # Devuelve el objeto Usuario si el nombre de usuario existe
    usuario = obtener_usuario_por_nombre(nombre_usuario)

    if usuario is None:
        return None 

    # Verificamos que la contrasena del Usuario coincida con la contrasena ingresada
    if contrasena != usuario.contrasena:
        return None

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

def actualizar_usuario(usuario:Usuario, nombre, username):
    if usuario is None:
        return False

    # Metodo que busca si el username existe
    """Nota para Ale: 
    Verifica si el nombre de usuario ya existe usa la misma logica que aplicamos en existe_sku().

    Segun el asistente no es necesario el atomic() pq se utiliza 
    cuando hay dos o mas operaciones de escritura que deben ser todo-o-nada
    Por ejemplo en Almacen, estamos creando un objeto Almacen, un objeto Direccion y 
    un objeto Seccion al mismo tiempo, entonces el atomic() actua cuando 1 de las 3 falla y
    revierte los cambios, en este caso solo estamos creando UN solo objeto por lo que no es necesario."""

    if existe_usuario(username, usuario.id_usuario):
        return False
    
    usuario.nombre = nombre
    usuario.usuario = username
    try:
        return guardar_usuario(usuario)
        
    except PeeweeException:
        return False

# Segun el diagrama de clases cambiar la contrasena es un metodo aparte
def actualizar_contrasena(usuario:Usuario, nueva_contrasena):
    if usuario is None:
        return False

    # FALTA METODO PARA VALIDAR Y HASHEAR CONTRASENA
    usuario.contrasena = nueva_contrasena
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

def cambiar_contrasena(usuario: Usuario, nueva_contrasena):
    if usuario is None:
        return False
        
    usuario.contrasena = nueva_contrasena

    try:
        return guardar_usuario(usuario)
    except PeeweeException:
        return False  

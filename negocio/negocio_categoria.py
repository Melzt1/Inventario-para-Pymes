from peewee import PeeweeException

from datos.modelos.categoria import Categoria
from datos.repositorios.repositorio_categoria import (
    listar_categoria, 
    guardar_categoria, 
    obtener_categoria_por_id,
    listar_categoria_desactivada
)

# ------------ Lectura ------------

def listar_categorias_activas():
    return listar_categoria()

def listar_categorias_desactivadas():
    return listar_categoria_desactivada()

def obtener_categoria(id_categoria):
    return obtener_categoria_por_id(id_categoria)

# ------------ Escritura ------------

def crear_categoria(nombre, descripcion):        
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    
    try:
        return guardar_categoria(nueva_categoria)
    except PeeweeException:
        return False

def actualizar_categoria(categoria: Categoria, nombre, descripcion):

    # Si no existe, no se actualiza
    if categoria is None:
        return False

    categoria.nombre = nombre
    categoria.descripcion = descripcion

    try:
        return guardar_categoria(categoria)
    except PeeweeException:
        return False

# ------------ Borrado logico ------------

def desactivar_categoria(categoria: Categoria):
    if categoria is None:
        return False

    categoria.estado = False

    try:
        return guardar_categoria(categoria)
    except PeeweeException:
        return False

# Metodo para activar Categoria
def activar_categoria(categoria: Categoria):
    if categoria is None:
        return False

    categoria.estado = True

    try:
        return guardar_categoria(categoria)
    except PeeweeException:
        return False
from datos.modelos.categoria import Categoria
from datos.repositorios.repositorio_categoria import (
    listar_categoria, 
    guardar_categoria, 
    obtener_categoria_por_id
)

# ------------ Lectura ------------

def listar_categorias_activas():
    return listar_categoria()

def obtener_categoria(id_categoria):
    return obtener_categoria_por_id(id_categoria)

# ------------ Escritura ------------

def crear_categoria(nombre, descripcion):        
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    return guardar_categoria(nueva_categoria)

def actualizar_categoria(id_categoria, nombre, descripcion):
    categoria = obtener_categoria(id_categoria)

    # Si no existe, no se actualiza
    if categoria is None:
        return False

    categoria.nombre = nombre
    categoria.descripcion = descripcion
    return guardar_categoria(categoria)

# ------------ Borrado logico ------------

def desactivar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    categoria.estado = False
    return guardar_categoria(categoria)

# Metodo para activar Categoria
def activar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    categoria.estado = True
    return guardar_categoria(categoria)
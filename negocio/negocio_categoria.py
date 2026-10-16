from datos.repositorios.repositorio_categoria import listado_categorias, guardar_categorias, obtener_categoria_por_id
from datos.modelos.categoria import Categoria

# Metodo READ
def lista_categorias():
    return listado_categorias()

def crear_categoria(nombre, descripcion):        
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    return guardar_categorias(nueva_categoria)
                    
# Metodo para validar el id
def obtener_categoria(id_categoria):
    return obtener_categoria_por_id(id_categoria)

# Metodo para Actualizar Categoria
def actualizar_categoria(id_categoria, nombre, descripcion):
    categoria = obtener_categoria(id_categoria)

    # si obtener_categoria devuelve None, no permitir asginar nombre y desc
    if categoria is None:
        return False

    categoria.nombre = nombre
    categoria.descripcion = descripcion
    return guardar_categorias(categoria)

# Metodo para Eliminar Categoria (borrado logico)
def desactivar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    # estado es un booleano, solo necesito cambiarlo a False para desactivarlo
    categoria.estado = False
    return guardar_categorias(categoria)

# Metodo para activar Categoria
def activar_categoria(id_categoria):
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        return False

    categoria.estado = True
    return guardar_categorias(categoria)
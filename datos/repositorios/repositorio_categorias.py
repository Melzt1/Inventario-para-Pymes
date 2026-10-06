from datos.modelos.categoria import Categoria

def listado_categorias():
    categorias = Categoria.select()
    if categorias:
        return categorias
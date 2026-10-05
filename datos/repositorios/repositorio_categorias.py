from datos.modelos.categoria import Categorias

def listado_categorias():
    categorias = Categorias.select()
    if categorias:
        return categorias
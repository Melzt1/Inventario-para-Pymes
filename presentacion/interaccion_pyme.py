from datos.repositorios.repositorio_categorias import listado_categorias
from prettytable import PrettyTable


def lista_categorias():
    tabla_categorias = PrettyTable()
    tabla_categorias.field_names = ['Id', 'Nombre', 'Descripcion']
    
    categorias = listado_categorias()
    if categorias:
        for categoria in categorias:
            tabla_categorias.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
        print(tabla_categorias)
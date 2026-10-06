from datos.repositorios.repositorio_categorias import listado_categorias, guardar_categorias
from prettytable import PrettyTable
from datos.modelos.categoria import Categoria


def lista_categorias():
    tabla_categorias = PrettyTable()
    tabla_categorias.field_names = ['Id', 'Nombre', 'Descripcion']
    
    categorias = listado_categorias()
    if categorias:
        for categoria in categorias:
            tabla_categorias.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
        print(tabla_categorias)

def crear_categoria(nombre, descripcion):        
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    guardar_categorias(nueva_categoria)

def actualizar_categoria(nombre, descripcion):
    pass
from datos.repositorios.repositorio_categorias import listado_categorias, guardar_categorias
from prettytable import PrettyTable
from datos.modelos.categoria import Categoria


def lista_categorias():
    tabla_categorias = PrettyTable()
    tabla_categorias.field_names = ['Id', 'Nombre', 'Descripcion']
    
    categorias = listado_categorias()

    if not categorias:
        print("No hay categorías registradas.")
        return
    
    for categoria in categorias:
        tabla_categorias.add_row([categoria.id_categoria, categoria.nombre, categoria.descripcion])
    print(tabla_categorias)

def crear_categoria(nombre, descripcion):        
    nueva_categoria = Categoria()
    nueva_categoria.nombre = nombre
    nueva_categoria.descripcion = descripcion
    guardar_categorias(nueva_categoria)
                    

# Metodo para Obtener el id de la categoria para actualizar
def obtener_categoria(id_categoria):
    try: 
        #return Categoria.get_by_id(id_categoria)
        return Categoria[id_categoria]
    except Categoria.DoesNotExist:
        return None

# Metodo para Actualizar Categoria
def actualizar_categoria(id_categoria, nombre, descripcion):
    categoria = obtener_categoria(id_categoria)

    # si obtener_categoria devuelve None, no permitir asginar nombre y desc
    if categoria is None:
        return False

    categoria.nombre = nombre
    categoria.descripcion = descripcion
    return guardar_categorias(categoria)      
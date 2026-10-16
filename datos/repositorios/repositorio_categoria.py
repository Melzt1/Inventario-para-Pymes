from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_categorias():
    return Categoria.select().where(Categoria.estado == True) #para ocultar las de borrado logico

def guardar_categorias(categoria:Categoria):
    try:
        categoria.save()
        return True

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
        
    return False
  
# get_or_none me ahorra el try except DoesNotExist y si no encuentra el ID retorna None (es un todo en uno)             
def obtener_categoria_por_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)
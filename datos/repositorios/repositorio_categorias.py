from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_categorias():
    return Categoria.select().where(Categoria.estado == True) #para ocultar las de borrado logico

def guardar_categorias(categoria:Categoria):
    try:
        return categoria.save()

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
        
    return False
             
def obtener_categoria_por_id(id_categoria):
    try: 
        # lo mismo que: return Categoria.get_by_id(id_categoria)
        return Categoria[id_categoria]
    except Categoria.DoesNotExist:
        return None
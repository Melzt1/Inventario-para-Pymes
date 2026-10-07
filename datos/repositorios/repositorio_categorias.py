from datos.modelos.categoria import Categoria
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_categorias():
    categorias = Categoria.select()
    if categorias:
        return categorias

def guardar_categorias(categoria:Categoria):
    try:
        guardar = categoria.save()
        print(guardar)
    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
    finally:
        print("Proceso finalizado.")

             

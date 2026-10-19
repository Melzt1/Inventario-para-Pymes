from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.categoria import Categoria

# ------------ Lectura ------------

def listar_categoria():
    return Categoria.select().where(Categoria.estado == True)

def obtener_categoria_por_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)

# ------------ Escritura ------------

def guardar_categoria(categoria:Categoria):
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

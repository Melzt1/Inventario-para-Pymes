from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.almacen import Almacen

# ------------ Lectura ------------

def listar_almacenes():
    return Almacen.select().where(Almacen.estado == True) 

def listar_almacenes_desactivados_repo():
    return Almacen.select().where(Almacen.estado == False) 

# get_or_none me ahorra el try except DoesNotExist y si no encuentra el ID retorna None (es un todo en uno)
def obtener_almacen_por_id(id_almacen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almacen)

# ------------ Escritura ------------

# .save() sirve para CREATE y UPDATE 
def guardar_almacen(almacen:Almacen):
    try:
        almacen.save()
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

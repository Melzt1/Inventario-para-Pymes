from datos.modelos.inventario import Inventario
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def guardar_inventario(inventario:Inventario):
    try:
        inventario.save()
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


# buscar un producto en un almacen especifico
def obtener_inventario(id_producto, id_almacen):
    return Inventario.get_or_none(
        (Inventario.id_producto == id_producto) &
        (Inventario.id_almacen == id_almacen)
    )

# listar el inventario de un almacen especifico
def lista_inventario_almacen(id_almacen):
    return Inventario.select().where(Inventario.id_almacen == id_almacen)    

# listar productos bajo stock critico
def lista_stock_critico():
    return Inventario.select().where(Inventario.stock_actual <= Inventario.stock_minimo)
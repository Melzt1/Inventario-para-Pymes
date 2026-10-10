from datos.modelos.producto import Producto
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_productos():
    return Producto.select().where(Producto.estado == True) #para ocultar las de borrado logico


def guardar_productos(prodcuto:Producto):
    try:
        return prodcuto.save()

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False

def obtener_producto_por_id(id_producto):
    try:
        return Producto[id_producto]
    except Producto.DoesNotExist:
        return None

def existe_sku(sku):
    return Producto.select().where(Producto.sku == sku).exists()    
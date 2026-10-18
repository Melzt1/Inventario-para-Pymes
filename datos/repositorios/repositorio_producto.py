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

# get_or_none me ahorra el try except DoesNotExist y si no encuentra el ID retorna None (es un todo en uno)     
def obtener_producto_por_id(id_producto):
    return Producto.get_or_none(Producto.id_producto == id_producto)

# Granito de arena by CHATGPT (La clave para al momento de hacer un update mantener el sku(unique))
# La consulta pregunta si otro producto tiene ese SKU, excluyendo el ID del producto actual.
def existe_sku(sku, id_producto = None):
    consulta = Producto.select().where(Producto.sku == sku)

    if id_producto is not None:
        consulta = consulta.where(Producto.id_producto != id_producto)

    return consulta.exists()    

def obtener_producto_por_sku(sku):
    return Producto.get_or_none(Producto.sku == sku)

def obtener_nombre_productos(nombre):
    return Producto.select().where(Producto.nombre.contains(nombre))

def obtener_nombre_productos_desactivados():
    return Producto.select().where(Producto.estado == False)
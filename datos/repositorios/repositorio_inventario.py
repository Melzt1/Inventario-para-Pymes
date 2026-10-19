from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.inventario import Inventario
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

# ------------ Lectura ------------

# obtiene el inventario de un almacen con los datos de sus productos
def listar_inventario_de_almacen(id_almacen):       
    return (Inventario
            .select(Inventario, Producto)
            .join(Producto)
            .where(Inventario.id_almacen == id_almacen)
            .order_by(Producto.nombre))  

# obtiene el inventario de un producto con el almacen ya cargado
def listar_inventario_de_producto(id_producto):
    return (Inventario
            .select(Inventario, Almacen)
            .join(Almacen)
            .where(Inventario.id_producto == id_producto)
            .order_by(Almacen.nombre))

def listar_inventario_stock_critico():
    return (Inventario.select()
            .where(Inventario.stock_actual <= Inventario.stock_minimo))

def obtener_inventario_por_id(id_inventario):
    return Inventario.get_or_none(Inventario.id_inventario == id_inventario)

# buscar un producto en un almacen especifico
def obtener_inventario(id_producto, id_almacen):
    return Inventario.get_or_none(
        (Inventario.id_producto == id_producto) &
        (Inventario.id_almacen == id_almacen))


# ------------ Escritura ------------

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











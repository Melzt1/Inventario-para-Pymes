from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.minimo_almacen import MinimoAlmacen
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

# ------------ Lectura ------------

def obtener_stock_minimo(id_producto, id_almacen):
    return MinimoAlmacen.get_or_none(
        (MinimoAlmacen.id_producto == id_producto) &
        (MinimoAlmacen.id_almacen == id_almacen)
    )

def listar_minimo_almacen(id_almacen):
    return MinimoAlmacen.select().where(MinimoAlmacen.id_almacen == id_almacen)

# ------------ Escritura ------------

def crear_minimo(producto: Producto, almacen: Almacen, stock_minimo):
    try:
        MinimoAlmacen.create(
            id_producto = producto.id_producto,
            id_almacen = almacen.id_almacen,
            stock_minimo = stock_minimo,
        )
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

def guardar_minimo(minimo: MinimoAlmacen):
    try:
        minimo.save()
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
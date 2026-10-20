from peewee import IntegrityError, PeeweeException, OperationalError, DataError

from datos.modelos.producto_proveedor import ProductoProveedor
from datos.modelos.proveedor import Proveedor

# ------------ Lectura ------------

# obtiene todas las relaciones producto-proveedor
def listar_relaciones():
    return ProductoProveedor.select()

# obtiene las relaciones de un producto con el proveedor
def listar_relaciones_de_producto_repo(id_producto):
    return (ProductoProveedor
            .select(ProductoProveedor, Proveedor)
            .join(Proveedor)
            .where(ProductoProveedor.id_producto == id_producto)
            .order_by(Proveedor.nombre))

# Proveedores ACTIVOS que aun no estan asociados a ese producto.
# CONSULTA GENERADA POR DEEPSEEK (IA). YO NO PUDE RESOLVERLA :C
def listado_proveedores_disponibles(id_producto):
    ids_asociados = (ProductoProveedor
                     .select(ProductoProveedor.id_proveedor)
                     .where(ProductoProveedor.id_producto == id_producto))

    return (Proveedor
            .select()
            .where((Proveedor.estado == True) &
                   (~Proveedor.id_proveedor.in_(ids_asociados)))
            .order_by(Proveedor.nombre))    

def obtener_relacion(id_producto, id_proveedor):
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto) &
        (ProductoProveedor.id_proveedor == id_proveedor)
    )

# obtiene la relacion principal o None si el producto no tiene
def obtener_relacion_principal(id_producto):
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto) &
        (ProductoProveedor.es_principal == True)
    )

# ------------ Escritura ------------

def crear_relacion(id_producto, id_proveedor, es_principal=False):
    try:
        ProductoProveedor.create(
            id_producto=id_producto,
            id_proveedor=id_proveedor,
            es_principal=es_principal,
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

# borrado fisico para eliminar la relacion de proveedor principal y asignar otra
def quitar_relacion(relacion):
    try:
        return relacion.delete_instance() 
    
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False  
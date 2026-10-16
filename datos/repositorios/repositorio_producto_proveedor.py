from datos.modelos.producto_proveedor import ProductoProveedor
from datos.modelos.proveedor import Proveedor
from peewee import IntegrityError, PeeweeException

# Lista para devolver todas las relaciones producto-proveedor
def listado_proveedores_asociados():
    return ProductoProveedor.select()

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
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
    return False


def obtener_relacion(id_producto, id_proveedor):
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto) &
        (ProductoProveedor.id_proveedor == id_proveedor)
    )

# buscar entre todos los proveedores cual es el principal
def obtener_proveedor_principal(id_producto):
    return ProductoProveedor.get_or_none(
        (ProductoProveedor.id_producto == id_producto) &
        (ProductoProveedor.es_principal == True)
    )

# busca todos los proveedores asociados a 1 producto en especifico
def listado_proveedores_producto(id_producto):
    return (ProductoProveedor
                .select(ProductoProveedor, Proveedor)
                .join(Proveedor)
                .where(ProductoProveedor.id_producto == id_producto))
    

# borrado fisico para eliminar la relacion de proveedor principal y asignar otra
def quitar_relacion(relacion):
    try:
        return relacion.delete_instance() 
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
    return False  
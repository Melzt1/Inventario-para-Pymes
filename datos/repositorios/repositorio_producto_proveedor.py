from datos.modelos.producto_proveedor import ProductoProveedor
from peewee import IntegrityError, PeeweeException


def crear_relacion(id_producto, id_proveedor, es_principal=False):
    try:
        return ProductoProveedor.create(
            id_producto=id_producto,
            id_proveedor=id_proveedor,
            es_principal=es_principal,
        )
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

def quitar_relacion(relacion):
    return relacion.delete_instance()   
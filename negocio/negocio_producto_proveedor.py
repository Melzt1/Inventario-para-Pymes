from datos.repositorios.repositorio_producto_proveedor import crear_relacion, obtener_relacion, quitar_relacion

from negocio.negocio_producto import obtener_producto
from negocio.negocio_proveedor import obtener_proveedor


def asignar_proveedor_principal(id_producto, id_proveedor):
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    return crear_relacion(id_producto, id_proveedor, es_principal=True)

def asignar_proveedor_secundario(id_producto, id_proveedor):
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    return crear_relacion(id_producto, id_proveedor, es_principal=False)

def eliminar_relacion(id_producto, id_proveedor):
    relacion = obtener_relacion(id_producto, id_proveedor)

    if relacion is None:
        return False

    return quitar_relacion(relacion)
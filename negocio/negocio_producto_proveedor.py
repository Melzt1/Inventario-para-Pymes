from datos.repositorios.repositorio_producto_proveedor import crear_relacion, obtener_relacion, quitar_relacion, listado_proveedores_asociados, obtener_proveedor_principal, listado_proveedores_producto, listado_proveedores_disponibles
from negocio.negocio_producto import obtener_producto
from negocio.negocio_proveedor import obtener_proveedor

def lista_proveedores_asociados():
    return listado_proveedores_asociados()

def lista_proveedores_de_producto(id_producto):
    return listado_proveedores_producto(id_producto)

def proveedor_principal_de_producto(id_producto):
    return obtener_proveedor_principal(id_producto)

def lista_proveedores_disponibles(id_producto):
    return listado_proveedores_disponibles(id_producto)

# Metodo Create
"""             regla de negocio:
el producto solo puede tener 1 proveedor principal, y no
se reemplaza si ya existe uno, hay que quitar esa relacion primero."""

def asignar_proveedor_principal(id_producto, id_proveedor):
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    if obtener_proveedor_principal(id_producto) is not None:
        return False

    return (crear_relacion(id_producto, id_proveedor, es_principal=True))    

def asignar_proveedor_secundario(id_producto, id_proveedor):
    producto = obtener_producto(id_producto)
    proveedor = obtener_proveedor(id_proveedor)

    if producto is None or proveedor is None:
        return False

    relacion = obtener_relacion(id_producto, id_proveedor)
    # Si ya esta asociado no se puede volver a asociar
    if relacion is not None:
        return False
    
    return crear_relacion(id_producto, id_proveedor, es_principal=False)

def eliminar_relacion(id_producto, id_proveedor):
    relacion = obtener_relacion(id_producto, id_proveedor)

    if relacion is None:
        return False

    return quitar_relacion(relacion)
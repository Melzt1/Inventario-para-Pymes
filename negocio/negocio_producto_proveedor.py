from datos.repositorios.repositorio_producto_proveedor import (
    crear_relacion, 
    obtener_relacion, 
    quitar_relacion, 
    listar_relaciones, 
    obtener_relacion_principal, 
    listar_relaciones_de_producto, 
    listado_proveedores_disponibles
)
from negocio.negocio_producto import obtener_producto
from negocio.negocio_proveedor import obtener_proveedor

# ------------ Lectura ------------

def listar_todas_las_relaciones():
    return listar_relaciones()

def listar_relaciones_de_producto(id_producto):
    return listar_relaciones_de_producto(id_producto)

# Proveedores activos que aun no estan asociados al producto
def listar_proveedores_disponibles(id_producto):
    return listado_proveedores_disponibles(id_producto)

def obtener_proveedor_principal(id_producto):
    return obtener_relacion_principal(id_producto)


# ------------ Escritura ------------

"""             regla de negocio:
el producto solo puede tener 1 proveedor principal, y no
se reemplaza si ya existe uno, hay que quitar esa relacion primero."""

def asignar_proveedor_principal(id_producto, id_proveedor):
    if obtener_producto(id_producto) is None:
        return False

    if obtener_proveedor(id_proveedor) is None:
        return False

    if obtener_relacion_principal(id_producto) is not None:
        return False

    return crear_relacion(id_producto, id_proveedor, es_principal=True)   

def asignar_proveedor_secundario(id_producto, id_proveedor):
    if obtener_producto(id_producto) is None:
        return False

    if obtener_proveedor(id_proveedor) is None:
        return False

    # Si ya esta asociado no se puede volver a asociar
    if obtener_relacion(id_producto, id_proveedor) is not None:
        return False
    
    return crear_relacion(id_producto, id_proveedor, es_principal=False)

def quitar_proveedor_de_producto(id_producto, id_proveedor):
    relacion = obtener_relacion(id_producto, id_proveedor)

    if relacion is None:
        return False

    return quitar_relacion(relacion)
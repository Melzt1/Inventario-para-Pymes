from peewee import PeeweeException

from datos.repositorios.repositorio_producto_proveedor import (
    crear_relacion, 
    obtener_relacion, 
    quitar_relacion, 
    listar_relaciones, 
    obtener_relacion_principal, 
    listar_relaciones_de_producto_repo, 
    listado_proveedores_disponibles
)
from datos.modelos.producto import Producto
from datos.modelos.proveedor import Proveedor

# ------------ Lectura ------------

def listar_todas_las_relaciones():
    return listar_relaciones()

def listar_relaciones_de_producto(id_producto):
    return listar_relaciones_de_producto_repo(id_producto)

# Proveedores activos que aun no estan asociados al producto
def listar_proveedores_disponibles(id_producto):
    return listado_proveedores_disponibles(id_producto)

def obtener_proveedor_principal(id_producto):
    return obtener_relacion_principal(id_producto)


# ------------ Escritura ------------

"""             regla de negocio:
el producto solo puede tener 1 proveedor principal, y no
se reemplaza si ya existe uno, hay que quitar esa relacion primero."""

def asignar_proveedor_principal(producto: Producto, proveedor: Proveedor):
    if producto is None:
        return False

    if proveedor is None:
        return False

    if obtener_relacion_principal(producto.id_producto) is not None:
        return False

    try:
        return crear_relacion(producto.id_producto, producto.id_proveedor, es_principal=True)
    except PeeweeException:
        return False   

def asignar_proveedor_secundario(producto: Producto, proveedor: Proveedor):
    if producto is None:
        return False

    if proveedor is None:
        return False

    # Si ya esta asociado no se puede volver a asociar
    if obtener_relacion(producto.id_producto, proveedor.id_proveedor) is not None:
        return False
    
    try:
        return crear_relacion(producto.id_producto, proveedor.id_proveedor, es_principal=False)
    except PeeweeException:
        return False

def quitar_proveedor_de_producto(producto: Producto, proveedor: Proveedor):
    if producto is None:
        return False

    if proveedor is None:
        return False
    
    relacion = obtener_relacion(producto.id_producto, proveedor.id_proveedor)

    if relacion is None:
        return False

    try:
        return quitar_relacion(relacion)
    except PeeweeException:
        return False
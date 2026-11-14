from peewee import PeeweeException

from datos.modelos.models import database
from datos.repositorios.repositorio_producto_proveedor import (
    crear_relacion, 
    obtener_relacion, 
    quitar_relacion, 
    listar_relaciones, 
    obtener_relacion_principal, 
    listar_relaciones_de_producto_repo, 
    listado_proveedores_disponibles,
    quitar_relaciuon_principal,
    asignar_como_principal,
    listado_proveedores_para_principal
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

# Todos los proveedores excepto el que ya es principal
def listar_proveedores_para_principal(id_producto):
    return listado_proveedores_para_principal(id_producto)
    
def obtener_proveedor_principal(id_producto):
    return obtener_relacion_principal(id_producto)


# ------------ Escritura ------------

""" Finalmente solucionado: Ahoora al asignar un proveedor principal 
se reemplaza el anterior y se evita el tener que eliminar la relacion,
todo gracias al bendito atomic() """

def asignar_proveedor_principal(producto: Producto, proveedor: Proveedor):
    if producto is None or proveedor is None:
        return False

    # Validamos que el producto y el proveedor no esten desactivados
    if not producto.estado or not proveedor.estado:
        return False

    try:
        with database.atomic():
            # Primero desmarcar al proveedor principala anterior
            quitar_relaciuon_principal(producto.id_producto)

            # Segundo: comprobar si el nuevo proveedor ya esta relacionado
            relacion = obtener_relacion(producto.id_producto, proveedor.id_proveedor)

            # Tecero: si no existe la relacion, la creamos
            if relacion is None:
                if not crear_relacion(producto.id_producto, proveedor.id_proveedor, es_principal=True):
                    raise ValueError("No se pudo crear la relación")
            # Cuarto: en caso de existir la relacion (proveedor secundario) pasa a ser principal              
            else:
                if not(asignar_como_principal(producto.id_producto, proveedor.id_proveedor)):
                    raise ValueError("No se pudo asignar como principal")
                                
        return True
    
    except (PeeweeException, ValueError):
        return False            

def asignar_proveedor_secundario(producto: Producto, proveedor: Proveedor):
    if producto is None or proveedor is None:
        return False

    if not producto.estado or not proveedor.estado:
        return False

    # Si ya esta asociado no se puede volver a asociar
    if obtener_relacion(producto.id_producto, proveedor.id_proveedor) is not None:
        return False
    
    try:
        return crear_relacion(producto.id_producto, proveedor.id_proveedor, es_principal=False)
    except PeeweeException:
        return False

def quitar_proveedor_de_producto(producto: Producto, proveedor: Proveedor):
    if producto is None or proveedor is None:
        return False
    
    relacion = obtener_relacion(producto.id_producto, proveedor.id_proveedor)

    if relacion is None:
        return False

    try:
        return quitar_relacion(relacion)
    except PeeweeException:
        return False
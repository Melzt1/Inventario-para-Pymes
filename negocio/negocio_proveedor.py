from peewee import PeeweeException

from datos.modelos.models import database
from datos.modelos.proveedor import Proveedor
from datos.repositorios.repositorio_direccion import guardar_direccion
from datos.repositorios.repositorio_proveedor import (
    listar_proveedores, 
    guardar_proveedor, 
    obtener_proveedor_por_id, 
    existe_correo, existe_telefono, 
    existe_rut, 
    buscar_proveedores_por_nombre,
    listar_proveedores_desactivados_repo
)
from negocio.negocio_direccion import crear_direccion, actualizar_direccion
from auxiliares.validaciones import validar_rut

# ------------ Validaciones ------------

def rut_en_uso(rut):
    return existe_rut(rut)

def correo_en_uso(correo, id_proveedor=None):
    return existe_correo(correo, id_proveedor)

def telefono_en_uso(telefono, id_proveedor=None):
    return existe_telefono(telefono, id_proveedor)

# ------------ Lectura ------------

def listar_proveedores_activos():
    return listar_proveedores()

def listar_proveedores_desactivados():
    return listar_proveedores_desactivados_repo()

def buscar_proveedores(nombre):
    return buscar_proveedores_por_nombre(nombre)

def obtener_proveedor(id_almacen):
    return obtener_proveedor_por_id(id_almacen)

# ------------ Escritura ------------

def registrar_proveedor(rut, nombre, correo, telefono, calle, numero, comuna, ciudad):
    if not validar_rut(rut):
        return False

    if rut_en_uso(rut):
        return False

    if correo_en_uso(correo):
        return False

    if telefono_en_uso(telefono):
        return False
    
    nuevo_proveedor = Proveedor()
    nuevo_proveedor.rut = rut
    nuevo_proveedor.nombre = nombre
    nuevo_proveedor.correo = correo
    nuevo_proveedor.telefono = telefono

    # Asociar direccion (relacion entre entidades)
    try:
        # atomic: si falla el proveedor, se revierte la direccion, asi no queda huerfana
        with database.atomic():
            nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)
            guardar_direccion(nueva_direccion)

            # nueva_direccion es el objeto Direccion y contiene id_direccion
            nuevo_proveedor.id_direccion = nueva_direccion
            guardar_proveedor(nuevo_proveedor)

        return True

    except PeeweeException:
        return False


def actualizar_proveedor(proveedor: Proveedor, correo, telefono):   
    if proveedor is None:
        return False

    # Excluimos este proveedor para que pueda conservar su correo actual.
    if correo_en_uso(correo, proveedor.id_proveedor):
        return False

    # Excluimos este proveedor para que pueda conservar su telefono actual.
    if telefono_en_uso(telefono, proveedor.id_proveedor):
        return False
    
    proveedor.correo = correo
    proveedor.telefono = telefono

    try:
        return guardar_proveedor(proveedor)
    except PeeweeException:
        return False  

def actualizar_direccion_proveedor(proveedor: Proveedor, calle, numero, comuna, ciudad):
    if proveedor is None:
        return False

    # La relacion (clave foranea) hace que proveedor.id_direccion entregue el objeto Direccion
    direccion = proveedor.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)

# ------------ Borrado logico ------------

def desactivar_proveedor(proveedor: Proveedor):
    if proveedor is None:
        return False

    proveedor.estado = False

    try:
        return guardar_proveedor(proveedor)
    except PeeweeException:
        return False

def activar_proveedor(proveedor: Proveedor):
    if proveedor is None:
        return False

    proveedor.estado = True

    try:
        return guardar_proveedor(proveedor)
    except PeeweeException:
        return False


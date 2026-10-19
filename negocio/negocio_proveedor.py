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
    buscar_proveedores_por_nombre)
from negocio.negocio_direccion import crear_direccion, actualizar_direccion

# ------------ Validaciones ------------

def validar_rut(rut):
    # Limpiar los caracteres del rut (puntos y guion) 
    rut_limpio = rut.replace(".", "").replace("-","").upper()

    # Debe existir al menos un digito y un digito verificador.
    if len(rut_limpio) < 2:
        return False
    
    # obtener todos los digitos menos el DV
    rut_sin_dv = rut_limpio[:-1] 
    dv_original = rut_limpio[-1]

    # validar que sean digitos
    if not rut_sin_dv.isdigit() or dv_original not in "0123456789K":
        return False

    multiplicador = 2
    suma = 0

    # reversed para invertir los digitos del rut
    for digito in reversed(rut_sin_dv):
        resultado = int(digito) * multiplicador # Hacemos un cast para poder multiplicar
        suma += resultado

        # Aumentamos 1 por cada iteracion hasta 7 y luego lo reseteamos
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # calcular el digito verificador
    dv_calculado = 11 - (suma % 11)

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado  == 10:
        dv_calculado = "K" 
    else:
        dv_calculado = str(dv_calculado )  

    # Comprobar si coincide con el digito verificador orignal
    return dv_original == dv_calculado

def rut_en_uso(rut):
    return existe_rut(rut)

def correo_en_uso(correo, id_proveedor=None):
    return existe_correo(correo, id_proveedor)

def telefono_en_uso(telefono, id_proveedor=None):
    return existe_telefono(telefono, id_proveedor)

# ------------ Lectura ------------

def listar_proveedores_activos():
    return listar_proveedores()

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


def actualizar_proveedor(id_proveedor, correo, telefono):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    # Excluimos este proveedor para que pueda conservar su correo actual.
    if correo_en_uso(correo, id_proveedor):
        return False

    # Excluimos este proveedor para que pueda conservar su telefono actual.
    if telefono_en_uso(telefono, id_proveedor):
        return False
    
    proveedor.correo = correo
    proveedor.telefono = telefono
    return guardar_proveedor(proveedor)    

def actualizar_direccion_proveedor(id_proveedor, calle, numero, comuna, ciudad):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    # La relacion (clave foranea) hace que proveedor.id_direccion entregue el objeto Direccion
    direccion = proveedor.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)

# ------------ Borrado logico ------------

def desactivar_proveedor(id_proveedor):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    proveedor.estado = False
    return guardar_proveedor(proveedor)

def activar_proveedor(id_proveedor):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    proveedor.estado = True
    return guardar_proveedor(proveedor)

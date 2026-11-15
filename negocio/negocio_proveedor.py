from peewee import PeeweeException

from datos.modelos.models import database
from datos.modelos.proveedor import Proveedor
from datos.repositorios.repositorio_direccion import guardar_direccion
from datos.repositorios.repositorio_proveedor import (
    listar_proveedores,
    guardar_proveedor,
    obtener_proveedor_por_id,
    existe_correo,
    existe_rut,
    buscar_proveedores_por_nombre,
    listar_proveedores_desactivados_repo
)
from auxiliares.validaciones import (validar_telefono,
                                     validar_rut,
                                     normalizar_rut)
from negocio.negocio_direccion import crear_direccion, actualizar_direccion

# ------------ Validaciones ------------
# La presentacion usa estas funciones para no importar directamente
# desde auxiliares ni desde los repositorios.

def validar_rut_ingresado(rut):
    return validar_rut(rut)

def rut_en_uso(rut):
    # Sin RUT no hay duplicado: varios proveedores extranjeros pueden no tenerlo.
    if rut is None:
        return False
    return existe_rut(normalizar_rut(rut))

# Convierte un texto vacio en None, porque en la BD una columna UNIQUE
# acepta varios NULL, pero no dos textos vacios "".
def texto_o_none(texto):
    if texto is None:
        return None
    texto = texto.strip()
    return texto if texto else None


def correo_en_uso(correo, id_proveedor=None):
    return existe_correo(correo, id_proveedor)

def validar_telefono_ingresado(telefono):
    return validar_telefono(telefono)


# Reglas de M08. Devuelve True si los datos se pueden guardar.
def datos_proveedor_validos(rut, nombre, correo, telefono, id_proveedor=None):
    # Nombre y correo son obligatorios (NOT NULL en el DDL)
    if nombre is None or correo is None:
        return False

    # El RUT es opcional: solo se valida si se escribio
    if rut is not None:
        if not validar_rut(rut) or rut_en_uso(rut):
            return False

    # El correo no se puede repetir
    if correo_en_uso(correo, id_proveedor):
        return False

    # El telefono es opcional y puede repetirse: solo se revisa el formato
    if telefono is not None and not validar_telefono(telefono):
        return False

    return True

# ------------ Lectura ------------

def listar_proveedores_activos():
    return listar_proveedores()

def listar_proveedores_desactivados():
    return listar_proveedores_desactivados_repo()

def buscar_proveedores(nombre):
    return buscar_proveedores_por_nombre(nombre)

def obtener_proveedor(id_proveedor):
    return obtener_proveedor_por_id(id_proveedor)

# ------------ Escritura ------------

def registrar_proveedor(rut, nombre, correo, telefono, calle, numero, comuna, ciudad):
    rut = texto_o_none(rut)
    # Se guarda siempre como 12345678-5 para que el mismo RUT no se repita
    if rut is not None:
        rut = normalizar_rut(rut)
    nombre = texto_o_none(nombre)
    correo = texto_o_none(correo)
    telefono = texto_o_none(telefono)

    if not datos_proveedor_validos(rut, nombre, correo, telefono):
        return False

    nuevo_proveedor = Proveedor()
    nuevo_proveedor.rut = rut
    nuevo_proveedor.nombre = nombre
    nuevo_proveedor.correo = correo
    nuevo_proveedor.telefono = telefono

    try:
        # atomic: si falla el proveedor, se revierte la direccion, asi no queda huerfana
        with database.atomic() as transaccion:
            nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)

            if not guardar_direccion(nueva_direccion):
                transaccion.rollback()
                return False

            # nueva_direccion es el objeto Direccion y contiene id_direccion
            nuevo_proveedor.id_direccion = nueva_direccion

            if not guardar_proveedor(nuevo_proveedor):
                transaccion.rollback()
                return False

        return True

    except PeeweeException:
        return False


def actualizar_proveedor(proveedor: Proveedor, correo, telefono):
    if proveedor is None:
        return False

    correo = texto_o_none(correo)
    telefono = texto_o_none(telefono)

    # El RUT no se modifica aqui, por eso se pasa None: si se pasara el actual,
    # rut_en_uso encontraria al mismo proveedor y rechazaria la actualizacion.
    # Se pasa el id del proveedor para que pueda conservar su propio correo.
    if not datos_proveedor_validos(None, proveedor.nombre, correo, telefono,
                                   proveedor.id_proveedor):
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
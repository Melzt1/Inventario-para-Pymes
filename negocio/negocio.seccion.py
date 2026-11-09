from peewee import PeeweeException

from datos.modelos.seccion import Seccion
from datos.modelos.seccion import Almacen
from datos.repositorios.repositorio_seccion import guardar_seccion
from datos.repositorios.repositorio_seccion import listar_secciones_de_almacen

def listar_secciones():
    return listar_secciones_de_almacen()   

def crear_seccion(almacen: Almacen, nombre, codigo, descripcion):
    if almacen is None:
        return False

    if codigo == "1-P":
        return False

    seccion = Seccion()
    seccion.nombre = nombre
    seccion.codigo = codigo
    seccion.descripcion = descripcion
    seccion.id_almacen = almacen

    try:
        return guardar_seccion(seccion)
    except PeeweeException:
        return False

def actualizar_seccion(seccion: Seccion, nombre, codigo, descripcion):
    if seccion is None:
        return False

    if codigo == "1-P":
        return False

    seccion.nombre = nombre
    seccion.codigo = codigo
    seccion.descripcion = descripcion

    try:
        return guardar_seccion(seccion)
    except PeeweeException:
        return False


def desactivar_seccion(seccion: Seccion):
    if seccion is None or seccion.nombre == "Principal":
        return False

    seccion.estado = False

    try:
        return guardar_seccion(seccion)
    except PeeweeException:
        return False

def activar_seccion(seccion: Seccion):
    if seccion is None:
        return False

    seccion.estado = True
    
    try:
        return guardar_seccion(seccion)
    except PeeweeException:
        return False    
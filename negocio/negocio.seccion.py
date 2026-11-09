from peewee import PeeweeException

from datos.modelos.seccion import Seccion
from datos.repositorios.repositorio_seccion import guardar_seccion

# Metodo para crear y devolver el objeto Direccion sin guardar
# Se usa para asociarlo a un proveedor o almacen y guardarlo despues.
def crear_seccion(nombre, codigo, descripcion):
    seccion = Seccion()
    seccion.nombre = nombre
    seccion.codigo = codigo
    seccion.descripcion = descripcion

    try:
        return guardar_seccion(seccion)
    except PeeweeException:
        return False

def actualizar_seccion(seccion: Seccion, nombre, codigo, descripcion):
    if seccion is None:
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
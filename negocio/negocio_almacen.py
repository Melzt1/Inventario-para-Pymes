from peewee import PeeweeException

from datos.modelos.models import database
from datos.modelos.almacen import Almacen
from datos.modelos.seccion import Seccion
from datos.repositorios.repositorio_almacen import (
    listar_almacenes, 
    guardar_almacen, 
    obtener_almacen_por_id,
    listar_almacenes_desactivados as listar_almacenes_desactivados_repo
)
from datos.repositorios.repositorio_direccion import guardar_direccion
from datos.repositorios.repositorio_seccion import guardar_seccion
from negocio.negocio_direccion import crear_direccion, actualizar_direccion


# ------------ Lectura ------------

# La presentacion NO debe conocer la capa de datos: solo importa de aqui.
# Si una consulta necesita una regla, se agrega aqui y la presentacion no se toca.

def listar_almacenes_activos():
    return listar_almacenes()   
   
def listar_almacenes_desactivados():
    return listar_almacenes_desactivados_repo()      

def obtener_almacen(id_almacen):
    return obtener_almacen_por_id(id_almacen)   

# ------------ Escritura ------------

def crear_almacen(nombre, calle, numero, comuna, ciudad):
    try:
        # atomic() si falla la creacion de uno de los objetos se revierte y no guarda datos huerfanos.
        with database.atomic():
            nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)
            guardar_direccion(nueva_direccion)

            nuevo_almacen = Almacen()
            nuevo_almacen.nombre = nombre
            nuevo_almacen.id_direccion = nueva_direccion # es lo mismo que (nueva_direccion.id_direccion)
            guardar_almacen(nuevo_almacen)

            # REGLA DE NEGOCIO: 
            # Al momento de crear un almacen DEBE nacer con una seccion principal
            principal = Seccion()
            principal.nombre = "Principal"
            principal.descripcion = "Seccion Principal"
            principal.id_almacen = nuevo_almacen
            guardar_seccion(principal)

        return True

    except (PeeweeException, ValueError):
        return False      

def actualizar_almacen(almacen: Almacen, nombre):
    if almacen is None:
        return False

    almacen.nombre = nombre
    return guardar_almacen(almacen)

def actualizar_direccion_almacen(almacen: Almacen, calle, numero, comuna, ciudad):
    if almacen is None:
        return False

    # La relacion (clave foranea) hace que almacen.id_direccion entregue el objeto Direccion
    direccion = almacen.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)

# ------------ Borrado logico ------------
def desactivar_almacen(almacen: Almacen):
    if almacen is None:
        return False

    # estado es un booleano, basta cambiarlo a False
    almacen.estado = False

    try:
        return guardar_almacen(almacen)
    except PeeweeException:
        return False

def activar_almacen(almacen: Almacen):
    if almacen is None:
        return False

    almacen.estado = True

    try:
        return guardar_almacen(almacen)
    except PeeweeException:
        return False


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

def crear_almacen(nombre, encargado, calle, numero, comuna, ciudad):
    try:
        # atomic() si falla el almacen, se revierte la direccion, asi no queda huerfana)
        with database.atomic():
            nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)
            if not guardar_direccion(nueva_direccion):
                return False

            nuevo_almacen = Almacen()
            nuevo_almacen.nombre = nombre
            nuevo_almacen.encargado = encargado
            # Peewee acepta el objeto relacionado y usa su PK como valor de la FK
            # Internamente hace esto (nueva_direccion.id_direccion)
            nuevo_almacen.id_direccion = nueva_direccion

            # REGLA DE NEGOCIO: 
            # Al momento de crear un almacen DEBE nacer con una seccion principal
            seccion_principal = Seccion()
            seccion_principal.nombre = "Principal"
            seccion_principal.codigo = "1-P"
            seccion_principal.descripcion = "Seccion Principal"
            seccion_principal.id_almacen = nuevo_almacen
            """ POR PROBAR, PUEDE QUE DE ERROR PQ SE ESTA CREANDO ANTES DE CREAR EL ALMACEN
                Y PUEDE FALLAR POR CULPA DE LA FK, SI ESTO NO FUNCIONA CREA UN METODO EN LA
                CAPA DE NEGOCIO DE SECCION, ALGO COMO CREAR_SECCION_PRINCIPAL Y LISTO"""
        
            if not guardar_seccion(seccion_principal):
                return False

            if not guardar_almacen(nuevo_almacen):
                return False

        return True

    except PeeweeException:
        return False      

def actualizar_almacen(almacen: Almacen, nombre, encagado):
    if almacen is None:
        return False

    almacen.nombre = nombre
    almacen.encargado = encagado
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


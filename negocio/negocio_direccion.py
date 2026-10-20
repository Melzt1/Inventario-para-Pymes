from peewee import PeeweeException

from datos.modelos.direccion import Direccion
from datos.repositorios.repositorio_direccion import guardar_direccion

# Metodo para crear y devolver el objeto Direccion sin guardar
# Se usa para asociarlo a un proveedor o almacen y guardarlo despues.
def crear_direccion(calle, numero, comuna, ciudad):
    nueva_direccion = Direccion()
    nueva_direccion.calle = calle
    nueva_direccion.numero = numero
    nueva_direccion.comuna = comuna
    nueva_direccion.ciudad = ciudad
    return nueva_direccion

def actualizar_direccion(direccion, calle, numero, comuna, ciudad):
    direccion.calle = calle
    direccion.numero = numero
    direccion.comuna = comuna
    direccion.ciudad = ciudad    

    try:
        return guardar_direccion(direccion)
    except PeeweeException:
        return False


from datos.modelos.direccion import Direccion
from datos.repositorios.repositorio_direccion import guardar_direcciones

# Metodo para crear y devolver el objeto Direccion sin guardar
# para asociarlo a un proveedor o alamcen y guardarlo despues
def crear_direccion(calle, numero, comuna, ciudad):
    nueva_direccion = Direccion()
    nueva_direccion.calle = calle
    nueva_direccion.numero = numero
    nueva_direccion.comuna = comuna
    nueva_direccion.ciudad = ciudad
    return nueva_direccion

# Actualiza los datos del objeto Direccion recibido y guarda los cambios
def actualizar_direccion(direccion, calle, numero, comuna, ciudad):
    direccion.calle = calle
    direccion.numero = numero
    direccion.comuna = comuna
    direccion.ciudad = ciudad    
    return guardar_direcciones(direccion)

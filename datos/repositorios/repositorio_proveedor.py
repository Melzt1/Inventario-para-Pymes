from datos.modelos.proveedor import Proveedor
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_proveedores():
    return Proveedor.select().where(Proveedor.estado == True) #para ocultar las de borrado logico

def guardar_proveedores(proveedor:Proveedor):
    try:
        return proveedor.save()

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False

# CONSULTAS A LA DB
def obtener_proveedor_por_id(id_proveedor):
    try:
        return Proveedor[id_proveedor]
    except Proveedor.DoesNotExist:
        return None

# consulta si el rut ya existe en la db
def existe_rut(rut):
    return Proveedor.select().where(Proveedor.rut == rut).exists()

# Consultar si el correo y telefono ingresado ya existen en la db ignorando al objeto Proveedor actual
def existe_correo(correo, id_proveedor=None):
    consulta = Proveedor.select().where(Proveedor.correo == correo)
    if id_proveedor is not None:
        consulta = consulta.where(Proveedor.id_proveedor != id_proveedor)
    return consulta.exists()

def existe_telefono(telefono, id_proveedor=None):
    consulta = Proveedor.select().where(Proveedor.telefono == telefono)
    if id_proveedor is not None:
        consulta = consulta.where(Proveedor.id_proveedor != id_proveedor)
    return consulta.exists()

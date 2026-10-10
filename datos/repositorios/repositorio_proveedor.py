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

# Consultar si el correo, telefono y rut ingresado ya existe en la db 
def existe_correo(correo):
    return Proveedor.select().where(Proveedor.correo == correo).exists()

def existe_telefono(telefono):
    return Proveedor.select().where(Proveedor.telefono == telefono).exists()

def existe_rut(rut):
    return Proveedor.select().where(Proveedor.rut == rut).exists()
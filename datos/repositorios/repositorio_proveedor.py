from datos.modelos.proveedor import Proveedor
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_proveedores():
    proveedores = Proveedor.select()
    if proveedores:
        return proveedores

def guardar_proveedores(proveedor:Proveedor):
    try:
        guardar_proveedor = proveedor.save()
        if guardar_proveedor:
            print(f"Proveedor registrado con exito con ID: {proveedor.id_proveedor}")
        return True

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")
    finally:
        print("Proceso finalizado.")

    return False
             

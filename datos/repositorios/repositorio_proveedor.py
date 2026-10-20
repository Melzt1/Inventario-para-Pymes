from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.proveedor import Proveedor

# ------------ Lectura ------------

def listar_proveedores():
    return Proveedor.select().where(Proveedor.estado == True)

def obtener_proveedor_por_id(id_proveedor):
    return Proveedor.get_or_none(Proveedor.id_proveedor == id_proveedor)

def buscar_proveedores_por_nombre(nombre):
    return (Proveedor.select()
            .where(Proveedor.nombre.contains(nombre) & Proveedor.estado == True)
            .order_by(Proveedor.nombre))

# ------------ Escritura ------------

def guardar_proveedor(proveedor:Proveedor):
    try:
        proveedor.save()
        return True

    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False

# ------------ Validaciones UNIQUE ------------

def existe_rut(rut):
    return Proveedor.select().where(Proveedor.rut == rut).exists()

# Excluye el proveedor indicado para que conserve su correo actual al hacer un UPDATE
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

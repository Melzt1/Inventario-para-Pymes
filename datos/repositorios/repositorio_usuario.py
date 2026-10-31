from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.usuario import Usuario

# ------------ Lectura ------------
def listar_usuarios():
    return Usuario.select().where(Usuario.estado == True).order_by(Usuario.nombre)

def obtener_usuario_por_nombre(usuario):
    return Usuario.get_or_none(Usuario.usuario == usuario)

# ------------ Escritura ------------

# .save() sirve para CREATE y UPDATE 
def guardar_usuario(usuario:Usuario):
    try:
        usuario.save()
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



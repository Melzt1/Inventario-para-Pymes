from datos.modelos.rol import Rol

# ------------ Lectura ------------
def listado_roles():
    return Rol.select()


def obtener_rol_por_id(id_rol):
    return Rol.get_or_none(Rol.id_rol == id_rol)


# no lleva de escritura ya que solo contara con dos roles, ('Administrador'), ('Trabajador') 
# Que se crean al iniciar.
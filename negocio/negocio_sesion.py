from datos.modelos.usuario import Usuario
from negocio.negocio_usuario_almacen import listar_almacenes_de_usuario
from negocio.negocio_usuario import autenticar

ROL_ADMINISTRADOR = "Administrador"

class Sesion:
    def __init__(self, usuario: Usuario):
        self.usuario_actual = usuario
    # Cada fila es una asignacion: el almacen esta en fila.id_almacen
        self.almacenes = []
        for fila in listar_almacenes_de_usuario(usuario):
            self.almacenes.append(fila.id_almacen)
        
    def tiene_rol(self, nombre_rol):
        return self.usuario_actual.id_rol.nombre == nombre_rol
    
    def es_administrador(self):
        return self.tiene_rol(ROL_ADMINISTRADOR)
    
    def puede_acceder_almacen(self, almacen):
        if self.es_administrador():
            return True
        return any(a.id_almacen == almacen.id_almacen for a in self.almacenes)


    # Metodo auxiliar que pregunta si tiene almacenes (util para imprimir)
    # El admin accede a todos por su rol
    def tiene_almacenes(self):
        return self.es_administrador() or len(self.almacenes) > 0

# ------------- INICALIZACION DE SESION -------------
def iniciar_sesion(nombre_usuario, contrasena):
    usuario = autenticar(nombre_usuario, contrasena)
    
    if usuario is None:
        return None
    
    return Sesion(usuario)

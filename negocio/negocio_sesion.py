from datos.modelos.usuario import Usuario

class Sesion:
    def __init__(self, usuario:Usuario):

        if usuario is None:
            raise ValueError("Usuario o contrasena invalido.")

        self.usuario_actual = usuario # Guardo la instancia de Usuario
        self.almacen = usuario.id_almacen # Guardo el almacen asociado al usuario
        self.sesion_activa = False

    def iniciar_sesion(self):
        self.sesion_activa = True

    # Al cerrar sesion limpiamos todos los datos antes de poner False
    def cerrar_sesion(self):
        self.usuario_actual = None
        self.almacen = None
        self.sesion_activa = False

    # Para comprobar que rol tiene el usuario
    def tiene_rol(self):
        pass

    # Para comprobar si el usuario(Trabajdor) tiene autorizacion para acceder a su almacen
    def puede_acceder_almacen(self):
        pass
        
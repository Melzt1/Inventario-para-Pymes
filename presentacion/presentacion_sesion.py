from auxiliares.entradas import campo_obligatorio
from negocio.negocio_usuario import autenticar
from negocio.negocio_sesion import Sesion

def solicitar_iniciar_sesion():
    sesion = None

    while sesion is None:
        nombre_usuario = campo_obligatorio("Usuario: ")
        contrasena = campo_obligatorio("Contrasena: ")

        # Este metodo se encarga de validar los datos y devolver el objeto
        # aun no hace nada, se encuentra en desarrollo
        usuario = autenticar(nombre_usuario, contrasena)

        if usuario is None:
            print("Usuario o contrasena incorrectos.")
        else:
            # Si el usuario esta autenticado se crea la instancia de Sesion
            # El constructor lo almacena en self.usuario_actual 
            sesion = Sesion(usuario) 
            sesion.iniciar_sesion()
    return sesion # Se retorna el objeto para usarlo en app.py               
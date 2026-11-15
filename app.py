from presentacion import menu_principal
from presentacion.presentacion_sesion import solicitar_iniciar_sesion

# Al cerrar sesion se vuelve a pedir usuario y contraseña.
# El programa termina al elegir "Salir" o al agotar los intentos de inicio de sesion.
continuar = True

while continuar:
    sesion = solicitar_iniciar_sesion()

    if sesion is None:
        continuar = False
    else:
        # menu_principal devuelve True si se cerro sesion y False si se eligio Salir
        continuar = menu_principal(sesion)
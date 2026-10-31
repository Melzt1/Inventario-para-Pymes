from presentacion import menu_principal
from presentacion.presentacion_sesion import solicitar_iniciar_sesion

sesion = solicitar_iniciar_sesion()
if sesion is not None:
    menu_principal()

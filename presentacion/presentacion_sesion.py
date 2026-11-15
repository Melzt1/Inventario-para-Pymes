from getpass import getpass

from negocio.negocio_sesion import iniciar_sesion

# Cantidad de intentos antes de cerrar el programa
INTENTOS_MAXIMOS = 3


# Pide usuario y contraseña hasta que sean correctos o se acaben los intentos.
# Devuelve la Sesion iniciada, o None si no se pudo iniciar.
def solicitar_iniciar_sesion():
    print("\n=== Iniciar sesion ===")

    sesion = None
    intentos = 0

    while sesion is None and intentos < INTENTOS_MAXIMOS:
        nombre_usuario = input("Usuario: ").strip()
        contrasena = getpass("Contraseña: ")
        intentos += 1

        sesion = iniciar_sesion(nombre_usuario, contrasena)

        if sesion is None:
            restantes = INTENTOS_MAXIMOS - intentos
            # Mismo mensaje para usuario inexistente, inactivo o contraseña incorrecta:
            # asi no se revela cual de los tres fallo
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {restantes}")

    if sesion is None:
        print("Se agotaron los intentos. Programa finalizado.")
        return None

    usuario = sesion.usuario_actual
    print(f"\nBienvenido(a), {usuario.nombre} ({usuario.id_rol.nombre}).")
    return sesion

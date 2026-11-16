from getpass import getpass

from prettytable import PrettyTable

from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from negocio.negocio_usuario import (
    listar_usuarios_activos,
    listar_usuarios_inactivos,
    listar_roles,
    listar_trabajores,
    nombre_usuario_en_uso,
    errores_contrasena,
    registrar_usuario,
    actualizar_usuario,
    cambiar_contrasena,
    desactivar_usuario,
    activar_usuario
)

# En este archivo:
#   usuario        = el OBJETO Usuario
#   nombre_usuario = el TEXTO con el que la persona inicia sesion (ej: "ale.g")


# ------------ Auxiliares ------------

# Muestra una lista numerada y devuelve el elemento elegido.
# "describir" es una funcion que recibe un elemento y devuelve el texto a mostrar.
def elegir_de_lista(elementos, describir, mensaje):
    for i, elemento in enumerate(elementos, start=1):
        print(f"[{i}] - {describir(elemento)}")

    elegido = None
    while elegido is None:
        seleccion = forzar_entero(mensaje)

        if 1 <= seleccion <= len(elementos):
            elegido = elementos[seleccion - 1]
        else:
            print(f"Opcion fuera de rango (1-{len(elementos)}).")
    return elegido


def describir_usuario(usuario):
    return f"{usuario.nombre} ({usuario.usuario}) - {usuario.id_rol.nombre}"


def solicitar_seleccion_usuario(usuarios, titulo):
    usuarios = list(usuarios)

    if not usuarios:
        print("No hay usuarios para mostrar.")
        return None

    print(f"\n{titulo}")
    return elegir_de_lista(usuarios, describir_usuario, "\nSeleccione el usuario: ")


def solicitar_seleccion_rol():
    roles = list(listar_roles())

    if not roles:
        print("No hay roles registrados.")
        return None

    print("\nRoles disponibles:")
    return elegir_de_lista(roles, lambda rol: rol.nombre, "\nSeleccione el rol: ")


# Pide un nombre de usuario que no este en uso.
# Al actualizar se pasa el usuario para que pueda conservar el suyo con ENTER.
def solicitar_nombre_usuario(usuario=None):
    nombre_usuario = None

    while nombre_usuario is None:
        if usuario is None:
            texto = campo_obligatorio("Ingrese el nombre de usuario (para iniciar sesion): ")
            id_excluir = None
        else:
            texto = campo_opcional("Ingrese el nuevo nombre de usuario", usuario.usuario)
            id_excluir = usuario.id_usuario

        if nombre_usuario_en_uso(texto, id_excluir):
            print(f"El nombre de usuario '{texto}' ya esta en uso. Ingrese otro.")
        else:
            nombre_usuario = texto

    return nombre_usuario


# Pide la contraseña nueva hasta que cumpla todas las reglas y se confirme.
# getpass no muestra lo que se escribe en pantalla.
def solicitar_contrasena_nueva():
    contrasena = None

    while contrasena is None:
        texto = getpass("Ingrese la contraseña: ")
        errores = errores_contrasena(texto)

        if errores:
            print("La contraseña no cumple con:")
            for error in errores:
                print(f"  - {error}")
        elif getpass("Repita la contraseña: ") != texto:
            print("Las contraseñas no coinciden. Intente nuevamente.")
        else:
            contrasena = texto

    return contrasena

# ------------ Lectura ------------

def mostrar_usuarios():
    usuarios = list(listar_usuarios_activos())

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Usuario', 'Rol', 'Estado', 'Fecha creacion']

    for usuario in usuarios:
        tabla.add_row([
            usuario.id_usuario,
            usuario.nombre,
            usuario.usuario,
            usuario.id_rol.nombre,
            ('Deshabilitado', 'Habilitado')[usuario.estado],
            usuario.fecha_creacion,
        ])

    print(tabla)

# ------------ Escritura ------------

def solicitar_registrar_usuario():
    print("\n=== Registrar usuario ===")

    nombre = campo_obligatorio("Ingrese el nombre completo: ")
    nombre_usuario = solicitar_nombre_usuario()

    rol = solicitar_seleccion_rol()
    if rol is None:
        return

    contrasena = solicitar_contrasena_nueva()

    resultado = registrar_usuario(nombre, nombre_usuario, contrasena, rol)
    print(f"Usuario '{nombre_usuario}' registrado con exito.") if resultado else print("No se pudo registrar el usuario.")


def solicitar_actualizar_usuario():
    usuario = solicitar_seleccion_usuario(listar_usuarios_activos(), "=== Actualizar usuario ===")
    if usuario is None:
        return

    nombre = campo_opcional("Ingrese el nuevo nombre", usuario.nombre)
    nombre_usuario = solicitar_nombre_usuario(usuario)

    rol = usuario.id_rol
    print(f"Rol actual: {rol.nombre}")
    if input("¿Desea cambiar el rol? (S/N): ").strip().upper() == "S":
        rol = solicitar_seleccion_rol() or rol

    resultado = actualizar_usuario(usuario, nombre, nombre_usuario, rol)
    print("Usuario actualizado con exito.") if resultado else print("No se pudo actualizar el usuario.")


def solicitar_cambiar_contrasena():
    usuario = solicitar_seleccion_usuario(listar_usuarios_activos(), "=== Cambiar contraseña ===")
    if usuario is None:
        return

    contrasena_actual = getpass("Ingrese la contraseña actual: ")

    print("Ahora ingrese la contraseña nueva.")
    contrasena_nueva = solicitar_contrasena_nueva()

    resultado = cambiar_contrasena(usuario, contrasena_actual, contrasena_nueva)
    print("Contraseña cambiada con exito.") if resultado else print("No se pudo cambiar la contraseña. Revise la contraseña actual.")

# ------------ Borrado logico ------------

def solicitar_desactivar_usuario():
    usuario = solicitar_seleccion_usuario(listar_trabajores(), "=== Desactivar usuario ===")
    if usuario is None:
        return

    resultado = desactivar_usuario(usuario)
    print(f"Usuario '{usuario.usuario}' desactivado.") if resultado else print("No se pudo desactivar el usuario.")


def solicitar_activar_usuario():
    usuario = solicitar_seleccion_usuario(listar_usuarios_inactivos(), "=== Usuarios desactivados ===")
    if usuario is None:
        return

    resultado = activar_usuario(usuario)
    print(f"Usuario '{usuario.usuario}' activado.") if resultado else print("No se pudo activar el usuario.")

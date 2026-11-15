from prettytable import PrettyTable

from negocio.negocio_usuario import listar_usuarios_activos
from negocio.negocio_almacen import listar_almacenes_activos
from negocio.negocio_usuario_almacen import (
    listar_almacenes_de_usuario,
    listar_usuarios_de_almacen,
    asignar_usuario_almacen,
    quitar_usuario_almacen,
    cambiar_encargado
)
from presentacion.presentacion_usuario import (elegir_de_lista,
                                               solicitar_seleccion_usuario)


# ------------ Auxiliares ------------

def solicitar_almacen(titulo):
    almacenes = list(listar_almacenes_activos())

    if not almacenes:
        print("No hay almacenes activos.")
        return None

    print(f"\n{titulo}")
    return elegir_de_lista(almacenes, lambda almacen: almacen.nombre, "\nSeleccione el almacen: ")


def solicitar_trabajador(titulo):
    return solicitar_seleccion_usuario(listar_usuarios_activos(), titulo)

# ternario
def texto_encargado(asignacion):
    return "Encargado" if asignacion.es_encargado else "-"

# ------------ Lectura ------------

def mostrar_almacenes_de_usuario():
    usuario = solicitar_trabajador("=== Almacenes de un usuario ===")
   
    if usuario is None:
        return

    asignaciones = list(listar_almacenes_de_usuario(usuario))
    
    if not asignaciones:
        print(f"'{usuario.usuario}' no tiene almacenes asignados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID Almacen', 'Almacen', 'Encargado']
    
    for asignacion in asignaciones:
        tabla.add_row([
            asignacion.id_almacen.id_almacen,
            asignacion.id_almacen.nombre,
            texto_encargado(asignacion),
        ])

    print(f"\n=== Almacenes de '{usuario.usuario}' ===")
    print(tabla)


def mostrar_usuarios_de_almacen():
    almacen = solicitar_almacen("=== Usuarios de un almacen ===")
    
    if almacen is None:
        return

    asignaciones = list(listar_usuarios_de_almacen(almacen))
    if not asignaciones:
        print(f"El almacen '{almacen.nombre}' no tiene usuarios asignados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID Usuario', 'Nombre', 'Usuario', 'Rol', 'Encargado']
    for asignacion in asignaciones:
        usuario = asignacion.id_usuario
        tabla.add_row([
            usuario.id_usuario,
            usuario.nombre,
            usuario.usuario,
            usuario.id_rol.nombre,
            texto_encargado(asignacion),
        ])

    print(f"\n=== Usuarios de '{almacen.nombre}' ===")
    print(tabla)

# ------------ Escritura ------------

def solicitar_asignar_usuario_almacen():
    usuario = solicitar_trabajador("=== Asignar usuario a almacen ===")
    if usuario is None:
        return

    almacen = solicitar_almacen("Almacenes disponibles:")
    if almacen is None:
        return

    resultado = asignar_usuario_almacen(usuario, almacen)
    if resultado:
        print(f"'{usuario.usuario}' asignado a '{almacen.nombre}' con exito.")
    else:
        print(f"No se pudo asignar. Revise si '{usuario.usuario}' ya esta en '{almacen.nombre}'.")


def solicitar_quitar_usuario_almacen():
    usuario = solicitar_trabajador("=== Quitar usuario de un almacen ===")
    if usuario is None:
        return

    # Solo se muestran los almacenes donde el usuario esta asignado
    asignaciones = list(listar_almacenes_de_usuario(usuario))
    if not asignaciones:
        print(f"'{usuario.usuario}' no tiene almacenes asignados.")
        return

    print(f"\nAlmacenes de '{usuario.usuario}':")
    asignacion = elegir_de_lista(
        asignaciones,
        lambda a: f"{a.id_almacen.nombre} ({texto_encargado(a)})",
        "\nSeleccione el almacen a quitar: "
    )

    almacen = asignacion.id_almacen
    resultado = quitar_usuario_almacen(usuario, almacen)
    print(f"'{usuario.usuario}' quitado de '{almacen.nombre}'.") if resultado else print("No se pudo quitar la asignacion.")


def solicitar_cambiar_encargado():
    almacen = solicitar_almacen("=== Cambiar encargado de almacen ===")
    if almacen is None:
        return

    # Solo puede ser encargado alguien asignado a ese almacen
    asignaciones = list(listar_usuarios_de_almacen(almacen))
    if not asignaciones:
        print(f"El almacen '{almacen.nombre}' no tiene usuarios asignados. Asigne uno primero.")
        return

    print(f"\nUsuarios de '{almacen.nombre}':")
    asignacion = elegir_de_lista(
        asignaciones,
        lambda a: f"{a.id_usuario.nombre} ({a.id_usuario.usuario}) - {texto_encargado(a)}",
        "\nSeleccione el nuevo encargado: "
    )

    usuario = asignacion.id_usuario
    resultado = cambiar_encargado(usuario, almacen)
    print(f"'{usuario.usuario}' es ahora el encargado de '{almacen.nombre}'.") if resultado else print("No se pudo cambiar el encargado.")

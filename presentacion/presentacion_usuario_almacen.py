from prettytable import PrettyTable

from auxiliares.entradas import solicitar_confirmacion
from negocio.negocio_usuario_almacen import (
    asignar_usuario,
    quitar_usuario,
    cambiar_encargado,
    listar_almacenes_de_usuario,
    listar_usuarios_de_almacen,
    es_encargado
)
from negocio.negocio_usuario import listar_usuarios_activos
from negocio.negocio_almacen import listar_almacenes_activos
from presentacion.presentacion_usuario import seleccionar_elemento

def mostrar_almacenes_de_un_usuario(): # Mostrar los almacenes donde trabaja un usuario
    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")
    if usuario is None:
        return

    # lista de almacenes donde trabaja un usuario
    almacenes = listar_almacenes_de_usuario(usuario.id_usuario)
    if not almacenes:
        print(f"{usuario.nombre} no tiene almacenes asignados")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Almacen', 'Es encargado']

    for almacen in almacenes:
        tabla.add_row([
            almacen.id_almacen,
            almacen.nombre,
            'Si' if es_encargado(usuario.id_usuario, almacen.id_almacen) else 'No',
        ])

    print(tabla)

def mostrar_usuarios_de_un_almacen(): # Muestra los usarios asignados a un almacen
    almacen = seleccionar_elemento(listar_almacenes_activos(), "almacenes")
    if almacen is None:
        return

    usuarios = listar_usuarios_de_almacen(almacen)
    if not usuarios:
        print(f"No hay usuarios asginado al almacen {almacen.nombre}")
        return

    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Usuario', 'Rol', 'Es encargado']

    for usuario in usuarios:
        tabla.add_row([
            usuario.id_usuario,
            usuario.nombre,
            usuario.usuario,
            usuario.id_rol.nombre,
            'Si' if es_encargado(usuario.id_usuario, almacen.id_almacen) else 'No',
        ])

    print(tabla)

def solicitar_asignar_usuario():
    print("\n=== Asignar usuario a un almacen ===")

    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")
    if usuario is None:
        return

    almacen = seleccionar_elemento(listar_almacenes_activos(), "almacenes")
    if almacen is None:
        return

    resultado = asignar_usuario(usuario, almacen)
    print("Usuario asignado correctamente") if resultado else print("No se pudo asignar el usuario al almacen")

def solicitar_quitar_usuario(): # Quitar un usuario de un almacen
    print("\n=== Quitar usuario de almacen ===")

    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")
    if usuario is None:
        return

    almacenes = listar_almacenes_de_usuario(usuario.id_usuario)
    if not almacenes:
        print(f"{usuario.nombre} no tiene almacenes asignados")
        return

    almacen = seleccionar_elemento(almacenes, "almacenes asignados")
    if almacen is None:
        return

    if not solicitar_confirmacion(f"Quitar {usuario.nombre} de {almacen.nombre} ?"):
        return

    resultado = quitar_usuario(usuario, almacen)
    print("Usuario eliminado del almacen") if resultado else print("No se pudo quitar del almacen")

def solicitar_cambiar_encargado():
    print("\n=== Cambiar encargado de almacen ===")

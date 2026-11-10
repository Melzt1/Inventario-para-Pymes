from prettytable import PrettyTable

from auxiliares.mensajes import NO_HAY_SECCIONES
from auxiliares.entradas import campo_obligatorio, forzar_entero
from negocio.negocio_seccion import (
    activar_seccion,
    actualizar_seccion,
    crear_seccion,
    desactivar_seccion,
    listar_secciones,
    listar_secciones_desactivadas,
)
from presentacion.presentacion_almacen import solicitar_seleccion_almacen

# Metodo auxiliar para seleccionar secciones
def seleccionar_seccion(secciones):
    if not secciones:
        print(NO_HAY_SECCIONES)
        return None


    for i, seccion in enumerate(secciones, start=1):
        print(f"[{i}] - {seccion.nombre}")

    seleccion = forzar_entero("Seleccione la seccion: ")

    if not 1 <= seleccion <= len(secciones):
        print(f"Opción fuera de rango (1-{len(secciones)}).")
        return None
    
    return secciones[seleccion - 1]
        
def mostrar_secciones_de_un_almacen():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return 

    secciones = listar_secciones(almacen)

    tabla_secciones = PrettyTable()
    tabla_secciones.field_names = ['ID', 'Nombre', 'Descripcion', 'Estado', 'ID Almacen']

    for seccion in secciones:
        tabla_secciones.add_row([
            seccion.id_seccion,
            seccion.nombre,
            seccion.descripcion,
            ('Deshabilitado', 'Habilitado')[seccion.estado],
            seccion.id_almacen
        ])
    print(tabla_secciones)    

def solicitar_crear_seccion():
    # Primero se selecciona un almacen
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        print("Primero debes registrar un Almacen")
        return

    nombre = campo_obligatorio("Nombre de la seccion: ")
    descripcion = input("Descripcion (opcional): ").strip()

    resultado = crear_seccion(almacen, nombre, descripcion)
    print("Seccion registrada con exito." if resultado else "No se pudo registrar la seccion.")


def solicitar_actualizar_seccion():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    seccion = seleccionar_seccion(listar_secciones(almacen))

    if seccion is None:
        print(NO_HAY_SECCIONES)
        return

    nombre = input("Nuevo nombre de la seccion: ").title()

    while nombre == "Principal" or nombre == "PRINCIPAL":
        print("El nombre 'Principal' esta reservado por el sistema. Ingresa otro.")
        nombre = input("Nuevo nombre de la seccion: ").title()

    descripcion = input("Nueva descripcion: ").strip()
    resultado = actualizar_seccion(almacen, nombre, descripcion)
    print("Seccion actualizada con exito." if resultado else "No se pudo actualizar la seccion.")

def solicitar_desactivar_seccion():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    seccion = seleccionar_seccion(listar_secciones(almacen))

    if seccion is None:
        print(NO_HAY_SECCIONES)
        return
    
    resultado = desactivar_seccion(seccion)
    print("Seccion desactivada con exito." if resultado else "No se pudo desactivar la seccion.")    

def solicitar_activar_seccion():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    seccion = seleccionar_seccion(listar_secciones_desactivadas(almacen))

    if seccion is None:
        print("No hay secciones desactivadas.")
        return
    
    resultado = activar_seccion(seccion)
    print("Seccion activada con exito." if resultado else "No se pudo activar la seccion.")     
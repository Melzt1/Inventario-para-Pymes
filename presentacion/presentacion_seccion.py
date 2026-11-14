from prettytable import PrettyTable

from auxiliares.mensajes import NO_HAY_SECCIONES
from auxiliares.entradas import campo_obligatorio, forzar_entero, campo_opcional
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

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("Seleccione la seccion: ")

        if 1 <= seleccion <= len(secciones):
            opcion_valida = True
            return secciones[seleccion - 1] 
        
        print(f"Opción fuera de rango (1-{len(secciones)}).")
        
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
        return

    nombre = campo_opcional("Ingrese el nuevo nombre", seccion.nombre).capitalize()

    while nombre == "Principal" or nombre == "PRINCIPAL":
        print("El nombre 'Principal' esta reservado por el sistema. Ingresa otro.")
        nombre = input("Nuevo nombre de la seccion: ").title()

    descripcion = input("Nueva descripcion: ").strip()
    resultado = actualizar_seccion(seccion, nombre, descripcion)
    print("Seccion actualizada con exito." if resultado else "No se pudo actualizar la seccion.")

def solicitar_desactivar_seccion():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    seccion = seleccionar_seccion(listar_secciones(almacen))

    if seccion is None:
        return

    if seccion.nombre == "Principal":
        print("La seccion 'Principal' no se puede desactivar")
        return False
    
    resultado = desactivar_seccion(seccion)
    print("Seccion desactivada con exito." if resultado else "No se pudo desactivar la seccion.")    

def solicitar_activar_seccion():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    seccion = seleccionar_seccion(listar_secciones_desactivadas(almacen))

    if seccion is None:
        return
    
    resultado = activar_seccion(seccion)
    print("Seccion activada con exito." if resultado else "No se pudo activar la seccion.")     
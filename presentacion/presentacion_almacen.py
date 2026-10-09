from negocio.negocio_almacen import listado_almacenes, crear_almacen, actualizar_almacen, actualizar_direccion_almacen, habilitar_almacen, obtener_almacen, inhabilitar_almacen
from auxiliares.mensajes import SOLICITUD_ID_ALMACEN, MENSAJE_ID_ENTERO, MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero

def solicitar_datos_almacen():
    print("\n=== Datos del almacen ===")

    nombre = input("Ingrese el nombre del almacen: ")
    encargado = input("Ingrese el nombre del encargado: ")

    
    print("\n=== Direccinn del almacen ===")
    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")
    return crear_almacen(nombre, encargado, calle, numero, comuna, ciudad)

def solicitar_actualizar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    nombre = input("Ingrese el nuevo nombre del almacen: ")
    encargado = input("Ingrese el nombre del nuevo encargado: ")    
    return actualizar_almacen(id_almacen, nombre, encargado)        

def solicitar_actualizar_direccion_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")
    return actualizar_direccion_almacen(id_almacen, calle, numero, comuna, ciudad)

def solicitar_inhabilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    return inhabilitar_almacen(almacen)

def solicitar_habilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    return habilitar_almacen(id_almacen)        
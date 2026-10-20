from prettytable import PrettyTable

from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from auxiliares.mensajes import SOLICITUD_ID_ALMACEN, MENSAJE_ID_NO_EXISTE
from negocio.negocio_almacen import (
    crear_almacen, 
    actualizar_almacen, 
    actualizar_direccion_almacen, 
    activar_almacen, 
    desactivar_almacen, 
    listar_almacenes_activos,
    listar_almacenes_desactivados
)

# ------------ Funcion Auxiliar ------------

def solicitar_seleccion_almacen():
    # Muestra los almacenes activos y devuelve el elegido o None
    almacenes = list(listar_almacenes_activos()) # Lista de objetos

    if not almacenes:
        print("No hay almacenes activos registrados.")
        return None

    print("\nAlmacenes disponibles:")
    for i, almacen in enumerate(almacenes, start=1):
        print(f"[{i}] - {almacen.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el almacen: ")

        if 1 <= seleccion <= len(almacenes):
            opcion_valida = True
            return almacenes[seleccion - 1] # Devuelve el objeto almacen

        print(f"Opcion fuera de rango (1-{len(almacenes)}).")

def mostrar_almacenes():
    almacenes = listar_almacenes_activos()

    if not almacenes:
        print("No hay almacenes registrados.")
        return

    tabla_almacenes = PrettyTable()
    tabla_almacenes.field_names = ['Id', 'Nombre', 'Encargado', 'Estado', 'Id Direccion']

    for almacen in almacenes:
        tabla_almacenes.add_row([
            almacen.id_almacen,
            almacen.nombre,
            almacen.encargado,
            ('Deshabilitado', 'Habilitado')[almacen.estado],
            almacen.id_direccion,
        ])

    print(tabla_almacenes)

def solicitar_datos_almacen():
    print("\n=== Registrar almacen ===")

    nombre = campo_obligatorio("Ingrese el nombre del almacen: ")
    encargado = campo_obligatorio("Ingrese el nombre del encargado: ")

    
    print("\n=== Direccion del almacen ===")
    calle = campo_obligatorio("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = campo_obligatorio("Ingrese la comuna: ")
    ciudad = campo_obligatorio("Ingrese la ciudad: ")

    resultado = crear_almacen(nombre, encargado, calle, numero, comuna, ciudad)
    print("Almacen registrado con exito.") if resultado else print("No se pudo registrar el almacen.")   

def solicitar_consultar_almacen():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    # La FK entrega el objeto Direccion
    direccion = almacen.id_direccion

    estado = "Habilitado" if almacen.estado else "Deshabilitado"

    print("\n=== Informacion Almacen ===")
    #print(f"{'ID':<16}: {almacen.id_almacen}")
    print(f"{'Nombre':<16}: {almacen.nombre}")
    print(f"{'Encargado':<16}: {almacen.encargado}")
    print(f"{'Estado':<16}: {estado}")
    print(f"{'Direccion':<16}: {direccion.calle} {direccion.numero or '_'}, {direccion.comuna}, {direccion.ciudad}\n")

def solicitar_actualizar_almacen():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    nombre = campo_opcional("Ingrese el nuevo nombre", almacen.nombre)
    encargado = campo_opcional("Ingrese el nuevo encargado", almacen.encargado)    

    resultado = actualizar_almacen(almacen.id_almacen, nombre, encargado)
    print("Almacen actualizado con exito.") if resultado else print("No se pudo actualizar el almacen.")         

def solicitar_actualizar_direccion_almacen():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return
    
    # La FK entrega el objeto Direccion
    direccion = almacen.id_direccion
    calle = campo_opcional("Ingrese el nombre de la calle", direccion.calle)
    numero = campo_opcional("Ingrese el numero de la direccion", direccion.numero)
    comuna = campo_opcional("Ingrese la comuna", direccion.comuna)
    ciudad = campo_opcional("Ingrese la ciudad", direccion.ciudad)

    resultado = actualizar_direccion_almacen(almacen.id_almacen, calle, numero, comuna, ciudad)
    print("Direccion actualizada con exito.") if resultado else print("No se pudo actualizar la direccion.")

def solicitar_desactivar_almacen():
    almacen = solicitar_seleccion_almacen()

    if almacen is None:
        return

    resultado = desactivar_almacen(almacen.id_almacen)
    print(f"Almacen: {almacen.nombre} inhabilitado con exito.") if resultado else print("No se pudo inhabilitar el almacen.")

def solicitar_activar_almacen():
    almacenes = list(listar_almacenes_desactivados()) # Lista de objetos

    if not almacenes:
        print("No hay almacenes desactivados.")
        return None

    print("\nAlmacenes Desactivados:")
    for i, almacen in enumerate(almacenes, start=1):
        print(f"[{i}] - {almacen.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el almacen: ")

        if 1 <= seleccion <= len(almacenes):
            opcion_valida = True
            almacen = almacenes[seleccion - 1] # Devuelve el objeto almacen
        else:
            print(f"Opcion fuera de rango (1-{len(almacenes)}).")

    if almacen is None:
        return False

    resultado = activar_almacen(almacen.id_almacen)  
    print(f"Almacen: {almacen.nombre} habilitado con exito.") if resultado else print("No se pudo habilitar el almacen.")      
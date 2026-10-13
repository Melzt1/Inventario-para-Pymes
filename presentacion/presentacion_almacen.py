from negocio.negocio_almacen import crear_almacen, actualizar_almacen, actualizar_direccion_almacen, habilitar_almacen, obtener_almacen, inhabilitar_almacen, lista_almacenes
from auxiliares.mensajes import SOLICITUD_ID_ALMACEN, MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from prettytable import PrettyTable

def mostrar_almacenes():
    almacenes = lista_almacenes()

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
    print("\n=== Datos del almacen ===")

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
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    # La FK entrega el objeto Direccion
    direccion = almacen.id_direccion

    estado = "Habilitado" if almacen.estado else "Deshabilitado"

    print("\n=== Almacen encontrado ===")
    print(f"{'ID':<16}: {almacen.id_almacen}")
    print(f"{'Nombre':<16}: {almacen.nombre}")
    print(f"{'Encargado':<16}: {almacen.encargado}")
    print(f"{'Estado':<16}: {estado}")
    print(f"{'Direccion':<16}  : {direccion.calle} {direccion.numero or '_'}, {direccion.comuna}, {direccion.ciudad}\n")

def solicitar_actualizar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    nombre = campo_opcional("Ingrese el nuevo nombre", almacen.nombre)
    encargado = campo_opcional("Ingrese el nuevo encargado", almacen.encargado)    

    resultado = actualizar_almacen(id_almacen, nombre, encargado)
    print("Almacen actualizado con exito.") if resultado else print("No se pudo actualizar el almacen.")         

def solicitar_actualizar_direccion_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False
    
    # La FK entrega el objeto Direccion
    direccion = almacen.id_direccion
    calle = campo_opcional("Ingrese el nombre de la calle", direccion.calle)
    numero = campo_opcional("Ingrese el numero de la direccion", direccion.numero)
    comuna = campo_opcional("Ingrese la comuna", direccion.comuna)
    ciudad = campo_opcional("Ingrese la ciudad", direccion.ciudad)

    resultado = actualizar_direccion_almacen(id_almacen, calle, numero, comuna, ciudad)
    print("Direccion actualizada con exito.") if resultado else print("No se pudo actualizar la direccion.")

def solicitar_inhabilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = inhabilitar_almacen(id_almacen)
    print(f"Almacen: {almacen.nombre} inhabilitado con exito.") if resultado else print("No se pudo inhabilitar el almacen.")

def solicitar_habilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = habilitar_almacen(id_almacen)  
    print(f"Almacen: {almacen.nombre} habilitado con exito.") if resultado else print("No se pudo habilitar el almacen.")      
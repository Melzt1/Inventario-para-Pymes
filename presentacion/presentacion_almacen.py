from negocio.negocio_almacen import crear_almacen, actualizar_almacen, actualizar_direccion_almacen, habilitar_almacen, obtener_almacen, inhabilitar_almacen
from auxiliares.mensajes import SOLICITUD_ID_ALMACEN, MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero, mostrar_resultado
from prettytable import PrettyTable

def solicitar_datos_almacen():
    print("\n=== Datos del almacen ===")

    nombre = input("Ingrese el nombre del almacen: ")
    encargado = input("Ingrese el nombre del encargado: ")

    
    print("\n=== Direccinn del almacen ===")
    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")

    resultado = crear_almacen(nombre, encargado, calle, numero, comuna, ciudad)
    mostrar_resultado(resultado, "Almacen registrado con exito.", "No se pudo registrar el almacen.")

def solicitar_consultar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    # obtener el objeto Direccion para mostrar los datos relacionados con almacen
    direccion = almacen.id_direccion

    tabla_almacen = PrettyTable()
    tabla_almacen.field_names = ['ID', 'Nombre', 'Encargado', 'Estado', 'Calle', 'Numero', 'Comuna', 'Ciudad']
    tabla_almacen.add_row([
        almacen.id_almacen,
        almacen.nombre,
        almacen.encargado,
        ('Deshabilitado', 'Habilitado')[almacen.estado],
        direccion.calle,
        direccion.numero,
        direccion.comuna,
        direccion.ciudad
    ])
    print(tabla_almacen)

def solicitar_actualizar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    nombre = input("Ingrese el nuevo nombre del almacen: ")
    encargado = input("Ingrese el nombre del nuevo encargado: ")    

    resultado = actualizar_almacen(id_almacen, nombre, encargado)
    mostrar_resultado(resultado, "Almacen actualizado con exito.", "No se pudo actualizar el almacen.")        

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

    resultado = actualizar_direccion_almacen(id_almacen, calle, numero, comuna, ciudad)
    mostrar_resultado(resultado, "Direccion actualizada con exito.", "No se pudo actualizar la direccion.")

def solicitar_inhabilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = inhabilitar_almacen(almacen)
    mostrar_resultado(resultado, f"Almacen: {almacen.nombre} inhabilitado con exito.", "No se pudo inhabilitar el almacen.")

def solicitar_habilitar_almacen():
    id_almacen = forzar_entero(SOLICITUD_ID_ALMACEN)

    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = habilitar_almacen(id_almacen)  
    mostrar_resultado(resultado, f"Almacen: {almacen.nombre} habilitado con exito.", "No se pudo habilitar el almacen.")      
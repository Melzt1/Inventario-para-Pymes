from negocio.negocio_proveedor import registrar_proveedor, obtener_proveedor, validar_rut, actualizar_proveedor, actualizar_direccion_proveedor, inhabilitar_proveedor, habilitar_proveedor, rut_en_uso, correo_en_uso, telefono_en_uso
from auxiliares.mensajes import SOLICITUD_ID_PROVEEDOR, MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero, mostrar_resultado
from prettytable import PrettyTable

def solicitar_datos_proveedor():
    print("\n=== Datos del proveedor ===")
    rut = input("Ingrese el RUT del proveedor. Ej (12.345.678-5) : ")

    if not validar_rut(rut):
        print("El rut ingresado no es valido.")
        return False
    
    if rut_en_uso(rut):
        print("El rut ya fue registrado")
        return False

    nombre = input("Ingrese el nombre o razon social: ")
    correo = input("Ingrese el correo: ")

    if correo_en_uso(correo):
        print("El correo ya fue registrado.")
        return False

    telefono = input("Ingrese el numero: ")

    if telefono_en_uso(telefono):
        print("El telefono ya fue registrado.")
        return False
    
    print("\n=== Direccinn del proveedor ===")
    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")

    resultado = registrar_proveedor(rut, nombre, correo, telefono, 
        calle, numero, comuna, ciudad)
    mostrar_resultado(resultado, "Proveedor registrado con exito.", "No se pudo registrar el proveedor")

def solicitar_consultar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    # obtener el objeto Direccion para mostrar los datos relacionados con almacen
    direccion = proveedor.id_direccion

    tabla_proveedor = PrettyTable()
    tabla_proveedor.field_names = ['ID', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Calle', 'Numero', 'Comuna', 'Ciudad']
    tabla_proveedor.add_row([
        proveedor.id_proveedor,
        proveedor.rut,
        proveedor.nombre,
        proveedor.correo,
        proveedor.telefono,
        ('Deshabilitado', 'Habilitado')[proveedor.estado],
        direccion.calle,
        direccion.numero,
        direccion.comuna,
        direccion.ciudad
    ])
    print(tabla_proveedor)

def solicitar_actualizar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    correo = input("Ingrese el nuevo correo: ").strip()

    if correo_en_uso(correo):
        print("El correo ya fue registrado")
        return False
    
    telefono = input("Ingrese el nuevo telefono: ").strip()

    if telefono_en_uso(telefono):
        print("El telefono ya fue registrado")
        return False

    resultado = actualizar_proveedor(id_proveedor, correo, telefono)
    mostrar_resultado(resultado, "Prveedor actualizado con exito.", "No se pudo actualizar el proveedor.")

def solicitar_actualizar_direccion_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        proveedor(MENSAJE_ID_NO_EXISTE)
        return

    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")

    resultado = actualizar_direccion_proveedor(id_proveedor, calle, numero, comuna, ciudad)  
    mostrar_resultado(resultado, "Direccion de proveedor actualizada con exito.", "No se pudo actualizar la direccion.")  

def solicitar_inhabilitar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    resultado = inhabilitar_proveedor(id_proveedor)
    mostrar_resultado(resultado, "Prveedor inhabilitado con exito.", "No se pudo inhabilitar el proveedor.")

def solicitar_habilitar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        proveedor(MENSAJE_ID_NO_EXISTE)
        return

    resultado = habilitar_proveedor(id_proveedor)     
    mostrar_resultado(resultado, "Prveedor habilitado con exito.", "No se pudo habilitar el proveedor.")   
from negocio.negocio_proveedor import registrar_proveedor, obtener_proveedor, validar_rut, validar_correo_en_uso, validar_telefono_en_uso, actualizar_proveedor, actualizar_direccion_proveedor, inhabilitar_proveedor, habilitar_proveedor
from auxiliares.mensajes import SOLICITUD_ID_PROVEEDOR, MENSAJE_ID_ENTERO, MENSAJE_ID_NO_EXISTE

def solicitar_datos_proveedor():
    print("\n=== Datos del proveedor ===")
    rut = input("Ingrese el RUT del proveedor. Ej (12.345.678-5) : ")

    if not validar_rut(rut):
        print("El rut ingresado no es valido.")
        return False

    nombre = input("Ingrese el nombre o razon social: ")
    correo = input("Ingrese el correo: ")

    if validar_correo_en_uso(correo):
        print("El correo ya fue registrado")
        return False
    
    telefono = input("Ingrese el telefono: ")

    if validar_telefono_en_uso(telefono):
        print("El telefono ya fue registrado")
        return False
    
    print("\n=== Direccinn del proveedor ===")
    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")
    return registrar_proveedor(rut, nombre, correo, telefono, 
        calle, numero, comuna, ciudad
    )

def solicitar_actualizar_proveedor():
    try:
        id_proveedor = int(input(SOLICITUD_ID_PROVEEDOR))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return

    proveedor = obtener_proveedor(id_proveedor)

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    correo = input("Ingrese el nuevo correo: ").strip()

    if validar_correo_en_uso(correo):
        print("El correo ya fue registrado")
        return False
    
    telefono = input("Ingrese el nuevo telefono: ").strip()

    if validar_telefono_en_uso(telefono):
        print("El telefono ya fue registrado")
        return False

    return actualizar_proveedor(id_proveedor, correo, telefono)

def solicitar_actualizar_direccion_proveedor():
    try:
        id_proveedor = int(input(SOLICITUD_ID_PROVEEDOR))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return 

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        proveedor(MENSAJE_ID_NO_EXISTE)
        return

    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")

    return actualizar_direccion_proveedor(id_proveedor, calle, numero, comuna, ciudad)    

def solicitar_inhabilitar_proveedor():
    try:
        id_proveedor = int(input(SOLICITUD_ID_PROVEEDOR))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return 

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    return inhabilitar_proveedor(id_proveedor)

def solicitar_habilitar_proveedor():
    try:
        id_proveedor = int(input(SOLICITUD_ID_PROVEEDOR))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return 

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        proveedor(MENSAJE_ID_NO_EXISTE)
        return

    return habilitar_proveedor(id_proveedor)        
from negocio.negocio_proveedor import registrar_proveedor

# falta validar 
def solicitar_datos_proveedor():
    print("\n=== Datos del proveedor ===")
    rut = input("Ingrese el RUT del proveedor: ")
    nombre = input("Ingrese el nombre o razon social: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el telefono: ")

    """ Nota:
        cuando no consigue registrar al proveedor continua preguntado y se registra 
        la direccion aunque no registre proveedor"""
    
    print("\n=== Direccinn del proveedor ===")
    calle = input("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = input("Ingrese la comuna: ")
    ciudad = input("Ingrese la ciudad: ")
    return registrar_proveedor(
        rut, nombre, correo, telefono, 
        calle, numero, comuna, ciudad
    )
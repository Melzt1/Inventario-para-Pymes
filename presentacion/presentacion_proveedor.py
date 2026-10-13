from negocio.negocio_proveedor import lista_proveedores, registrar_proveedor, obtener_proveedor, validar_rut, actualizar_proveedor, actualizar_direccion_proveedor, inhabilitar_proveedor, habilitar_proveedor, rut_en_uso, correo_en_uso, telefono_en_uso
from auxiliares.mensajes import SOLICITUD_ID_PROVEEDOR, MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from prettytable import PrettyTable

def mostrar_proveedores():
    proveedores = lista_proveedores()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    tabla_proveedores = PrettyTable()
    tabla_proveedores.field_names = ['Id', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Id Direccion']

    for proveedor in proveedores:
        tabla_proveedores.add_row([
            proveedor.id_proveedor,
            proveedor.rut,
            proveedor.nombre,
            proveedor.correo,
            proveedor.telefono,
            ('Deshabilitado', 'Habilitado')[proveedor.estado],
            proveedor.id_direccion,
        ])

    print(tabla_proveedores)

def solicitar_datos_proveedor():
    print("\n=== Datos del proveedor ===")
    rut = campo_obligatorio("Ingrese el RUT del proveedor. Ej (12.345.678-5) : ")

    if not validar_rut(rut):
        print("El rut ingresado no es valido.")
        return False
    
    if rut_en_uso(rut):
        print("El rut ya fue registrado")
        return False

    nombre = campo_obligatorio("Ingrese el nombre o razon social: ")
    correo = campo_obligatorio("Ingrese el correo: ")

    if correo_en_uso(correo):
        print("El correo ya fue registrado.")
        return False

    telefono = campo_obligatorio("Ingrese el numero: ")

    if telefono_en_uso(telefono):
        print("El telefono ya fue registrado.")
        return False
    
    print("\n=== Direccion del proveedor ===")
    calle = campo_obligatorio("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = campo_obligatorio("Ingrese la comuna: ")
    ciudad = campo_obligatorio("Ingrese la ciudad: ")

    resultado = registrar_proveedor(rut, nombre, correo, telefono, 
        calle, numero, comuna, ciudad)
    print("Proveedor registrado con exito.") if resultado else print("No se pudo registrar el proveedor.")

def solicitar_consultar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    # La FK entrega el objeto Direccion, no el ID
    direccion = proveedor.id_direccion

    estado = "Habilitado" if proveedor.estado else "Deshabilitado"

    print("\n=== Proveedor encontrado ===")
    print(f"{'ID':<16}: {proveedor.id_proveedor}")
    print(f"{'RUT':<16}: {proveedor.rut}")
    print(f"{'Nombre':<16}: {proveedor.nombre}")
    print(f"{'Correo':<16}: {proveedor.correo}")
    print(f"{'Telefono':<16}: {proveedor.telefono}")
    print(f"{'Estado':<16}: {estado}")
    print(f"{'Direccion':<16}: {direccion.calle} {direccion.numero or '_'}, {direccion.comuna}, {direccion.ciudad}\n")

def solicitar_actualizar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)
    proveedor = obtener_proveedor(id_proveedor)

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    correo = campo_opcional("Ingrese el nuevo correo", proveedor.correo)

    if correo_en_uso(correo, id_proveedor):
        print("El correo ya fue registrado")
        return False
    
    telefono = campo_opcional("Ingrese el nuevo telefono", proveedor.telefono)

    if telefono_en_uso(telefono, id_proveedor):
        print("El telefono ya fue registrado")
        return False

    resultado = actualizar_proveedor(id_proveedor, correo, telefono)
    print("Proveedor actualizado con exito.") if resultado else print("No se pudo actualizar el proveedor.")

def solicitar_actualizar_direccion_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)
    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return
    
    direccion = proveedor.id_direccion
    calle = campo_opcional("Ingrese el nombre de la calle", direccion.calle)
    numero = campo_opcional("Ingrese el numero de la direccion", direccion.numero)
    comuna = campo_opcional("Ingrese la comuna", direccion.comuna)
    ciudad = campo_opcional("Ingrese la ciudad", direccion.ciudad)

    resultado = actualizar_direccion_proveedor(id_proveedor, calle, numero, comuna, ciudad)  
    print("Direccion de proveedor actualizada con exito.") if resultado else print("No se pudo actualizar la direccion.")

def solicitar_inhabilitar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    resultado = inhabilitar_proveedor(id_proveedor)
    print("Prveedor inhabilitado con exito.") if resultado else print("No se pudo inhabilitar el proveedor.")

def solicitar_habilitar_proveedor():
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    proveedor = obtener_proveedor(id_proveedor)   

    if proveedor is None:
        print(MENSAJE_ID_NO_EXISTE)
        return

    resultado = habilitar_proveedor(id_proveedor)     
    print("Prveedor habilitado con exito.") if resultado else print("No se pudo habilitar el proveedor.")
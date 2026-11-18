from prettytable import PrettyTable
from auxiliares.entradas import forzar_entero_positivo, campo_obligatorio, campo_opcional, actualizar_mantener_campo_texto
from auxiliares.validaciones import validar_rut, validar_correo, validar_telefono
from negocio.negocio_proveedor import (
    listar_proveedores_activos, 
    registrar_proveedor, 
    actualizar_proveedor, 
    actualizar_direccion_proveedor, 
    desactivar_proveedor, 
    activar_proveedor, 
    rut_en_uso, correo_en_uso, 
    telefono_en_uso, 
    buscar_proveedores,
    listar_proveedores_desactivados
)

# Metodo auxiliar que recibe una lista y escoge un proveedor
def seleccionar_proveedor(proveedores):
    if not proveedores:
        print("No hay proveedores registrados")
        return None 

    print(f"\n{len(proveedores)} proveedores encontrados:")
    for i, proveedor in enumerate(proveedores, start=1):
        print(f"[{i}] {proveedor.nombre} ({proveedor.rut})")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero_positivo("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(proveedores):
            opcion_valida = True
            return proveedores[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(proveedores)}).")

# Metodo auxiliares para reducir cognitive complexity
def leer_rut_opcional():
    valido = False
    while not valido:
        rut = campo_opcional("Ingrese el RUT del proveedor. Ej (12.345.678-5)")

        # campo_opcional devuelve el valor ingresado o None si ingresa un str vacio
        if rut is None:
            return None

        if not validar_rut(rut):
            print("El RUT ingresado no es valido. Intente nuevamente.")
            continue

        if rut_en_uso(rut):
            print("El RUT ya fue registrado. Ingrese otro.")
            continue

        valido = True

    return rut

def leer_correo_obligatorio():
    correo_valido = False
    while not correo_valido:
        correo = campo_obligatorio("Ingrese el correo: ")

        if not validar_correo(correo):
            print("El correo ingresado no es valido. Intente nuevamente.")
            continue

        if correo_en_uso(correo):
            print("El correo ya fue registrado. Ingrese otro.")
            continue

        correo_valido = True

    return correo

def leer_telefono_opcional():
    telefono_valido = False
    while not telefono_valido:
        telefono = campo_opcional("Ingrese el telefono, por ejemplo '+56912345678'")

        if telefono is None:
            return None
        
        if not validar_telefono(telefono):
            print("El teléfono debe contener entre 8 y 15 digitos.")
            continue

        if telefono_en_uso(telefono):
            print("El teléfono ya fue registrado. Ingrese otro.")
            continue

        telefono_valido = True
    return telefono    

def mostrar_proveedores():
    proveedores = listar_proveedores_activos()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    tabla_proveedores = PrettyTable()
    tabla_proveedores.field_names = ['Id', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Id Direccion']

    for proveedor in proveedores:
        tabla_proveedores.add_row([
            proveedor.id_proveedor,
            (proveedor.rut or '_'),
            proveedor.nombre,
            proveedor.correo,
            (proveedor.telefono or 'Sin registrar'),
            ('Deshabilitado', 'Habilitado')[proveedor.estado],
            proveedor.id_direccion,
        ])

    print(tabla_proveedores)
    

def solicitar_datos_proveedor():
    print("\n=== Registrar proveedor ===")

    rut = leer_rut_opcional()
    nombre = campo_obligatorio("Ingrese el nombre o razon social: ")
    correo = leer_correo_obligatorio()
    telefono = leer_telefono_opcional()

    print("\n=== Direccion del proveedor ===")
    calle = campo_obligatorio("Ingrese el nombre de la calle: ")
    numero = campo_opcional("Ingrese el numero de la direccion: ")
    comuna = campo_opcional("Ingrese la comuna")
    ciudad = campo_obligatorio("Ingrese la ciudad: ")

    resultado = registrar_proveedor(rut, nombre, correo, telefono, calle, numero, comuna, ciudad)
    print(f"Proveedor(a) '{nombre}' registrado con exito.") if resultado else print("No se pudo registrar el proveedor.")

def solicitar_consultar_proveedor():
    nombre = campo_obligatorio("Ingrese el nombre del proveedor: ")
    proveedor = seleccionar_proveedor(buscar_proveedores(nombre))

    if proveedor is None:
        return

    # La FK entrega el objeto Direccion
    direccion = proveedor.id_direccion

    estado = "Habilitado" if proveedor.estado else "Deshabilitado"

    print("\n=== Datos Proveedor ===")
    #print(f"{'ID':<16}: {proveedor.id_proveedor}")
    print(f"{'RUT':<16}: {proveedor.rut or '_'}")
    print(f"{'Nombre':<16}: {proveedor.nombre}")
    print(f"{'Correo':<16}: {proveedor.correo}")
    print(f"{'Telefono':<16}: {proveedor.telefono or 'No registrado'}")
    print(f"{'Estado':<16}: {estado}")
    print(f"{'Direccion':<16}: {direccion.calle} {direccion.numero or '_'}, {direccion.comuna or '_'}, {direccion.ciudad}\n")

def solicitar_actualizar_proveedor():   
    proveedor = seleccionar_proveedor(listar_proveedores_activos())

    if proveedor is None:
        return

    correo = actualizar_mantener_campo_texto("Ingrese el nuevo correo", proveedor.correo)

    if correo != proveedor.correo:
        if not validar_correo(correo):
            print("El correo ingresado no es valido.")
            return False
        
        if correo_en_uso(correo, proveedor.id_proveedor):
            print("El correo ya fue registrado")
            return False
    
    telefono = actualizar_mantener_campo_texto("Ingrese el nuevo telefono", proveedor.telefono)

    if telefono != proveedor.telefono:
        if telefono_en_uso(telefono, proveedor.id_proveedor):
            print("El telefono ya fue registrado")
            return False

    resultado = actualizar_proveedor(proveedor, correo, telefono)
    print("Proveedor actualizado con exito.") if resultado else print("No se pudo actualizar el proveedor.")

def solicitar_actualizar_direccion_proveedor():
    proveedor = seleccionar_proveedor(listar_proveedores_activos())

    if proveedor is None:
        return
    
    direccion = proveedor.id_direccion

    calle = actualizar_mantener_campo_texto("Ingrese el nombre de la calle", direccion.calle)
    numero = actualizar_mantener_campo_texto("Ingrese el numero de la direccion", direccion.numero)
    comuna = actualizar_mantener_campo_texto("Ingrese la comuna", direccion.comuna)
    ciudad = actualizar_mantener_campo_texto("Ingrese la ciudad", direccion.ciudad)

    resultado = actualizar_direccion_proveedor(proveedor, calle, numero, comuna, ciudad)  
    print("Direccion de proveedor actualizada con exito.") if resultado else print("No se pudo actualizar la direccion.")

def solicitar_desactivar_proveedor():
    proveedor = seleccionar_proveedor(listar_proveedores_activos())

    if proveedor is None:
        return

    resultado = desactivar_proveedor(proveedor)
    print("Prveedor inhabilitado con exito.") if resultado else print("No se pudo inhabilitar el proveedor.")

def solicitar_activar_proveedor():
    proveedor = seleccionar_proveedor(listar_proveedores_desactivados())

    if proveedor is None:
        return
    resultado =activar_proveedor(proveedor)
    print(f"Proveedor '{proveedor.nombre}' activado.") if resultado else print("No se pudo activar el proveedor.")
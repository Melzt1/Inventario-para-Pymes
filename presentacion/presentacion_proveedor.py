from prettytable import PrettyTable
from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from negocio.negocio_proveedor import (
    listar_proveedores_activos, 
    registrar_proveedor, 
    validar_rut, 
    actualizar_proveedor, 
    actualizar_direccion_proveedor, 
    desactivar_proveedor, 
    activar_proveedor, 
    rut_en_uso, correo_en_uso, 
    telefono_en_uso, 
    buscar_proveedores,
    listar_proveedores_desactivados
)

# Metodo auxiliar que se reciclara para mostrar proveedores por nombre
# NO ES PARTE DEL MENU
def solicitar_seleccion_proveedor():
    nombre = campo_obligatorio("Busque el proveedor por nombre: ")

    proveedores = list(buscar_proveedores(nombre))

    if not proveedores:
        print("No hay proveedores activos con ese nombre.")
        return None

    # Si hay una sola coincidencia retorno directo el proveedor, seria absurdo hacer elegir si solo hay una opcion
    if len(proveedores) == 1:
        print(f"Proveedor encontrado: {proveedores[0].nombre} ({proveedores[0].rut})")
        return proveedores[0]

    print(f"\n{len(proveedores)} proveedores encontrados:")
    for i, proveedor in enumerate(proveedores, start=1):
        print(f"[{i}] {proveedor.nombre} ({proveedor.rut})")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(proveedores):
            opcion_valida = True
            return proveedores[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(proveedores)}).")

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
            proveedor.rut,
            proveedor.nombre,
            proveedor.correo,
            proveedor.telefono,
            ('Deshabilitado', 'Habilitado')[proveedor.estado],
            proveedor.id_direccion,
        ])

    print(tabla_proveedores)

def solicitar_datos_proveedor():
    print("\n=== Registrar proveedor ===")

    rut_valido = False
    while not rut_valido:
        rut = campo_obligatorio("Ingrese el RUT del proveedor. Ej (12.345.678-5): ")

        if not validar_rut(rut):
            print("El RUT ingresado no es valido. Intente nuevamente.")
            continue

        if rut_en_uso(rut):
            print("El RUT ya fue registrado. Ingrese otro.")
            continue

        rut_valido = True

    nombre = campo_obligatorio("Ingrese el nombre o razon social: ")

    correo_valido = False
    while not correo_valido:
        correo = campo_obligatorio("Ingrese el correo: ")

        if correo_en_uso(correo):
            print("El correo ya fue registrado. Ingrese otro.")
            continue

        correo_valido = True

    telefono_valido = False
    while not telefono_valido:
        telefono = campo_obligatorio("Ingrese el numero incluyendo el 9 (9 digitos): ")

        # Comprobar que sean 9 digitos (Falta comprobar que el primer digito sea un 9)
        if not telefono.isdigit() or len(telefono) != 9:
            print("El teléfono debe contener exactamente 9 dígitos.")
            continue

        if telefono_en_uso(telefono):
            print("El teléfono ya fue registrado. Ingrese otro.")
            continue

        telefono_valido = True
    
    print("\n=== Direccion del proveedor ===")
    calle = campo_obligatorio("Ingrese el nombre de la calle: ")
    numero = input("Ingrese el numero de la direccion: ")
    comuna = campo_obligatorio("Ingrese la comuna: ")
    ciudad = campo_obligatorio("Ingrese la ciudad: ")

    resultado = registrar_proveedor(rut, nombre, correo, telefono, 
        calle, numero, comuna, ciudad)
    print(f"Proveedor(a) '{nombre}' registrado con exito.") if resultado else print("No se pudo registrar el proveedor.")

def solicitar_consultar_proveedor():
    proveedor = solicitar_seleccion_proveedor()

    if proveedor is None:
        return

    # La FK entrega el objeto Direccion
    direccion = proveedor.id_direccion

    estado = "Habilitado" if proveedor.estado else "Deshabilitado"

    print("\n=== Datos Proveedor ===")
    #print(f"{'ID':<16}: {proveedor.id_proveedor}")
    print(f"{'RUT':<16}: {proveedor.rut}")
    print(f"{'Nombre':<16}: {proveedor.nombre}")
    print(f"{'Correo':<16}: {proveedor.correo}")
    print(f"{'Telefono':<16}: {proveedor.telefono}")
    print(f"{'Estado':<16}: {estado}")
    print(f"{'Direccion':<16}: {direccion.calle} {direccion.numero or '_'}, {direccion.comuna}, {direccion.ciudad}\n")

def solicitar_actualizar_proveedor():   
    proveedor = solicitar_seleccion_proveedor()

    if proveedor is None:
        return

    id_proveedor = proveedor.id_proveedor
    correo = campo_opcional("Ingrese el nuevo correo", proveedor.correo)

    if correo_en_uso(correo, id_proveedor):
        print("El correo ya fue registrado")
        return False
    
    telefono = campo_opcional("Ingrese el nuevo telefono", proveedor.telefono)

    if telefono_en_uso(telefono, id_proveedor):
        print("El telefono ya fue registrado")
        return False

    resultado = actualizar_proveedor(proveedor, correo, telefono)
    print("Proveedor actualizado con exito.") if resultado else print("No se pudo actualizar el proveedor.")

def solicitar_actualizar_direccion_proveedor():
    proveedor = solicitar_seleccion_proveedor()

    if proveedor is None:
        return
    
    direccion = proveedor.id_direccion

    calle = campo_opcional("Ingrese el nombre de la calle", direccion.calle)
    numero = campo_opcional("Ingrese el numero de la direccion", direccion.numero)
    comuna = campo_opcional("Ingrese la comuna", direccion.comuna)
    ciudad = campo_opcional("Ingrese la ciudad", direccion.ciudad)

    resultado = actualizar_direccion_proveedor(proveedor, calle, numero, comuna, ciudad)  
    print("Direccion de proveedor actualizada con exito.") if resultado else print("No se pudo actualizar la direccion.")

def solicitar_desactivar_proveedor():
    proveedor = solicitar_seleccion_proveedor()

    if proveedor is None:
        return

    resultado = desactivar_proveedor(proveedor)
    print("Prveedor inhabilitado con exito.") if resultado else print("No se pudo inhabilitar el proveedor.")

def solicitar_activar_proveedor():
    proveedores = listar_proveedores_desactivados()

    if not proveedores:
        print("No hay proveedores desactivados.")
        return

    print("\nProveedores desactivados:")
    for i, proveedor in enumerate(proveedores, start=1):
        print(f"[{i}] - {proveedor.nombre} ({proveedor.rut})")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione el proveedor: ")

        if 1 <= seleccion <= len(proveedores):
            opcion_valida = True
            proveedor = proveedores[seleccion - 1]
        else:
            print(f"Opcion fuera de rango (1-{len(proveedores)}).")

    resultado = activar_proveedor(proveedor)
    print(f"Proveedor '{proveedor.nombre}' activado.") if resultado else print("No se pudo activar el proveedor.")
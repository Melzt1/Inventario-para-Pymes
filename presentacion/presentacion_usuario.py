from auxiliares.validaciones import validar_contrasena
from auxiliares.entradas import (
    campo_obligatorio, 
    campo_opcional,
    forzar_entero_positivo
)
from negocio.negocio_usuario import (
    registrar_usuario,
    actualizar_usuario,
    actualizar_contrasena,
    activar_usuario,
    desactivar_usuario,
    existe_nombre_usuario
)
from datos.repositorios.repositorio_rol import listar_roles
from negocio.negocio_almacen import listar_almacenes_activos

def seleccionar_elemento(elementos, mensaje):
    if not elementos:
        print(f"No hay {mensaje} registrados.")
        return None

    print(f"\n{mensaje} disponibles:")
    for i, elemento in enumerate(elementos, start=1):
        print(f"[{i}] - {elemento.nombre}")    

    opcion_valida = False

    while not opcion_valida:
        seleccion = forzar_entero_positivo("\nSeleccione: ")

        if 1 <= seleccion <= len(elementos):
            opcion_valida = True
            return elementos[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(elementos)}).")

def leer_nombre_usuario():
    valido = False

    while not valido:
        nombre_usuario = campo_obligatorio("Nombre de usuario: ").strip()

        if existe_nombre_usuario(nombre_usuario):
            print("El nombre de usuario ya se encuentra en uso. Elige otro.")
            continue

        valido = True

    return nombre_usuario     
 
def leer_contrasena():
    valido = False

    while not valido:
        contrasena = campo_obligatorio("Contrasena: ")

        errores = validar_contrasena(contrasena)

        if len(errores) > 0:
            print("\nErrores en tu contrasena:")
            for error in errores:
                print("-", error)
            continue

        confirmacion = input("Repita la contrasena: ")

        if contrasena != confirmacion:
            print("Las contrasenas no coinciden.")
            continue

        valido = True

    return contrasena
    
def solicitar_datos_usuario():
    print("\n=== Registrar usuario ===")

    nombre = campo_obligatorio("Nombre completo: ")
    nombre_usuario = leer_nombre_usuario()
    contrasena = leer_contrasena() # la contrasena se hasheara en la capa de negocio

    rol = seleccionar_elemento(listar_roles(), "roles")
    if rol is None:
        return
    
    almacen = seleccionar_elemento(listar_almacenes_activos(), "almacenes")
    if almacen is None:
        return

    resultado = registrar_usuario(nombre, nombre_usuario, contrasena, rol, almacen)
    print("Usuario registrado con exito") if resultado else print("No se pudo registrar el usuario.")

    



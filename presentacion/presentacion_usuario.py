from prettytable import PrettyTable

from auxiliares.validaciones import validar_contrasena
from auxiliares.entradas import (
    campo_obligatorio, 
    forzar_entero_positivo,
    actualizar_mantener_campo_texto,
    solicitar_confirmacion
)
from negocio.negocio_usuario import (
    registrar_usuario,
    listar_usuarios_activos,
    listar_usuarios_inactivos,
    actualizar_usuario,
    actualizar_contrasena,
    activar_usuario,
    desactivar_usuario,
    existe_nombre_usuario
)
from negocio.negocio_usuario import listar_roles

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
    
def solicitar_datos_usuario(): # REGISTRAR
    print("\n=== Registrar usuario ===")

    nombre = campo_obligatorio("Nombre completo: ")
    nombre_usuario = leer_nombre_usuario()
    contrasena = leer_contrasena() # la contrasena se hashea en la capa de negocio

    rol = seleccionar_elemento(listar_roles(), "roles")
    if rol is None:
        return

    resultado = registrar_usuario(nombre, nombre_usuario, contrasena, rol)
    print("Usuario registrado con exito") if resultado else print("No se pudo registrar el usuario.")

def mostrar_usuarios(): # LISTADO DE USUARIOS
    usuarios = listar_usuarios_activos()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['ID', 'Nombre', 'Usuario', 'Rol', 'Estado', 'Fecha creacion']

    for usuario in usuarios:
        tabla_usuarios.add_row([
            usuario.id_usuario,
            usuario.nombre,
            usuario.usuario,
            usuario.id_rol.nombre,
            ('Deshabilitado', 'Habilitado')[usuario.estado],
            usuario.fecha_creacion
        ])
    print(tabla_usuarios)        

def solicitar_actualizar_usuario(): 
    print("\n=== Actualizar usuario ===")

    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")

    if usuario is None:
        return
    
    nombre = actualizar_mantener_campo_texto("Nuevo nombre", usuario.nombre)
    nombre_usuario = actualizar_mantener_campo_texto("Nuevo nombre usuario", usuario.usuario)

    if nombre_usuario != usuario.usuario and existe_nombre_usuario(nombre_usuario, usuario.id_usuario):
        print(f"El usuarrio '{nombre_usuario}' ya esta en uso")
        return

    confirmar = solicitar_confirmacion(f"Deseas cambiar el rol? - Rol actual: '{usuario.id_rol.nombre}' ")
    if not confirmar:
        rol = usuario.id_rol
    else:
        rol = seleccionar_elemento(listar_roles(), "roles")
        if rol is None:
            return       
    
    resultado = actualizar_usuario(usuario, nombre, nombre_usuario, rol)        
    print("Usuario actualizado con exito.") if resultado else print("No se pudo actualizar el usuario.")

def solicitar_desactivar_usuario():
    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")
    if usuario is None:
        return

    if not solicitar_confirmacion(f"Desactivar al usuario '{usuario.usuario}'?"):
        return

    resultado = desactivar_usuario(usuario)
    print("Usuario desactivado.") if resultado else print("No se pudo desactivar.")

def solicitar_activar_usuario():
    usuario = seleccionar_elemento(listar_usuarios_inactivos(), "usuarios desactivados")
    if usuario is None:
        return

    resultado = activar_usuario(usuario)
    print("Usuario activado.") if resultado else print("No se pudo activar el usuario.")    

def solicitar_cambiar_contrasena():
    print("\n=== Actualizar contrasena ===")

    usuario = seleccionar_elemento(listar_usuarios_activos(), "usuarios")
    if usuario is None:
        return

    contrasena = leer_contrasena()

    resultado = actualizar_contrasena(usuario, contrasena)
    print("Contrasena actualizada correctamente.") if resultado else print("No se pudo actualizar la contrasena.")    
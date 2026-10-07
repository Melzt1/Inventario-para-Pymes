from negocio.negocio_categoria import crear_categoria, actualizar_categoria, obtener_categoria, desactivar_categoria, activar_categoria
from auxiliares.mensajes import SOLICITUD_ID_CATEGORIA, MENSAJE_ID_ENTERO, MENSAJE_CATEGORIA_NO_EXISTE

def solicitar_datos_categoria():
    nombre = descripcion = ""

    while nombre == "":
        nombre = input("Ingrese el nombre de la categoria: ")
    while descripcion == "":    
        descripcion = input("Ingrese la descripion de la categoria: ")

    return crear_categoria(nombre, descripcion)

def solicitar_actualizar_categoria():
    try:
        id_categoria = int(input(SOLICITUD_ID_CATEGORIA))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return

    # Buscamos la categoria por su ID
    # Si existe, obtenemos el objeto Categoria y si no existe obtenemos None
    categoria = obtener_categoria(id_categoria)

    # Si no encontro la categoria se detiene la funcion actual
    if categoria is None:
        print(MENSAJE_CATEGORIA_NO_EXISTE)
        return 

    nombre = input("Ingrese el nombre de la categoria: ")   
    descripcion = input("Ingrese la descripion de la categoria: ")

    return actualizar_categoria(id_categoria, nombre, descripcion) 

def solicitar_desactivar_categoria():
    try:
        id_categoria = int(input(SOLICITUD_ID_CATEGORIA))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_CATEGORIA_NO_EXISTE)
        return 

    confirmar = input(f"Estas seguro de desactivar la categoria: {categoria.nombre}? (S/N): ").strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(id_categoria)
        if resultado:
            print(f"Categoria '{categoria.nombre}' desactivada con exito.")
        else:
            print("No se pudo desactivar la categoría.")
    elif confirmar == "N":
        print("Opcion Cancelada.")
    else:
        print("Opcion invalida.") 

def solicitar_activar_categoria():
    try:
        id_categoria = int(input(SOLICITUD_ID_CATEGORIA))
    except ValueError:
        print(MENSAJE_ID_ENTERO)
        return

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_CATEGORIA_NO_EXISTE)
        return 

    return activar_categoria(id_categoria)
                    
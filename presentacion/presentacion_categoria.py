from negocio.negocio_categoria import crear_categoria, actualizar_categoria, obtener_categoria, desactivar_categoria, activar_categoria
from auxiliares.mensajes import SOLICITUD_ID_CATEGORIA, MENSAJE_ID_NO_EXISTE, OPCION_INVALIDA
from auxiliares.entradas import forzar_entero, mostrar_resultado, campo_obligatorio, campo_opcional
from prettytable import PrettyTable

def solicitar_datos_categoria():
    nombre = campo_obligatorio("Ingrese el nombre de la categoria: ")
    descripcion = campo_obligatorio("Ingrese la descripion de la categoria: ")

    resultado = crear_categoria(nombre, descripcion)
    mostrar_resultado(resultado, "Categoria creada con exito.", "No se pudo crear la categoria.")

def solicitar_consultar_categoria():
    id_categoria = forzar_entero(SOLICITUD_ID_CATEGORIA)

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    tabla_categoria = PrettyTable()
    tabla_categoria.field_names = ['ID', 'Nombre', 'Descripcion', 'Estado']
    tabla_categoria.add_row([
        categoria.id_categoria,
        categoria.nombre,
        categoria.descripcion,
        ('Deshabilitado', 'Habilitado')[categoria.estado]
    ])
    print(tabla_categoria)

def solicitar_actualizar_categoria():
    id_categoria = forzar_entero(SOLICITUD_ID_CATEGORIA)

    # Buscamos la categoria por su ID
    # Si existe, obtenemos el objeto Categoria y si no existe obtenemos None
    categoria = obtener_categoria(id_categoria)

    # Si no encontro la categoria se detiene la funcion actual
    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return 

    nombre = campo_opcional("Ingrese el nuevo nombre", categoria.nombre)   
    descripcion = campo_opcional("Ingrese la nueva descripion", categoria.descripcion)

    resultado = actualizar_categoria(id_categoria, nombre, descripcion)
    mostrar_resultado(resultado, "Categoria actualizada con exito.", "No se pudo actualizar la categoria.") 

def solicitar_desactivar_categoria():
    id_categoria = forzar_entero(SOLICITUD_ID_CATEGORIA)

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return 

    confirmar = input(f"Estas seguro de desactivar la categoria: {categoria.nombre}? (S/N): ").strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(id_categoria)
        mostrar_resultado(resultado, f"Categoria: {categoria.nombre} desactivada con exito.", "No se pudo desactivar la categoria.")
    elif confirmar == "N":
        print("Opcion Cancelada.")
    else:
        print(OPCION_INVALIDA) 

def solicitar_activar_categoria():
    id_categoria = forzar_entero(SOLICITUD_ID_CATEGORIA)

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return 

    resultado = activar_categoria(id_categoria)
    mostrar_resultado(resultado, f"Categoria: {categoria.nombre} activada con exito.", "No se pudo activar la categoria.")    
                    
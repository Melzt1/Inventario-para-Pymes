from prettytable import PrettyTable

from auxiliares.entradas import forzar_entero, campo_obligatorio, campo_opcional
from auxiliares.mensajes import SOLICITUD_ID_CATEGORIA, MENSAJE_ID_NO_EXISTE, OPCION_INVALIDA
from negocio.negocio_categoria import (
    crear_categoria, 
    actualizar_categoria, 
    obtener_categoria, 
    desactivar_categoria, 
    activar_categoria, 
    listar_categorias_activas
)

# ------------ Funcion Auxiliar ------------

def solicitar_seleccion_categoria():
    categorias = list(listar_categorias_activas())

    if not categorias:
        print("No hay categorias activas registradas.")
        return None

    print("\nCategorias disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"[{i}] - {categoria.nombre}")

    opcion_valida = False
    while not opcion_valida:
        seleccion = forzar_entero("\nSeleccione la categoria: ")

        if 1 <= seleccion <= len(categorias):
            opcion_valida = True
            return categorias[seleccion - 1]

        print(f"Opcion fuera de rango (1-{len(categorias)}).")

def mostrar_categorias():
    categorias = listar_categorias_activas()

    if not categorias:
        print("No hay categorias registradas.")
        return

    tabla_categorias = PrettyTable()
    tabla_categorias.field_names = ['Id', 'Nombre', 'Descripcion', 'Estado']

    for categoria in categorias:
        tabla_categorias.add_row([
            categoria.id_categoria,
            categoria.nombre,
            categoria.descripcion,
            ('Deshabilitado', 'Habilitado')[categoria.estado],
        ])

    print(tabla_categorias)

def solicitar_datos_categoria():
    nombre = campo_obligatorio("Ingrese el nombre de la categoria: ")
    descripcion = campo_obligatorio("Ingrese la descripion de la categoria: ")

    resultado = crear_categoria(nombre, descripcion)
    print("Categoria creada con exito.") if resultado else print("No se pudo crear la categoria.")

def solicitar_consultar_categoria():
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 

    estado = "Habilitado" if categoria.estado else "Deshabilitado"

    print("\n=== Informacion Categoria ===")
    print(f"{'ID':<16}: {categoria.id_categoria}")
    print(f"{'Nombre':<16}: {categoria.nombre}")
    print(f"{'Descripcion':<16}: {categoria.descripcion}")
    print(f"{'Estado':<16}: {estado}\n")

def solicitar_actualizar_categoria():
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 
    
    nombre = campo_opcional("Ingrese el nuevo nombre", categoria.nombre)   
    descripcion = campo_opcional("Ingrese la nueva descripion", categoria.descripcion)

    resultado = actualizar_categoria(categoria.id_categoria, nombre, descripcion)
    print("Categoria actualizada con exito.") if resultado else print("No se pudo actualizar la categoria.")    

# Falta validar que no se pueda desactivar categorias con productos que tengan stock > 0
def solicitar_desactivar_categoria():
    categoria = solicitar_seleccion_categoria()

    if categoria is None:
        return 

    confirmar = input(f"Estas seguro de desactivar la categoria: {categoria.nombre}? (S/N): ").strip().upper()
    if confirmar == "S":
        resultado = desactivar_categoria(categoria.id_categoria)
        print(f"Categoria: {categoria.nombre} desactivada con exito.") if resultado else print("No se pudo desactivar la categoria.") 
    elif confirmar == "N":
        print("Opcion Cancelada.")
    else:
        print(OPCION_INVALIDA) 

# Falta mostrar la lista de las categorias Desactivadas
def solicitar_activar_categoria():
    id_categoria = forzar_entero(SOLICITUD_ID_CATEGORIA)

    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return 

    resultado = activar_categoria(id_categoria)
    print(f"Categoria: {categoria.nombre} activada con exito.") if resultado else print("No se pudo activar la categoria.")    
                    
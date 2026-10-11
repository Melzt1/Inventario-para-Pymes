from datos.modelos.almacen import Almacen
from datos.repositorios.repositorio_almacen import listado_almacenes, guardar_almacen, obtener_almacen_por_id
from datos.repositorios.repositorio_direccion import guardar_direcciones
from negocio.negocio_direccion import crear_direccion, actualizar_direccion
from prettytable import PrettyTable

def lista_almacenes():
    tabla_almacenes = PrettyTable()
    tabla_almacenes.field_names = ['Id', 'Nombre', 'Encargado', 'Estado', 'Id Direccion']

    almacenes = listado_almacenes()

    if not almacenes:
        print("No hay Almecenes registrados.")
        return

    for almacen in almacenes:
        tabla_almacenes.add_row([
            almacen.id_almacen,
            almacen.nombre,
            almacen.encargado,
            ('Deshabilitado', 'Habilitado')[almacen.estado],
            almacen.id_direccion
        ])
    print(tabla_almacenes)

def crear_almacen(nombre, encargado, calle, numero, comuna, ciudad):
    nuevo_almacen = Almacen()
    nuevo_almacen.nombre = nombre
    nuevo_almacen.encargado = encargado

    # asociar direccion (relacion entre entidades)
    nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)

    # Si no puede guardar direccion, devuelve False asi no intenta crear un proveedor sin direccion
    if not guardar_direcciones(nueva_direccion):
        return False

    # asignar al almacen el objeto Direccion
    nuevo_almacen.id_direccion = nueva_direccion
    return guardar_almacen(nuevo_almacen)

def obtener_almacen(id_almacen):
    return obtener_almacen_por_id(id_almacen)    

def actualizar_almacen(id_almacen, nombre, encagado):
    almacen = obtener_almacen_por_id(id_almacen)

    if almacen is None:
        return False

    almacen.nombre = nombre
    almacen.encargado = encagado
    return guardar_almacen(almacen)

def actualizar_direccion_almacen(id_almacen, calle, numero, comuna, ciudad):
    almacen = obtener_almacen_por_id(id_almacen)

    if almacen is None:
        return False

    # La relacion (clave foranea) hace que almacen.id_direccion entregue el objeto Direccion
    direccion = almacen.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)

def inhabilitar_almacen(id_almacen):
    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        return False

    almacen.estado = False
    return guardar_almacen(almacen)

def habilitar_almacen(id_almacen):
    almacen = obtener_almacen(id_almacen)

    if almacen is None:
        return False

    almacen.estado = True
    return guardar_almacen(almacen)


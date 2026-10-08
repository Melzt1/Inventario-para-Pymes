from datos.modelos.proveedor import Proveedor
from datos.repositorios.repositorio_proveedor import listado_proveedores, guardar_proveedores
from datos.repositorios.repositorio_direccion import guardar_direcciones
from negocio.negocio_direccion import crear_direccion, actualizar_direccion
from prettytable import PrettyTable

def lista_proveedores():
    tabla_proveedores = PrettyTable()
    tabla_proveedores.field_names(['Id', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Id Direccion'])

    proveedores = listado_proveedores()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    for proveedor in proveedores:
        tabla_proveedores.add_row[(
            proveedor.id_proveedor,
            proveedor.rut,
            proveedor.nombre,
            proveedor.correo,
            proveedor.telefono,
            ('Deshabilitado', 'Habilitado')[proveedor.estado],
            proveedor.id_direccion
        )]

    print(tabla_proveedores)

def registrar_proveedor(rut, nombre, correo, telefono, calle, numero, comuna, ciudad):
    nuevo_proveedor = Proveedor()
    nuevo_proveedor.rut = rut
    nuevo_proveedor.nombre = nombre
    nuevo_proveedor.correo = correo
    nuevo_proveedor.telefono = telefono

    # asociar direccion (relacion entre entidades)
    nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)

    # Intentar guardar direccion, si no puede devuelve False asi no intenta crear un proveedor sin direccion
    if not guardar_direcciones(nueva_direccion):
        return False 

    # asignar al proveedor el objeto Direccion
    nuevo_proveedor.id_direccion = nueva_direccion
    return guardar_proveedores(nuevo_proveedor)
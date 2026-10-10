from datos.modelos.proveedor import Proveedor
from datos.repositorios.repositorio_proveedor import listado_proveedores, guardar_proveedores, obtener_proveedor_por_id, existe_correo, existe_telefono, existe_rut
from datos.repositorios.repositorio_direccion import guardar_direcciones
from negocio.negocio_direccion import crear_direccion, actualizar_direccion
from prettytable import PrettyTable

def lista_proveedores():
    tabla_proveedores = PrettyTable()
    tabla_proveedores.field_names = ['Id', 'Rut', 'Nombre', 'Correo', 'Telefono', 'Estado', 'Id Direccion']

    proveedores = listado_proveedores()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    for proveedor in proveedores:
        tabla_proveedores.add_row([
            proveedor.id_proveedor,
            proveedor.rut,
            proveedor.nombre,
            proveedor.correo,
            proveedor.telefono,
            ('Deshabilitado', 'Habilitado')[proveedor.estado],
            proveedor.id_direccion])
    print(tabla_proveedores)

def validar_rut(rut):
    # Limpiar los caracteres del rut (puntos y guion) 
    rut_limpio = rut.replace(".", "").replace("-","")

    # obtener todos los digitos menos el DV
    rut_sin_dv = rut_limpio[:-1] 
    dv_original = rut_limpio[-1]

    multiplicador = 2
    suma = 0

    # reversed para invertir los digitos del rut
    for digito in reversed(rut_sin_dv):
        resultado = int(digito) * multiplicador # Hacemos un cast para poder multiplicar
        suma += resultado

        # Aumentamos 1 por cada iteracion hasta 7 y luego lo reseteamos
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # calcular el digito verificador
    resto = suma % 11
    dv_calculado = 11 - resto

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado  == 10:
        dv_calculado = "K" 
    else:
        dv_calculado = str(dv_calculado )  

    # retonar si coincide con el digito verificador orignal
    return dv_original == dv_calculado

# VALIDACIONES UNIQUE
def rut_en_uso(rut):
    return existe_rut(rut)

def correo_en_uso(correo):
    return existe_correo(correo)

def telefono_en_uso(telefono):
    return existe_telefono(telefono)

def registrar_proveedor(rut, nombre, correo, telefono, calle, numero, comuna, ciudad):
    if not validar_rut(rut):
        return False

    if rut_en_uso(rut):
        return False

    if correo_en_uso(correo):
        return False

    if telefono_en_uso(telefono):
        return False
    
    nuevo_proveedor = Proveedor()
    nuevo_proveedor.rut = rut
    nuevo_proveedor.nombre = nombre
    nuevo_proveedor.correo = correo
    nuevo_proveedor.telefono = telefono

    # asociar direccion (relacion entre entidades)
    nueva_direccion = crear_direccion(calle, numero, comuna, ciudad)

    # Si no puede guardar direccion, devuelve False asi no intenta crear un proveedor sin direccion
    if not guardar_direcciones(nueva_direccion):
        return False 

    # asignar al proveedor el objeto Direccion
    nuevo_proveedor.id_direccion = nueva_direccion
    return guardar_proveedores(nuevo_proveedor)

# Actualizar solo datos que pueden variar
def actualizar_proveedor(id_proveedor, correo, telefono):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    proveedor.correo = correo
    proveedor.telefono = telefono
    return guardar_proveedores(proveedor)    

def actualizar_direccion_proveedor(id_proveedor, calle, numero, comuna, ciudad):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    # La relacion (clave foranea) hace que proveedor.id_direccion entregue el objeto Direccion
    direccion = proveedor.id_direccion
    return actualizar_direccion(direccion, calle, numero, comuna, ciudad)

def inhabilitar_proveedor(id_proveedor):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    proveedor.estado = False
    return guardar_proveedores(proveedor)

def habilitar_proveedor(id_proveedor):
    proveedor = obtener_proveedor_por_id(id_proveedor)

    if proveedor is None:
        return False

    proveedor.estado = True
    return guardar_proveedores(proveedor)

def obtener_proveedor(id_almacen):
    return obtener_proveedor_por_id(id_almacen)
from negocio.negocio_producto import registrar_producto, sku_en_uso, obtener_producto, actualizar_producto, validar_precios_negativos
from negocio.negocio_categoria import obtener_categoria
from auxiliares.mensajes import MENSAJE_ID_NO_EXISTE, SOLICITUD_ID_PRODUCTO
from auxiliares.entradas import forzar_entero, mostrar_resultado, campo_obligatorio, campo_opcional
from datetime import datetime

""" FALTA CREAR METODO PARA VALIDAR FECHAS, VALIDAR QUE LOS PRECIOS SEAN POSITIVOS
    Y QUE EL PRECIO VENTA SEA MAYOR AL PRECIO COSTO """

def solicitar_datos_producto():
    nombre = campo_obligatorio("Ingrese el nombre del producto: ")
    sku = campo_obligatorio("Ingrese el SKU del producto: ")

    if sku_en_uso(sku):
        print(f"El SKU: '{sku}' ya fue registrado.")
        return False

    precio_costo = forzar_entero("Ingrese el precio costo del producto: ")
    precio_venta = forzar_entero("Ingrese el precio venta del producto: ")

    # METODO DE PRUEBA
    if not validar_precios_negativos(precio_costo, precio_venta):
        print("El precio debe ser positivo")
        return False

    descripcion = campo_obligatorio("Ingrese la descripcion del producto: ")

    fecha_elaboracion = input("Ingrese la fecha de elaboracion (DD-MM-YYYY): ")
    fecha_elaboracion = datetime.strptime(fecha_elaboracion, "%d-%m-%Y").date()

    fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD-MM-YYYY): ")
    fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d-%m-%Y").date()
    
    # Obtener el objeto Categoria por su ID para hacer la relacion
    id_categoria = forzar_entero("Ingrese la categoria (Ingrasar por ID):")
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, categoria)
    mostrar_resultado(resultado, "Producto registado con exito", "No se pudo registrar el producto.")

def solicitar_actualizar_producto():
    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    producto = obtener_producto(id_producto)

    if producto is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    nombre = campo_opcional("Ingrese el nuevo nombre", producto.nombre)
    sku = campo_opcional("Ingrese el nuevo SKU", producto.sku)

    # POR ALGUNA RAZON ESTA ESTUPIDEZ FUNCIONA XD
    if sku != producto.sku and sku_en_uso(sku, id_producto):
        print(f"El SKU '{sku}' ya se encuentra registrado.")
        return False
    
    # hacklife para admitir un String vacio al solicitar un INT
    precio_venta = input("Ingrese el nuevo precio de venta (ENTER para mantener): ")
    if precio_venta == "":
        precio_venta = producto.precio_venta
    else:
        precio_venta = int(precio_venta)        

    descripcion = campo_opcional("Ingrese la nueva descripcion", producto.descripcion) 

    resultado =  actualizar_producto(id_producto, nombre, sku, precio_venta, descripcion)
    mostrar_resultado(resultado, "Producto actualizado con exito.", "No se pudo actualizar el producto.")
    



from negocio.negocio_producto import registrar_producto, sku_en_uso
from negocio.negocio_categoria import obtener_categoria
from auxiliares.mensajes import MENSAJE_ID_NO_EXISTE
from auxiliares.entradas import forzar_entero, mostrar_resultado
from datetime import datetime

def solicitar_datos_producto():
    nombre = input("Ingrese el nombre del producto: ")
    sku = input("Ingrese el SKU del producto: ")

    if sku_en_uso(sku):
        print(f"El SKU: '{sku}' ya fue registrado.")
        return False

    precio_costo = forzar_entero("Ingrese el precio costo del producto: ")
    precio_venta = forzar_entero("Ingrese el precio venta del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")

    fecha_elaboracion = input("Ingrese la fecha de elaboracion (DD-MM-YYYY): ")
    fecha_elaboracion = datetime.strptime(fecha_elaboracion, "%d-%m-%Y").date()

    fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD-MM-YYYY), ENTER si no aplica: ").strip()

    # Obtener el objeto Categoria por su ID para hacer la relacion
    id_categoria = forzar_entero("Ingrese la categoria (Ingrasar por ID):")
    categoria = obtener_categoria(id_categoria)

    if categoria is None:
        print(MENSAJE_ID_NO_EXISTE)
        return False

    resultado = registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, categoria)
    mostrar_resultado(resultado, "Producto registado con exito", "No se pudo registrar el producto.")
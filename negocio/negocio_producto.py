from datos.repositorios.repositorio_producto import listado_productos, guardar_productos, obtener_producto_por_id, existe_sku
from datos.modelos.producto import Producto
from prettytable import PrettyTable

def lista_productos():
    tabla_productos = PrettyTable()
    tabla_productos.field_names = ['ID', 'Nombre', 'SKU', 'Precio Costo', 'Precio Venta', 'Descripcion', 'Fecha Elaboracion', 'Fecha Vencimiento', 'Estado', 'ID Categoria']

    productos = listado_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        tabla_productos.add_row([
            producto.id_producto,
            producto.nombre,
            producto.sku,
            producto.precio_costo,
            producto.precio_venta,
            producto.descripcion,
            producto.fecha_elaboracion,
            producto.fecha_vencimiento,
            ('Inhabilitado', 'Habilitado')[producto.estado],
            producto.id_categoria
        ])
    print(tabla_productos)

def registrar_producto(nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, id_categoria):
    nuevo_producto = Producto()
    nuevo_producto.nombre = nombre
    nuevo_producto.sku = sku
    nuevo_producto.precio_costo = precio_costo
    nuevo_producto.precio_venta =precio_venta
    nuevo_producto.descripcion = descripcion
    nuevo_producto.fecha_elaboracion = fecha_elaboracion
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    nuevo_producto.id_categoria = id_categoria
    return guardar_productos(nuevo_producto)

# Validacion Unique
def sku_en_uso(sku):
    return existe_sku(sku)


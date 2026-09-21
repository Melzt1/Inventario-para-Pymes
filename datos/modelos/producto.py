class Producto:
    def __init__(self, id_producto, nombre, sku, precio_costo, precio_venta, descripcion, fecha_elaboracion, fecha_vencimiento, estado):
        self.id_producto = id_producto
        self.nombre = nombre
        self.sku = sku
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.descripcion = descripcion
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        
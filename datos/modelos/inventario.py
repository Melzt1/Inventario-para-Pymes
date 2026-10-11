from peewee import ForeignKeyField, AutoField
from datos.modelos.almacen import Almacen
from datos.modelos.producto import Producto
from datos.modelos.stock import Stock
from datos.modelos.models import BaseModel

class Inventario(BaseModel):
    id_inventario = AutoField()
    id_almacen = ForeignKeyField(Almacen, field=Almacen.id_almacen, column_name="id_almacen")
    id_producto = ForeignKeyField(Producto, field=Producto.id_producto, column_name="id_producto")
    id_stock = ForeignKeyField(Stock, field=Stock.id_stock, column_name="id_stock")

    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto', 'id_almacen'), True),
        )
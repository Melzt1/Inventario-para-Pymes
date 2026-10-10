from peewee import Model, ForeignKeyField, AutoField
from datos.conexion import conectar_db
from datos.modelos.almacen import Almacen
from datos.modelos.producto import Producto
from datos.modelos.stock import Stock

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

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
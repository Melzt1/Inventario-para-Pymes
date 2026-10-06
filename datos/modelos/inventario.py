from peewee import Model, IntegerField, AutoField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Inventario(BaseModel):
    id_inventario = AutoField()
    id_almacen = IntegerField(index=True)
    id_producto = IntegerField()
    id_stock = IntegerField(unique=True)

    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto', 'id_almacen'), True),
        )
from peewee import ForeignKeyField, AutoField, IntegerField, SQL
from datos.modelos.seccion import Seccion
from datos.modelos.producto import Producto
from datos.modelos.models import BaseModel

class Inventario(BaseModel):
    id_inventario = AutoField()

    id_producto = ForeignKeyField(
        Producto, 
        field=Producto.id_producto, 
        column_name="id_producto"
    )    
    id_seccion = ForeignKeyField(
        Seccion, 
        field=Seccion.id_seccion, 
        column_name="id_seccion"
    )
    stock_actual = IntegerField(default=0)

    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto', 'id_seccion'), True),
        )

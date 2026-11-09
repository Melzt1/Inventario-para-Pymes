from peewee import IntegerField, ForeignKeyField, CompositeKey

from datos.modelos.models import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

class MinimoAlmacen(BaseModel):
    id_producto = ForeignKeyField(
        Producto, 
        field=Producto.id_producto, 
        column_name="id_producto"
    )
    id_almacen = ForeignKeyField(
        Almacen,
        field=Almacen.id_almacen,
        column_name="id_almacen"
    )

    stock_minimo = IntegerField() 

    class Meta:
        table_name = 'minimos_almacen'
        primary_key = CompositeKey('id_producto', 'id_almacen')


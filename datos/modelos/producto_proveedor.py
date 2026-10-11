from peewee import BooleanField, SQL, ForeignKeyField, CompositeKey
from datos.modelos.producto import Producto
from datos.modelos.proveedor import Proveedor
from datos.modelos.models import BaseModel

class ProductoProveedor(BaseModel):
    id_producto = ForeignKeyField(Producto, field=Producto.id_producto, column_name="id_producto")
    id_proveedor = ForeignKeyField(Proveedor, field=Proveedor.id_proveedor, column_name="id_proveedor")
    es_principal = BooleanField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'producto_proveedor'
        indexes = (
            (('id_producto', 'id_proveedor'), True),
        )
        primary_key = CompositeKey('id_producto', 'id_proveedor')
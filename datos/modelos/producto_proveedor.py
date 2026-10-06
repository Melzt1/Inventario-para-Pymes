from peewee import Model, BooleanField, SQL, IntegerField, CompositeKey
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class ProductoProveedor(BaseModel):
    es_principal = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)
    id_producto = IntegerField()
    id_proveedor = IntegerField(index=True)

    class Meta:
        table_name = 'producto_proveedor'
        indexes = (
            (('id_producto', 'id_proveedor'), True),
        )
        primary_key = CompositeKey('id_producto', 'id_proveedor')
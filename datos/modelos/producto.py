from peewee import CharField, BooleanField, SQL, DateField, IntegerField, AutoField, ForeignKeyField
from auxiliares.mensajes import defecto
from datos.modelos.categoria import Categoria
from datos.modelos.models import BaseModel

class Producto(BaseModel):
    id_producto = AutoField()
    nombre = CharField(max_length=50)
    sku = CharField(max_length=100, unique=True)
    precio_costo = IntegerField()
    precio_venta = IntegerField()
    descripcion = CharField()
    fecha_elaboracion = DateField(null=True)
    fecha_vencimiento = DateField(null=True)
    estado = BooleanField(constraints=[SQL(defecto)])

    id_categoria = ForeignKeyField(
        Categoria,
        field=Categoria.id_categoria,
        column_name="id_categoria"
    )

    class Meta:
        table_name = 'productos'        
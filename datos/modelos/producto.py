from peewee import Model, CharField, BooleanField, SQL, DateField, IntegerField, AutoField, ForeignKeyField
from datos.conexion import conectar_db
from auxiliares.mensajes import defecto
from datos.modelos.categoria import Categoria

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

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
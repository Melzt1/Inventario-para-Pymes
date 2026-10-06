from peewee import Model, CharField, BooleanField, SQL, DateField, IntegerField, AutoField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Producto(BaseModel):
    descripcion = CharField()
    estado = BooleanField(constraints=[SQL(defecto)])
    fecha_elaboracion = DateField(null=True)
    fecha_vencimiento = DateField(null=True)
    id_categoria = IntegerField(index=True)
    id_producto = AutoField()
    nombre = CharField(max_length=50)
    precio_costo = IntegerField()
    precio_venta = IntegerField()
    sku = CharField(max_length=100, unique=True)

    class Meta:
        table_name = 'productos'        
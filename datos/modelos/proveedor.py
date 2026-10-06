from peewee import Model, AutoField, BooleanField, CharField, IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Proveedor(BaseModel):
    correo = CharField(max_length=100, null=True, unique=True)
    estado = BooleanField(constraints=[SQL(defecto)])
    id_direccion = IntegerField(index=True)
    id_proveedor = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=12, unique=True)
    telefono = CharField(max_length=9, unique=True)

    class Meta:
        table_name = 'proveedores'        
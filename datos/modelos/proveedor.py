from peewee import Model, AutoField, BooleanField, SQL, CharField, ForeignKeyField
from datos.modelos.direccion import Direccion
from auxiliares.mensajes import defecto
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Proveedor(BaseModel):
    id_proveedor = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=50)
    correo = CharField(max_length=100, null=True, unique=True)
    telefono = CharField(max_length=9, unique=True)
    estado = BooleanField(constraints=[SQL(defecto)])
    id_direccion = ForeignKeyField(
        Direccion,
        field=Direccion.id_direccion,
        column_name="id_direccion"
    )

    class Meta:
        table_name = 'proveedores'        
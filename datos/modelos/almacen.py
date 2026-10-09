from peewee import Model, CharField, BooleanField, AutoField, ForeignKeyField, SQL
from auxiliares.mensajes import defecto
from datos.modelos.direccion import Direccion
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre = CharField(max_length=50)
    encargado = CharField(max_length=50)
    estado = BooleanField(constraints=[SQL(defecto)])
    id_direccion = ForeignKeyField(
        Direccion,
        field=Direccion.id_direccion,
        column_name="id_direccion"
    )

    class Meta:
        table_name = 'almacenes'    

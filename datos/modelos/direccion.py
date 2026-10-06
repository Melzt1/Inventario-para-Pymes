from peewee import Model, CharField, AutoField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Direccion(BaseModel):
    id_direccion = AutoField()
    calle = CharField(max_length=50)
    numero = CharField(max_length=10, null=True)
    ciudad = CharField(max_length=100)
    comuna = CharField(max_length=100)

    class Meta:
        table_name = 'direcciones'        
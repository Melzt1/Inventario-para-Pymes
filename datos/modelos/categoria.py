from peewee import Model, AutoField, CharField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    descripcion = CharField(max_length=255)

    class Meta:
        table_name = 'categorias'
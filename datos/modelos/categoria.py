from peewee import *
from datos.modelos.models import BaseModel

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    descripcion = CharField()

    class Meta:
        table_name = 'categorias'
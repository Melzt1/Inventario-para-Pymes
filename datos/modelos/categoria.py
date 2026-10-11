from peewee import AutoField, CharField, BooleanField, SQL
from auxiliares.mensajes import defecto
from datos.modelos.models import BaseModel

class Categoria(BaseModel):
    id_categoria = AutoField()
    nombre = CharField(max_length=50)
    descripcion = CharField(max_length=255)
    estado = BooleanField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'categorias'
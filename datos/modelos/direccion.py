from peewee import CharField, AutoField
from datos.modelos.models import BaseModel

class Direccion(BaseModel):
    id_direccion = AutoField()
    calle = CharField(max_length=50)
    numero = CharField(max_length=10, null=True)
    ciudad = CharField(max_length=100)
    comuna = CharField(max_length=100)

    class Meta:
        table_name = 'direcciones'        
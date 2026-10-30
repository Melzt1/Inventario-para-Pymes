from peewee import CharField, AutoField

from datos.modelos.models import BaseModel

class Rol(BaseModel):
    id_rol = AutoField()
    nombre = CharField(max_length=30, unique=True)

    class Meta:
        table_name = 'roles'    

from peewee import CharField, BooleanField, AutoField, ForeignKeyField, SQL
from auxiliares.mensajes import defecto
from datos.modelos.direccion import Direccion
from datos.modelos.models import BaseModel

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

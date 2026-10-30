from peewee import CharField, BooleanField, AutoField, ForeignKeyField, SQL, DeferredForeignKey
from auxiliares.mensajes import defecto
from datos.modelos.direccion import Direccion
from datos.modelos.models import BaseModel

from datos.modelos.usuario import Usuario

class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre = CharField(max_length=50)
    estado = BooleanField(constraints=[SQL(defecto)])
    id_direccion = ForeignKeyField(
        Direccion,
        field=Direccion.id_direccion,
        column_name="id_direccion"
    )

    # Se usa "DeferredForeignKey" por la dependencia circular entre las tablas
    id_encargado = DeferredForeignKey(
        Usuario,
        field=Usuario.id_usuario,
        column_name="id_encargado"
    )

    class Meta:
        table_name = 'almacenes'    

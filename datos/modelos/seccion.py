from peewee import CharField, AutoField, BooleanField, SQL, ForeignKeyField

from datos.modelos.models import BaseModel
from datos.modelos.almacen import Almacen
from auxiliares.mensajes import defecto

class Seccion(BaseModel):
    id_seccion = AutoField()
    nombre = CharField(max_length=50)
    codigo = CharField(max_length=50, unique=True)
    descripcion = CharField(max_length=255)
    estado = BooleanField(constraints=[SQL(defecto)])

    id_almacen = ForeignKeyField(
        Almacen,
        field=Almacen.id_almacen,
        column_name="id_almacen"
    )

    class Meta:
        table_name = 'secciones'
        indexes = (
            (('id_almacen', 'nombre'), True),
        )    

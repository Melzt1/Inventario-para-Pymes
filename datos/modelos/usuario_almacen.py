from peewee import BooleanField, SQL, ForeignKeyField, CompositeKey

from datos.modelos.models import BaseModel
from datos.modelos.usuario import Usuario
from datos.modelos.almacen import Almacen

class UsuarioAlmacen(BaseModel):
    id_usuario = ForeignKeyField(
        Usuario, 
        field=Usuario.id_usuario, 
        column_name="id_usuario"
    )
    id_almacen = ForeignKeyField(
        Almacen,
        field=Almacen.id_almacen,
        column_name="id_almacen"
    )

    es_encargado = BooleanField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'usuario_almacen'
        primary_key = CompositeKey('id_usuario', 'id_almacen')


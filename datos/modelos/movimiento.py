from peewee import IntegerField, CharField, DateTimeField, AutoField, SQL, ForeignKeyField
from datos.modelos.inventario import Inventario
from datos.modelos.models import BaseModel

class Movimiento(BaseModel):
    id_movimiento = AutoField()
    descripcion = CharField(null=True)
    cantidad = IntegerField()
    tipo = CharField()
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_inventario = ForeignKeyField(
        Inventario,
        field=Inventario.id_inventario,
        column_name="id_inventario"
    )
    
    class Meta:
        table_name = 'movimientos'
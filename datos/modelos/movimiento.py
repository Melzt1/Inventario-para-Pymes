from peewee import Model, IntegerField, CharField, DateTimeField, AutoField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Movimiento(BaseModel):
    id_movimiento = AutoField()
    descripcion = CharField(null=True)
    cantidad = IntegerField()
    tipo = CharField()
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_inventario = IntegerField(index=True)
    
    class Meta:
        table_name = 'movimientos'
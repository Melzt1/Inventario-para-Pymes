from peewee import Model, CharField, BooleanField, AutoField, IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database


class Almacen(BaseModel):
    id_almacen = AutoField()
    nombre = CharField(max_length=50)
    encargado = CharField(max_length=50)
    estado = BooleanField(constraints=[SQL(defecto)])
    id_direccion = IntegerField(index=True)

    class Meta:
        table_name = 'almacenes'    

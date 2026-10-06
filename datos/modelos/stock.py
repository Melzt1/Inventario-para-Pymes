from peewee import *
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Stock(BaseModel):
    id_stock = AutoField()
    stock_actual = IntegerField()
    stock_minimo = IntegerField()

    class Meta:
        table_name = 'stocks'

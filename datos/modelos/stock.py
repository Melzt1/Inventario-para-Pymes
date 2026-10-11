from peewee import AutoField, IntegerField
from datos.modelos.models import BaseModel

class Stock(BaseModel):
    id_stock = AutoField()
    stock_actual = IntegerField()
    stock_minimo = IntegerField()

    class Meta:
        table_name = 'stocks'

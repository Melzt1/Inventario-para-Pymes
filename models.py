from peewee import *

database = MySQLDatabase('sistema_pyme', **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'Usuario', 'password': 'Inacap.2026semestre2!'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Direcciones(BaseModel):
    calle = CharField(max_length=50)
    ciudad = CharField(max_length=100)
    comuna = CharField(max_length=100)
    id_direccion = AutoField()
    numero = CharField(max_length=10, null=True)

    class Meta:
        table_name = 'direcciones'

class Almacenes(BaseModel):
    encargado = CharField(max_length=50)
    estado = BooleanField(constraints=[SQL("DEFAULT 1")])
    id_almacen = AutoField()
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direcciones)
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'almacenes'

class Categorias(BaseModel):
    descripcion = CharField()
    id_categoria = AutoField()
    nombre = CharField(max_length=50)

    class Meta:
        table_name = 'categorias'

class Productos(BaseModel):
    descripcion = CharField()
    estado = BooleanField(constraints=[SQL("DEFAULT 1")])
    fecha_elaboracion = DateField(null=True)
    fecha_vencimiento = DateField(null=True)
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categorias)
    id_producto = AutoField()
    nombre = CharField(max_length=50)
    precio_costo = IntegerField()
    precio_venta = IntegerField()
    sku = CharField(max_length=100, unique=True)

    class Meta:
        table_name = 'productos'

class Stocks(BaseModel):
    id_stock = AutoField()
    stock_actual = IntegerField()
    stock_minimo = IntegerField()

    class Meta:
        table_name = 'stocks'

class Inventarios(BaseModel):
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacenes)
    id_inventario = AutoField()
    id_producto = ForeignKeyField(column_name='id_producto', field='id_producto', model=Productos)
    id_stock = ForeignKeyField(column_name='id_stock', field='id_stock', model=Stocks, unique=True)

    class Meta:
        table_name = 'inventarios'
        indexes = (
            (('id_producto', 'id_almacen'), True),
        )

class Movimientos(BaseModel):
    cantidad = IntegerField()
    descripcion = CharField(null=True)
    fecha = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_inventario = ForeignKeyField(column_name='id_inventario', field='id_inventario', model=Inventarios)
    id_movimiento = AutoField()
    tipo = CharField()

    class Meta:
        table_name = 'movimientos'

class Proveedores(BaseModel):
    correo = CharField(max_length=100, null=True, unique=True)
    estado = BooleanField(constraints=[SQL("DEFAULT 1")])
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direcciones)
    id_proveedor = AutoField()
    nombre = CharField(max_length=50)
    rut = CharField(max_length=12, unique=True)
    telefono = CharField(max_length=9, unique=True)

    class Meta:
        table_name = 'proveedores'

class ProductoProveedor(BaseModel):
    es_principal = BooleanField(constraints=[SQL("DEFAULT 0")])
    id_producto = ForeignKeyField(column_name='id_producto', field='id_producto', model=Productos)
    id_proveedor = ForeignKeyField(column_name='id_proveedor', field='id_proveedor', model=Proveedores)

    class Meta:
        table_name = 'producto_proveedor'
        indexes = (
            (('id_producto', 'id_proveedor'), True),
        )
        primary_key = CompositeKey('id_producto', 'id_proveedor')


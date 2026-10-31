from peewee import CharField, BooleanField, AutoField, ForeignKeyField, SQL, DateTimeField
from auxiliares.mensajes import defecto
from datos.modelos.models import BaseModel

from datos.modelos.rol import Rol
from datos.modelos.almacen import Almacen

class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    usuario = CharField(max_length=50, unique=True)
    contrasena = CharField(max_length=255)
    estado = BooleanField(constraints=[SQL(defecto)])
    fecha_creacion = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    id_rol = ForeignKeyField(
        Rol,
        field=Rol.id_rol,
        column_name="id_rol"
    )

    id_almacen = ForeignKeyField(
        Almacen,
        field=Almacen.id_almacen,
        column_name="id_almacen",
        null=True
    )
    
    class Meta:
        table_name = 'usuarios'    

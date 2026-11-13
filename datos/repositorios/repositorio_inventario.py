from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.inventario import Inventario
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen
from datos.modelos.seccion import Seccion

# ------------ Lectura ------------

# Obtiene todas las secciones con sus productos registrados en un Almacen
def listar_inventario_de_almacen(id_almacen):       
    return (Inventario
            .select(Inventario, Producto, Seccion, Almacen)
            .join(Producto)
            .switch(Inventario)
            .join(Seccion)
            .join(Almacen)
            .where(Seccion.id_almacen == id_almacen)
            .order_by(Seccion.nombre, Producto.nombre))  

# Obtiene todos los almacenes y secciones donde esta registrado un producto 
def listar_inventario_de_producto(id_producto):
    return (Inventario
            .select(Inventario, Seccion, Almacen)
            .join(Seccion)
            .join(Almacen)
            .where(Inventario.id_producto == id_producto)
            .order_by(Almacen.nombre, Seccion.nombre))

# Obtiene todas las secciones donde esta registrado un producto dentro de un almacen especifico
def listar_inventario_producto_almacen(id_producto, id_almacen):
    return (Inventario
            .select(Inventario, Seccion)
            .join(Seccion)
            .where((Inventario.id_producto == id_producto) & (Seccion.id_almacen == id_almacen)))

def obtener_inventario_por_id(id_inventario):
    return Inventario.get_or_none(Inventario.id_inventario == id_inventario)

# buscar un producto en una seccion especifico
def obtener_inventario(id_producto, id_seccion):
    return Inventario.get_or_none(
        (Inventario.id_producto == id_producto) &
        (Inventario.id_seccion == id_seccion))


# ------------ Escritura ------------

def guardar_inventario(inventario:Inventario):
    try:
        inventario.save()
        return True
    
    except IntegrityError as e:
        print(f"Integridad de la base de datos: {e}")
    except OperationalError as e:
        print(f"Error operativo: {e}")
    except DataError as e:  
        print(f"Error de validación de datos: {e}")
    except PeeweeException as e:
        print(f"Error general de Peewee: {e}")

    return False    











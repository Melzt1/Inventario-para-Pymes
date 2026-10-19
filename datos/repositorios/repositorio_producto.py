from peewee import IntegrityError, OperationalError, DataError, PeeweeException

from datos.modelos.producto import Producto

# ------------ Lectura ------------

# Todos los productos activos
def listar_productos():
    return Producto.select().where(Producto.estado == True)

# Productos desactivados, para poder reactivarlos
def listar_productos_desactivados():
    return Producto.select().where(Producto.estado == False)

def obtener_producto_por_id(id_producto):
    return Producto.get_or_none(Producto.id_producto == id_producto)

def obtener_producto_por_sku(sku):
    return Producto.get_or_none(Producto.sku == sku)

def buscar_productos_por_nombre(nombre):
    return Producto.select().where(Producto.nombre.contains(nombre))

# ------------ Escritura ------------

def guardar_producto(prodcuto:Producto):
    try:
        prodcuto.save()
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

# ------------ Validaciones UNIQUE ------------

# CONSULTA GENERADA POR DEEPSEEK (IA). YO NO PUDE RESOLVERLA :C 
# Al momento de hacer un UPDATE y mantener el SKU, se vuelve a setear el mismo SKU y da error por el UNIQUE

# La consulta pregunta si otro producto tiene ese SKU, excluyendo el SKU del producto actual.
def existe_sku(sku, id_producto = None):
    consulta = Producto.select().where(Producto.sku == sku)

    if id_producto is not None:
        consulta = consulta.where(Producto.id_producto != id_producto)

    return consulta.exists()    


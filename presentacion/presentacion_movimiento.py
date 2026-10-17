from negocio.negocio_movimiento import registrar_entrada, registrar_salida, lista_movimientos, validar_stock_salida, lista_movimientos_entrada, lista_movimientos_salida, lista_movimientos_rango_fecha
from auxiliares.entradas import campo_obligatorio, forzar_positivo, forzar_entero, forzar_fecha
from negocio.negocio_producto import obtener_producto_sku
from negocio.negocio_inventario import lista_producto_inventario
from prettytable import PrettyTable

"""
Para registrar un movimiento, pedire el SKU del producto y el almacen donde se realizara. 
Con esos datos obtendre los objetos Producto y Almacen, y buscare el Inventario (id_inventario) que los relaciona,
si existe, usare el id_inventario (FK) para guardar el movimiento,
asi el usuario no necesita conocer ni digitar el id_inventario, lo cual es cero intuitivo usando la terminal.

TODA ESTA LOGICA OCURRIRA GRACIAS A LOS METODOS DE LA CAPA DE NEGOCIO Y LOS OBJETOS CAPTURADOS, PD: TODAVIA LA EXTRANO :c
"""

def solicitar_registrar_entrada():
    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()

    # aca obtengo el objeto Producto por su sku
    producto = obtener_producto_sku(sku)
    if producto is None:
        print("No existe producto con ese SKU.")
        return False

    # obtengo el id_producto del objeto Producto conseguido anteriormente
    id_producto = producto.id_producto 

    # este metodo devuelve todos los inventarios con dicho producto
    # teniendo acceso al objeto Inventareio, tengo acceso al id_almacen (objeto Almacen)
    lista_inventario = lista_producto_inventario(id_producto)

    if not lista_inventario:
        print("El producto no esta asociado a ningun almacen.")
        return False
    
    print(f"Producto encontrado: {producto.nombre}")
    print("Almacenes con inventario para este producto:")
    # creo una lista para almacenar los objetos y luego compararlo con la respuesta "seleccion"
    opciones = []

    # dado que mi lista almacenara la cantidad de objetos (0,1,2,3,4......) usare enumerate
    # OJO: estoy almacenando el objeto NO el id_inventario
    for i, inventario in enumerate(lista_inventario, start=1):
        almacen = inventario.id_almacen
        print(f"[{i}] - {almacen.nombre} - Stock: {inventario.stock_actual}")
        opciones.append(inventario) 

    seleccion = forzar_entero("\nSeleccione el Almacen: ")

    if 1 <= seleccion <= len(opciones):
        inventario = opciones[seleccion-1]
        id_inventario = inventario.id_inventario
    else:
        print("Opcion fuera de rango.")
        return False
    
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")
    fecha = forzar_fecha("Ingrese la fecha (DD-MM-YYYY): ", obligatorio=True)

    resultado = registrar_entrada(descripcion, cantidad, fecha, id_inventario)
    print("Entrada registrada con exito.") if resultado else print("No se pudo realizar el movimiento")
        

def solicitar_registrar_salida():
    sku = campo_obligatorio("ingrese el SKU del producto: ").strip()

    producto = obtener_producto_sku(sku)
    if producto is None:
        print("No existe producto con ese SKU.")
        return False

    id_producto = producto.id_producto 
    lista_inventario = lista_producto_inventario(id_producto)

    if not lista_inventario:
        print("El producto no esta asociado a ningun almacen.")
        return False
    
    print(f"Producto encontrado: {producto.nombre}")
    print("Almacenes con inventario para este producto:")

    opciones = []

    for i, inventario in enumerate(lista_inventario, start=1):
        almacen = inventario.id_almacen
        print(f"[{i}] - {almacen.nombre} - Stock: {inventario.stock_actual}")
        opciones.append(inventario) 

    seleccion = forzar_entero("\nSeleccione el Almacen: ")

    if 1 <= seleccion <= len(opciones):
        inventario = opciones[seleccion-1]
        id_inventario = inventario.id_inventario
    else:
        print("Opcion fuera de rango.")
        return False

    if inventario.stock_actual == 0:
        print("No hay stock suficiente")
        return False
        
    descripcion = campo_obligatorio("Ingrese la descripcion: ")
    cantidad = forzar_positivo("Ingrese la cantidad: ")
    fecha = forzar_fecha("Ingrese la fecha (DD-MM-YYYY): ", obligatorio=True)

    if not validar_stock_salida(id_inventario, cantidad):
        print("El stock es insuficiente para esa salida.")
        return False
    
    resultado = registrar_salida(descripcion, cantidad, fecha, id_inventario)

    print("Salida registrada con exito.") if resultado else print("No se pudo realizar el movimiento")

def solicitar_consultar_movimiento():
    print("=== Consulta de Movimientos ===")
    opcion = campo_obligatorio("Ingrese el tipo de movimiento (ENTRADA/SALIDA): ").strip().upper()

    if opcion == "ENTRADA":
        movimientos = lista_movimientos_entrada()
    elif opcion == "SALIDA":
        movimientos = lista_movimientos_salida()
    else:
        print("Opción invaida. Por favor, escribe ENTRADA o SALIDA.\n")
        return

    if not movimientos:
        print("No hay movimientos registrados.")
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,   
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        

def mostrar_movimientos_rango_fecha():
    fecha_inicio = forzar_fecha("Ingrese la fecha de inicio (DD-MM-YYYY): ", obligatorio=True)
    fecha_termino = forzar_fecha("Ingrese la fecha de termino (DD-MM-YYYY): ", obligatorio=True)       

    if fecha_inicio > fecha_termino:
        print("La fecha de inicio no puede ser posterior a la fecha de termino.")
        return False
    
    movimientos = lista_movimientos_rango_fecha(fecha_inicio, fecha_termino)
    if not movimientos:
        print("No hay movimientos registrados.")
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        

def mostrar_historial_movimientos():
    movimientos = lista_movimientos()

    if not movimientos:
        print("No hay movimientos registrados.")
        return False

    tabla_movimiento = PrettyTable()
    tabla_movimiento.field_names = ['Fecha', 'Producto', 'Almacen', 'Tipo', 'Cantidad', 'Descripcion']

    for movimiento in movimientos:
        inventario = movimiento.id_inventario
        producto = inventario.id_producto
        almacen = inventario.id_almacen

        tabla_movimiento.add_row([
            movimiento.fecha,
            producto.nombre,
            almacen.nombre,
            movimiento.tipo,
            movimiento.cantidad,
            movimiento.descripcion,
        ])
    print(tabla_movimiento)        
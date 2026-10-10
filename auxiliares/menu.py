from auxiliares.mensajes import VOLVER_AL_MENU

menu_superior = {
    "1": "Gestión de categorías (Funcionando)",
    "2": "Gestión de proveedores (Funcionando)",
    "3": "Gestión de productos (En proceso)",
    "4": "Gestión de almacenes (Funcionando)",
    "5": "Gestión de inventario y movimientos (No hace nada)",
    "0": "Salir",
}

submenu_categoria = {
    "1": "Listar categorías",
    "2": "Guardar cateogria",
    "3": "Consultar categoria por ID",
    "4": "Actualizar cateogria",
    '5': "Desactivar categoria",
    '6': "Activar categoria",
    "0": VOLVER_AL_MENU
}

submenu_proveedor = {
    "1": "Listar proveedores",
    "2": "Registrar proveedor",
    "3": "Consultar proveedor por ID",
    "4": "Actualizar proveedor",
    "5": "Actualizar direccion proveedor",
    '6': "Desactivar proveedor",
    '7': "Activar proovedor",
    "0": VOLVER_AL_MENU
}

submenu_almacen = {
    "1": "Listar almacenes",
    "2": "Registrar almacen",
    "3": "Consultar almacen por ID",
    "4": "Actualizar almacen",
    "5": "Actualizar direccion almacen",
    '6': "Desactivar almacen",
    '7': "Activar almacen",
    "0": VOLVER_AL_MENU
}

submenu_producto = {
    "1": "Listar productos",
    "2": "Registrar producto",
    "3": "Consultar producto por ID",
    "4": "Actualizar producto",
    "5": "Asignar proveedor al producto",
    "6": "Desactivar producto",
    "7": "Activar producto",
    "8": "Consultar stock del producto",
    "0": VOLVER_AL_MENU
}
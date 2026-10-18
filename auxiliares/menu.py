from auxiliares.mensajes import VOLVER_AL_MENU

menu_superior = {
    "1": "Gestión de categorías",
    "2": "Gestión de proveedores",
    "3": "Gestión de productos",
    "4": "Gestión de almacenes",
    "5": "Gestión de inventario y movimientos",
    "0": "Salir",
}

submenu_categoria = {
    "1": "Listar categorías",
    "2": "Guardar cateogria",
    "3": "Consultar categoria por ID",
    "4": "Actualizar categoria",
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
    '7': "Activar proveedor",
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
    "3": "Consultar producto por nombre",
    "4": "Actualizar producto",
    "5": "Desactivar producto",
    '6': "Activar producto",  
    "7": "Gestión de relaciones producto-proveedor",
    "0": VOLVER_AL_MENU
}

submenu_producto_proveedor = {
    "1": "Asignar proveedor principal al producto",
    "2": "Asignar proveedor secundario al producto",
    "3": "Quitar proveedor al producto",
    "4": "Ver proveedores del producto",
    "0": "Volver al menu anterior"
}

submenu_inventario = {
    "1": "Asociar producto a un almacen",
    "2": "Consultar inventario de un producto en un almacen",
    "3": "Listar inventario de un almacen",
    "4": "Listar productos bajo stock minimo",
    "5": "Gestion de movimientos",    
    "0": VOLVER_AL_MENU
}

submenu_movimientos = {
    "1": "Registrar entrada de stock",
    "2": "Registrar salida de stock",
    "3": "Consultar movimientos por tipo",
    "4": "Consultar movimientos por rango de fecha",    
    "5": "Ver historial completo",
    "0": "Volver al menu anterior"
}
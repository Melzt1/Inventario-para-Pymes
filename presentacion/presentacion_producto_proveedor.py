from negocio.negocio_producto_proveedor import asignar_proveedor_principal, asignar_proveedor_secundario, eliminar_relacion

from auxiliares.entradas import forzar_entero, mostrar_resultado
from auxiliares.mensajes import SOLICITUD_ID_PRODUCTO, SOLICITUD_ID_PROVEEDOR


# FUNCION PARA TESTEAR, FALTA MUHCO
def solicitar_asignar_proveedor_principal():
    print("\n=== Asignar proveedor principal ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    resultado = asignar_proveedor_principal(id_producto, id_proveedor)
    mostrar_resultado(resultado, "Proveedor principal asignado con exito", "No se pudo asignar el proveedor")

""""    SE PODRIA CREAR UN SOLO METODO QUE PREGUNTE SI ES PRINCIPAL O SECUNDARIO
        PERO DE MOMENTO ES PARA TESTEAR     """

def solicitar_asignar_proveedor_secundario():
    print("\n=== Asignar proveedor secundario ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR)

    resultado = asignar_proveedor_secundario(id_producto, id_proveedor)
    mostrar_resultado(resultado, "Proveedor secundario asignado con exito", "No se pudo asignar el proveedor")    

def solicitar_quitar_proveedor():
    print("\n=== Quitar proveedor al producto ===")

    id_producto = forzar_entero(SOLICITUD_ID_PRODUCTO)
    id_proveedor = forzar_entero(SOLICITUD_ID_PROVEEDOR) 

    resultado = eliminar_relacion(id_producto, id_proveedor)
    mostrar_resultado(resultado, f"El proveedor con ID {id_proveedor} se quitó del producto con ID {id_producto}.", "No se pudo quitar el proveedor")               
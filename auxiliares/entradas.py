from datetime import datetime
from decimal import Decimal, InvalidOperation

from auxiliares.mensajes import (
    MENSAJE_ID_ENTERO,
    MENSAJE_NUMERO_DECIMAL,
    MENSAJE_NUMERO_POSITIVO,
    MENSAJE_MAXIMO_DECIMALES
)
from datetime import datetime

""" En este repositorio somos hater del while True!
    Si eres partidario del while True por favor sal de este repositorio """

def forzar_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print(MENSAJE_ID_ENTERO)
    return numero

def forzar_positivo(mensaje):
    valido = False
    while not valido:
        numero = forzar_entero(mensaje)
        if numero > 0:
            valido = True
        else:
            print("Debes ingresar un valor mayor que cero")
    return numero

def campo_obligatorio(mensaje):
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo es obligatorio!")
            continue
        valido = True
    return texto        

def campo_opcional(mensaje, valor_actual):
    valor_nuevo = input(f"{mensaje} (ENTER para mantener): ").strip()

    if valor_nuevo == "":
        return valor_actual
    return valor_nuevo

def forzar_fecha(mensaje, obligatorio=False):
    fecha_valida = False
    while not fecha_valida:
        texto = input(mensaje).strip()
        if texto == "":
            if obligatorio:
                print("La fecha es obligatoria.")
                continue
            return None
        try: 
            fecha = datetime.strptime(texto, "%d-%m-%Y").date()
            fecha_valida = True
        except ValueError:
            print("Ingrese una fecha válida con el formato DD-MM-YYYY.")   
    return fecha


def convertir_decimal_positivo(texto, decimales):
    try:
        numero = Decimal(texto.replace(",", "."))
    except InvalidOperation:
        print(MENSAJE_NUMERO_DECIMAL)
        return None

    if not numero.is_finite() or numero <= 0:
        print(MENSAJE_NUMERO_POSITIVO)
        return None
    if -numero.normalize().as_tuple().exponent > decimales:
        print(MENSAJE_MAXIMO_DECIMALES.format(decimales))
        return None
    return numero


def forzar_decimal_positivo(mensaje, decimales):
    numero = None
    while numero is None:
        numero = convertir_decimal_positivo(input(mensaje).strip(), decimales)
    return numero


def actualizar_decimal_positivo(mensaje, valor_actual, decimales):
    numero = None
    while numero is None:
        texto = input(f"{mensaje} (ENTER para mantener): ").strip()
        if texto == "":
            return valor_actual
        numero = convertir_decimal_positivo(texto, decimales)
    return numero                 
from datetime import datetime
from decimal import Decimal, InvalidOperation

from auxiliares.mensajes import MENSAJE_NUMERO_ENTERO, MENSAJE_NUMERO_DECIMAL, MENSAJE_MAYOR_QUE_CERO


""" En este repositorio somos hater del while True!
    Si eres partidario del while True por favor sal de este repositorio """

def forzar_entero_positivo(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                valido = True
            else:
                print(MENSAJE_MAYOR_QUE_CERO)          
        except ValueError:
            print(MENSAJE_NUMERO_ENTERO)
    return numero

# Entradas de decimales
def forzar_decimal_positivo(mensaje):
    valido = False

    while not valido:
        try:
            numero = Decimal(input(mensaje))
            if numero > 0:
                valido = True
            else:
                print(MENSAJE_MAYOR_QUE_CERO) 
        except InvalidOperation:
            print(MENSAJE_NUMERO_DECIMAL)
    return numero
    
# EntradaS NOT NULL
def campo_obligatorio(mensaje):
    valido = False
    while not valido:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo es obligatorio!")
            continue
        valido = True
    return texto        

def campo_opcional(mensaje):
    valor = input(f"{mensaje} (ENTER para omitir): ").strip()

    if valor == "":
        return None

    return valor

# Metodos auxiliares para retornar el valor actual o nuevo
def actualizar_mantener_campo_texto(mensaje, valor_actual):
    valor_nuevo = input(f"{mensaje} (ENTER para mantener): ").strip()

    if valor_nuevo == "":
        return valor_actual
    return valor_nuevo

def actualizar_mantener_campo_entero(mensaje, valor_actual):
    numero = None

    while numero is None:
        texto = input(f"{mensaje} (ENTER para mantener): ").strip()

        if texto == "":
            numero = valor_actual
        else:
            try:
                numero = int(texto)
            except ValueError:
                print(MENSAJE_NUMERO_ENTERO)

    return numero

def actualizar_mantener_campo_decimal(mensaje, valor_actual):
    numero = None

    while numero is None:
        texto = input(f"{mensaje} (ENTER para mantener): ").strip()

        if texto == "":
            numero = valor_actual
        else:
            try:
                numero = Decimal(texto)
            except InvalidOperation:
                print(MENSAJE_NUMERO_DECIMAL)

    return numero
                           

# ENTRADAS DATE

def forzar_fecha(mensaje, obligatorio=False):
    fecha = None

    while fecha is None:
        texto = input(mensaje).strip()

        if texto == "" and obligatorio:
            print("La fecha es obligatoria.")
            continue
        elif texto == "":
            return None

        try:
            fecha = datetime.strptime(texto, "%d-%m-%Y").date()
        except InvalidOperation:
            print("Ingrese una fecha válida con el formato DD-MM-YYYY.")

    return fecha


def solicitar_confirmacion(mensaje):
    respuesta_valida = False

    while not respuesta_valida:
        respuesta = input(f"{mensaje} (S/N): ").strip().upper()

        if respuesta == "S":
            return True
        elif respuesta == "N":
            return False
        else:
            print("Opción no válida. Ingrese S o N.")         
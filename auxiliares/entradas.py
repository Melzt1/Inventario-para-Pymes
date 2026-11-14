from auxiliares.mensajes import MENSAJE_NUMERO_ENTERO, MENSAJE_NUMERO_DECIMAL, MENSAJE_MAYOR_QUE_CERO
from datetime import datetime

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
            numero = float(input(mensaje))
            if numero > 0:
                valido = True
            else:
                print(MENSAJE_MAYOR_QUE_CERO) 
        except ValueError:
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
                numero = float(texto)
            except ValueError:
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
        except ValueError:
            print("Ingrese una fecha válida con el formato DD-MM-YYYY.")

    return fecha
         
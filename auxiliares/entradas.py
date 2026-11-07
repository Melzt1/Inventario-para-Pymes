from auxiliares.mensajes import MENSAJE_ID_ENTERO
from datetime import datetime

""" En este repositorio somos hater del while True!
    Si eres partidario del while True por favor sal de este repositorio """

# EntradaS de INT
def forzar_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print(MENSAJE_ID_ENTERO)
    return numero

# EntradaS de INT positivo
def forzar_positivo(mensaje):
    valido = False
    while not valido:
        numero = forzar_entero(mensaje)
        if numero > 0:
            valido = True
        else:
            print("Debes ingresar un valor mayor que cero")
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

# ENTRADAS NULL
def actualizar_mantener_campo_texto(mensaje, valor_actual):
    valor_nuevo = input(f"{mensaje} (ENTER para mantener): ").strip()

    if valor_nuevo == "":
        return valor_actual
    return valor_nuevo

def actualizar_mantener_campo_entero(mensaje, valor_actual):
    valido = False
    numero = valor_actual

    while not valido:
        texto = input(f"{mensaje} (ENTER para mantener): ").strip()

        if texto == "":
            valido = True
        else:
            try:
                numero = int(texto)
                valido = True
            except ValueError:
                print("Debe ingresar un número entero.")

    return numero

# ENTRADAS DATE
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
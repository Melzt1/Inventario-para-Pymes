from auxiliares.mensajes import MENSAJE_ID_ENTERO

def forzar_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print(MENSAJE_ID_ENTERO)
    return numero

def mostrar_resultado(resultado, mensaje_exitoso, mensaje_fallido):
    if resultado:
        print(mensaje_exitoso)
    else:
        print(mensaje_fallido)        

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
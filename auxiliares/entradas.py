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
import re

def validar_rut(rut):
    
    #strip para evitar que los espacios generen un error o bugs
    rut = rut.strip().replace(".", "").replace("-", "")
    
    if len(rut) < 2:
        return False
    
    numero_del_rut = rut[:-1]
    digito_verificador = rut[-1].upper()
    
    
    if not numero_del_rut.isdigit():
        return False
    
    suma = 0
    multiplicador = 2
    
    for i in reversed(range(len(numero_del_rut))):
        suma += int(numero_del_rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2 #Ternario
        
    digito_verificador_calculado = 11 - (suma % 11)
    
    if digito_verificador_calculado == 11:
        digito_verificador_calculado = '0'
    
    elif digito_verificador_calculado == 10:
        digito_verificador_calculado = 'K'
        
    return str(digito_verificador_calculado) == digito_verificador 


def validar_telefono(telefono):
    telefono = telefono.strip().replace(" ", "")
    return re.fullmatch(r"\+?\d{8,15}", telefono) is not None
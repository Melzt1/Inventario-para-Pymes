import re

def validar_rut(rut):
    # Limpiar los caracteres del rut (puntos y guion) 
    rut_limpio = rut.replace(".", "").replace("-","").upper()

    # Debe existir al menos un digito y un digito verificador
    if len(rut_limpio) < 2:
        return False
    
    # obtener todos los digitos menos el DV
    rut_sin_dv = rut_limpio[:-1] 

    # obtener solo el digito verficiador
    dv_original = rut_limpio[-1]

    # validar que sean digitos
    if not rut_sin_dv.isdigit() or dv_original not in "0123456789K":
        return False

    multiplicador = 2
    suma = 0

    # reversed para invertir los digitos del rut
    for digito in reversed(rut_sin_dv):
        resultado = int(digito) * multiplicador # Hacemos un cast para poder multiplicar
        suma += resultado

        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # calcular el digito verificador
    dv_calculado = 11 - (suma % 11)

    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado  == 10:
        dv_calculado = "K" 
    else:
        dv_calculado = str(dv_calculado )  

    # Comprobar si coincide con el digito verificador orignal
    return dv_original == dv_calculado

def validar_contrasena(contrasena):

    errores = []
    caracteres_especiales = "!@#$%&/."

    if len(contrasena) < 8 or len(contrasena) > 16:
        errores.append("La contraseña debe tener entre 8 y 16 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in caracteres_especiales for c in contrasena):
        errores.append("Debe contener al menos un carácter especial (!@#$%&/.).")

    return errores

def validar_correo(correo):

    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(patron_correo, correo))

def validar_telefono(telefono):

    patron_telefono = r'^9\d{8}$'

    return bool(re.match(patron_telefono, telefono))       
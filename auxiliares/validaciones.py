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

        
import hashlib
import hmac
import secrets

# La sal se genera de manera aleatoria para cada contraseña,
# por lo que aunque dos usuarios tengan la misma contraseña,
# sus hashes finales serán completamente diferentes.
# Generar la sal con secrets.token_bytes(16).
# Convertir la contraseña a bytes con contrasena.encode().
# Calcular el hash con hashlib.pbkdf2_hmac("sha256", ...).
# Unir la sal y el hash en un solo texto, con .hex() y un separador.

# de este video saque la idea de como generar el hash y verificarlo:
#https://www.youtube.com/watch?v=it9suW1HN3Q

# generar_hash y verificar_contrasena deben usar el mismo valor, por eso lo almaceno en una constante, porr si quiero cambiarlo, lo haga en un solo lugar.
ITERACIONES = 100_000

def generar_hash(contrasena):
    # Generar la sal con 16 bytes aleatorios
    sal = secrets.token_bytes(16)

    # Convertir la contraseña a bytes
    contrasena_bytes = contrasena.encode('utf-8')

    # Calcular el hash con PBKDF2 HMAC usando SHA-256 y ITERACIONES vueltas
    # Argumentos: (algoritmo, contraseña_bytes, sal, iteraciones)
    hash_bytes = hashlib.pbkdf2_hmac('sha256', contrasena_bytes, sal, ITERACIONES)

    # Unir la sal y el hash usando .hex() y un separador('$')
    resultado = f"{sal.hex()}${hash_bytes.hex()}"

    return resultado


def verificar_contrasena(contrasena, guardado):
    # Sin valor guardado (None o "") o sin separador, no se puede verificar
    if not guardado or '$' not in guardado:
        return False

    try:
        # Separar el texto guardado en sal y hash
        sal_hex, hash_hex = guardado.split('$', 1)

        # Convertir la sal de hex a bytes
        sal = bytes.fromhex(sal_hex)

        # Calcular el hash de la contraseña ingresada con la misma configuración (sha256 e ITERACIONES)
        contrasena_bytes = contrasena.encode('utf-8')
        hash_calculado = hashlib.pbkdf2_hmac('sha256', contrasena_bytes, sal, ITERACIONES)

        # Convertir el hash guardado (en hex) a bytes para poder compararlo
        hash_guardado = bytes.fromhex(hash_hex)

        # Comparar ambos hashes de forma segura contra ataques de temporización (timing attacks)
        return hmac.compare_digest(hash_calculado, hash_guardado)

    except (ValueError, TypeError, AttributeError):
        return False
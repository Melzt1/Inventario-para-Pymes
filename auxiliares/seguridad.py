import bcrypt

def generar_hash(contrasena):
    return bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_contrasena(contrasena, hash_guardado):
    try:
        return bcrypt.checkpw(contrasena.encode("utf-8"), hash_guardado.encode("utf-8"))
    except (ValueError, TypeError):
        return False
import mysql.connector
from mysql.connector import errorcode

def generar_conexion(user, password, host, database):
    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexion exitosa")
            return conexion
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(f"Error de conexión: {error}")
    return None

# test de conexion
mi_conexion = generar_conexion("root", "1234", "localhost", "sistema_pyme")

if mi_conexion:
    mi_conexion.close()
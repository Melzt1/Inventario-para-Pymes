from peewee import MySQLDatabase
from decouple import config


def conectar_db():
    database = MySQLDatabase(
        config('db'),
        host=config('host'),
        port=config('port', cast=int),
        user=config('user'),
        password=config('password'),
        charset='utf8mb4'
    )

    return database

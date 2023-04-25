from logger import log
import psycopg2 as bd
import sys


class Connection:
    _DATABASE = 'test'
    _USERNAME = 'vanstrouble'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _connection = None
    _cur = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = bd.connect(
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Conexión exitosa: {cls._connection}')
                return cls._connection
            except Exception as e:
                log.error(f'Error. Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls._connection

    @classmethod
    def get_cursor(cls):
        if cls._cur is None:
            try:
                cls._cur = cls.get_connection().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cur}')
                return cls._cur
            except Exception as e:
                log.error(f'Error. Ocurrió una excepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cur


if __name__ == '__main__':
    Connection.get_connection()
    Connection.get_cursor()

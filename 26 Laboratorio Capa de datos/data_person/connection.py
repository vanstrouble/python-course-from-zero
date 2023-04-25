from logger import log
from psycopg2 import pool
import sys


class Connection:
    _DATABASE = 'testing'
    _USERNAME = 'vanstrouble'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    database=cls._DATABASE)

                log.debug(f'Creación del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit(1)
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        connection = cls.get_pool().getconn()
        log.debug(f'Conexión obtenida del pool: {connection}')
        return connection

    @classmethod
    def release_connection(cls, connection):
        cls.get_pool().putconn(connection)
        log.debug(f'Regresamos la conexión al pool: {connection}')

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()


if __name__ == '__main__':
    connection1 = Connection.get_connection()
    Connection.release_connection(connection1)

    connection2 = Connection.get_connection()
    # connection3 = Connection.get_connection()
    # connection4 = Connection.get_connection()
    # connection5 = Connection.get_connection()

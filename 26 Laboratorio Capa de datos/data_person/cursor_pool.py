from logger import log
from connection import Connection


class Cursor_Pool:
    def __init__(self) -> None:
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._connection = Connection.get_connection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_value, trace):
        log.debug('Se ejecuta método __exit__')
        if exc_value:
            self._connection.rollback()
            log.error(f'Ocurió una excepción: {exc_value} {exc_type} {trace}')
        else:
            self._connection.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Connection.release_connection(self._connection)


if __name__ == '__main__':
    with Cursor_Pool() as cur:
        log.debug('Dentro del bloque with')
        cur.execute('SELECT * FROM users')
        log.debug(cur.fetchall())

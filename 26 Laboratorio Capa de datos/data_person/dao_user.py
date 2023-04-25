from cursor_pool import Cursor_Pool
from logger import log
from user import User


class DAO_User:
    '''
    DAO - Data Access Object for user table
    CRUD - Create, Read, Update, Delete
    '''

    _SELECT = 'SELECT * FROM users ORDER BY id_user'
    _INSERT = 'INSERT INTO users(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE users SET username=%s, password=%s WHERE id_user=%s'
    _DELETE = 'DELETE FROM users WHERE id_user=%s'

    @classmethod
    def select(cls):
        with Cursor_Pool() as cur:
            log.debug('Seleccionado usuarios')
            cur.execute(cls._SELECT)
            records = cur.fetchall()
            users = []
            for record in records:
                user = User(record[0], record[1], record[2])
                users.append(user)
            return users

    @classmethod
    def insert(cls, user):
        with Cursor_Pool() as cur:
            log.debug(f'Usuario a insertar: {user}')
            values = (user.username, user.password)
            cur.execute(cls._INSERT, values)
            return cur.rowcount

    @classmethod
    def update(cls, user):
        with Cursor_Pool() as cur:
            log.debug(f'Usuario a actualizar: {user}')
            values = (user.username, user.password, user.id_user)
            cur.execute(cls._UPDATE, values)
            return cur.rowcount

    @classmethod
    def delete(cls, user):
        with Cursor_Pool() as cur:
            log.debug(f'Usuario a eliminar: {user}')
            values = (user.id_user,)
            cur.execute(cls._DELETE, values)
            return cur.rowcount

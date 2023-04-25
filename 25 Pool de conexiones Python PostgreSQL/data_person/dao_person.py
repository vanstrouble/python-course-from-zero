from cursor_pool import Cursor_Pool
from person import Person
from logger import log


class DAO_Person:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''

    _SELECT = 'SELECT * FROM users ORDER BY id_user'
    _INSERT = 'INSERT INTO users(first_name, sec_name, last_name, birthdate) VALUES(%s, %s, %s, %s)'
    _UPDATE = 'UPDATE  users set first_name = %s, sec_name = %s, last_name = %s, birthdate = %s WHERE id_user = %s'
    _DELETE = 'DELETE FROM users WHERE id_user = %s'

    @classmethod
    def select(cls):
        with Cursor_Pool() as cur:
            cur.execute(cls._SELECT)
            records = cur.fetchall()

            persons = []
            for record in records:
                person = Person(record[0], record[1], record[2], record[3], record[4])
                persons.append(person)
            return persons

    @classmethod
    def insert(cls, person):
        with Cursor_Pool() as cur:
            values = (person.first_name, person.sec_name, person.last_name, person.birthdate)
            cur.execute(cls._INSERT, values)
            log.debug(f'Persona insertada: {person}')
            return cur.rowcount

    @classmethod
    def update(cls, person):
        with Cursor_Pool() as cur:
            values = (person.first_name, person.sec_name, person.last_name, person.birthdate, person.id_user)
            cur.execute(cls._UPDATE, values)
            log.debug(f'Persona actualizada: {person}')
            return cur.rowcount

    @classmethod
    def delete(cls, person):
        with Cursor_Pool() as cur:
            values = (person.id_user,)
            cur.execute(cls._DELETE, values)
            log.debug(f'Persona eliminada: {person}')
            return cur.rowcount


if __name__ == '__main__':
    # Insert a record
    # person1 = Person(first_name='Silvia', sec_name='Elizabeth', last_name='Amaro', birthdate='1998-10-02')
    # inserted_records = DAO_Person.insert(person1)
    # log.debug(f'Personas insertadas {inserted_records}')

    # Update an existing record
    # person1 = Person(3, 'Jessica', '', 'Alarcón', '1997-10-24')
    # updated_records = DAO_Person.update(person1)
    # log.debug(f'Personas actualizadas: {updated_records}')

    # Delete an existing record
    # person1 = Person(id_user=9)
    # deleted_records = DAO_Person.delete(person1)
    # log.debug(f'Personas eliminadas: {deleted_records}')

    # Show the records
    persons = DAO_Person.select()
    for person in persons:
        log.debug(person)

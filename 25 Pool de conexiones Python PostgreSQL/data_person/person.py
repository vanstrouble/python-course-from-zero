from logger import log


class Person:
    def __init__(self, id_user=None, first_name=None, sec_name=None, last_name=None, birthdate=None) -> None:
        self._id_user = id_user
        self._first_name = first_name
        self._sec_name = sec_name
        self._last_name = last_name
        self._birthdate = birthdate

    def __str__(self):
        return f'''
            ID: {self._id_user}, Nombre: {self._first_name}, Segundo nombre: {self._sec_name}
            Apellido: {self._last_name}, Nacimiento: {self._birthdate}
        '''

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def sec_name(self):
        return self._sec_name

    @sec_name.setter
    def sec_name(self, sec_name):
        self._sec_name = sec_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self._birthdate = birthdate


if __name__ == '__main__':
    person1 = Person(1, 'Aideé', 'Berenice', 'Correa', '1997-09-03')
    log.debug(person1)
    print(person1)

    # Simulate an insertion
    persona1 = Person(first_name='Aideé', sec_name='Berenice', last_name='Correa', birthdate='1997-09-03')
    log.debug(persona1)

    # Simulate a delete
    persona1 = Person(id_user=1)
    log.debug(persona1)

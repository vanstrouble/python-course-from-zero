# Data Classes
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Person():
    name: str
    lastname: str
    persons_count: ClassVar[int] = 0


    def __post_init__(self):
        if not self.name:
            raise ValueError('Debes dar un nombre')



if __name__ == '__main__':
    p1 = Person('Aideé', 'Correa')
    print(p1)

    # Variable de clase
    print(f'Variable de clase: {Person.persons_count}')

    # Variables de instancia
    print(f'Variables de instancia: {p1.__dict__}')

    # Variable con valores vacios
    empty_person = Person('', '')
    print(f'Persona vacía: {empty_person}')

# Representación de objetos (str, repr, format)
# print(dir(object))

class Person:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    # repr, mas enfocado a los developers
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(nombre: {self.name}, apellido: {self.lastname})'

    # str es más para el usuario final u otros sistemas
    # la implementación por default llama al método repr
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} {self.lastname}'

    # format
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.name} y apellido {self.lastname}'


# repr
person1 = Person('Aideé', 'Correa')
print(f'Objeto person1: {person1!r}')

# str
print(person1)

#format
print(f'{person1}')

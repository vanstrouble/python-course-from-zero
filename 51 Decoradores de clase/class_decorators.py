# Decoradores de clase

# Permiten transformar de manera programática nuestar clase.
# Es similar a los decoradores de funciones (es metaprogramación)


def repr_decorator(cls):
    print('Se ejecuta el decorador de la clase')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    return cls


@repr_decorator
class Person(object):
    def __init__(self, name, lastname) -> None:
        print('Se ejecuta el inicializador')
        self._name = name
        self._lastname = lastname

    @property
    def name(self):
        return self._name

    @property
    def lastname(self):
        return self._lastname

    # def __repr__(self) -> str:
    #     return f'Persona({self._name}, {self._lastname})'


p1 = Person('Aideé', 'Correa')

if __name__ == '__main__':
    pass

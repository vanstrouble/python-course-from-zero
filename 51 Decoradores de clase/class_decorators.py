# Decoradores de clase

# Permiten transformar de manera programática nuestar clase.
# Es similar a los decoradores de funciones (es metaprogramación)


import inspect


def repr_decorator(cls):
    print('Se ejecuta el decorador de la clase')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    attributes = vars(cls)
    
    # Iteramos cada atributo
    # [print(name, attributes) for name, attributes in attributes.items()]

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in attributes:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    init_sign = inspect.signature(cls.__init__)
    print(f'Firma del método __init__: {init_sign}')

    # Recuperamos los parámetros, excepto el primero que es self
    init_parameters  = list(init_sign.parameters)[1:]
    print(f'Parámetros init: {init_parameters}')

    # Revisar si por cada parámetro tiene un método property asociado
    for parameter in init_parameters:
        # Property es un valor de tipo built-in para preguntar si 
        # se está utilizando el decorador property
        if not isinstance(attributes.get(parameter), property):
            raise TypeError(f'El parámetro {parameter} no utiliza el método property')

    # Crear método repr dinámicamente
    def repr_method(self, ):
        return f'Resultado de ejecutar método repr'

    # Agregar dinamicamente el método repr a nuestra clase
    setattr(cls, '__repr__', repr_method)

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


if __name__ == '__main__':
    p1 = Person('Aideé', 'Correa')
    print(p1)

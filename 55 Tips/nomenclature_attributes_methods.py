class MyClass:
    """
    Clase MyClass que demuestra el uso de variables públicas, protegidas y privadas en Python.

    Atributos:
        public_variable (int): Variable pública accesible desde cualquier lugar.
        _protected_variable (int): Variable protegida, su acceso está limitado a la clase y sus subclases.
        __private_variable (int): Variable privada, su acceso está restringido a la clase.

    Métodos:
        __init__(): Inicializa una instancia de MyClass con variables públicas, protegidas y privadas.
    """

    # En Python, la nomenclatura de variables y métodos sigue ciertas convenciones:
    # - Las variables y métodos públicos no tienen ningún prefijo especial.
    # - Las variables y métodos protegidos tienen un solo guion bajo (_) al principio de su nombre.
    # - Las variables y métodos privados tienen dos guiones bajos (__) al principio de su nombre.
    def __init__(self):
        self.public_variable = 10
        self._protected_variable = 20
        self.__private_variable = 30


if __name__ == '__main__':
    obj = MyClass()
    print(obj.public_variable)
    print(obj._protected_variable)
    # print(obj.__private_variable)

# Comprobar cómo funciona la Herencia Múltiple con el ejercicio
# No admite herencia circular

class Class1(object):
    def __init__(self) -> None:
        print('Class1.__init__()')

    def test_method(self, ):
        print('Class1.test_method()')


class Class2(Class1):
    def __init__(self) -> None:
        super().__init__()

    def test_method(self, ):
        print('Class2.test_method()')


class Class3(Class1):
    def __init__(self) -> None:
        super().__init__()

    def test_method(self, ):
        print('Class3.test_method()')


class Class4(Class2, Class3):
    # def __init__(self) -> None:
    #     super().__init__()

    def test_method(self):
        print('Class4.test_method()')


# Prueba
class4 = Class4()
print(Class4.__bases__)

# MRO
print(Class4.__mro__)

# Método
print(class4.test_method())

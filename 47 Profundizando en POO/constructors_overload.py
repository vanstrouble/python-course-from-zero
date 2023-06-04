# Simulación de sobrecarga de cosntructortes
# Agregar otras formas de crear objetos
class Person:

    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    @classmethod
    def create_empty_person(cls):
        return cls(None, None)

    @classmethod
    def create_person_values(cls, name, lastname):
        return cls(name, lastname)

    def __str__(self) -> str:
        return f'Nombre: {self.name}, Apellido: {self.lastname}'


person1 = Person('Aideé', 'Correa')
empty_person = Person.create_empty_person()
print(person1)
print(empty_person)

values_person = Person.create_person_values('Berenice', 'Villegas')
print(values_person)

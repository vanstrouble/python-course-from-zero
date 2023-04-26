class Person:
    persons_count = 0

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name


# Mostrar los atributos de un objeto
person1 = Person('Aideé', 'Correa')
print(person1.__dict__)

# Crear un atributo al vuelo
print(person1.persons_count)  # Accediento al atributo de clase
# No es posible modificarlo con el objeto, solo con la clase

person1.persons_count = 10
print(person1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Person.persons_count)
print(person1.persons_count)

# Un segundo objeto
person2 = Person('Pedro', 'Vázquez')
print(person2.__dict__)
print(person2.persons_count)

# Asociar un atributo al vuelo
Person.count2 = 20
print(Person.count2)

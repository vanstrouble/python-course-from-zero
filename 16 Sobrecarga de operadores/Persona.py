class Persona:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

# object1 + object2
# object1.__add(object2)


persona1 = Persona('Aideé', 23)
persona2 = Persona('Berenice', 22)

print(persona1 + persona2)
print(persona1 - persona2)

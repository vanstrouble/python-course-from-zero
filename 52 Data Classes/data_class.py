# Data Classes
from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Address:
    street: str
    number: int = 0


@dataclass(eq=True, frozen=True)
class Person:
    name: str
    lastname: str
    address: Address
    persons_count: ClassVar[int] = 0

    def __post_init__(self):
        if not self.name:
            raise ValueError("Debes dar un nombre")


if __name__ == "__main__":
    ad1 = Address("Gral. Pedro García", 16)
    p1 = Person("Aideé", "Correa", ad1)
    print(p1)

    # Variable de clase
    print(f"Variable de clase: {Person.persons_count}")

    # Variables de instancia
    print(f"Variables de instancia: {p1.__dict__}")

    # Variable con valores vacios
    empty_person = Person("Empty", "", None)  # Validación solo en nombre
    print(f"Persona vacía: {empty_person}")

    # Revisar igualdad entre objetos (__eq__)
    p2 = Person("Berenice", "Villegas", ad1)
    print(f"Objetos iguales: {p1 == p2}")

    # Agregar esta clase a una colección
    coll = {p1, p2}
    print(coll)

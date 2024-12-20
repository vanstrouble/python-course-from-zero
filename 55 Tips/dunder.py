# dunder.py

"""
Métodos Dunder (Double Underscore) en Python

Los métodos Dunder, también conocidos como métodos mágicos o métodos especiales, son métodos predefinidos en Python
que tienen dobles guiones bajos al principio y al final de sus nombres. Estos métodos te permiten definir el
comportamiento de tus objetos para operaciones integradas como adición, sustracción, representación de cadenas y más.

Métodos Dunder Comunes:
1. __init__(self, ...): Método constructor, llamado cuando se crea una instancia.
2. __str__(self): Define la representación en cadena de un objeto.
3. __repr__(self): Define la representación oficial en cadena de un objeto.
4. __add__(self, other): Define el comportamiento del operador de adición (+).
5. __len__(self): Define el comportamiento de la función len().
6. __eq__(self, other): Define el comportamiento del operador de igualdad (==).

Ejemplos:
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)


# Ejemplo de uso
p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1)  # Salida: Point(2, 3)
print(repr(p1))  # Salida: Point(2, 3)
print(p1 + p2)  # Salida: Point(6, 8)
print(p1 == p2)  # Salida: False
print(len(p1))  # Salida: 3

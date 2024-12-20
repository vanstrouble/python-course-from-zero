# underscore.py

# En Python, el guion bajo (_) tiene varios usos especiales. Aquí hay algunos ejemplos:

# 1. Uso de _ como una variable temporal o de "desecho"
for _ in range(5):
    print("Esto se imprimirá 5 veces")

# 2. Uso de _ en la consola interactiva para obtener el último resultado
# >>> 5 + 3
# 8
# >>> _
# 8


# 3. Uso de _ en nombres de variables para indicar que son privadas
class MyClass:
    def __init__(self):
        self._private_variable = 42


# 4. Uso de __ (doble guion bajo) para evitar colisiones de nombres en clases
class MyOtherClass:
    def __init__(self):
        self.__private_variable = 99


# 5. Uso de _ en nombres de variables para mejorar la legibilidad
big_number = 1_000_000

# 6. Uso de _ como un marcador de posición en desempacado de tuplas
tuple_example = (1, 2, 3)
a, _, c = tuple_example
print(a, c)  # Salida: 1 3

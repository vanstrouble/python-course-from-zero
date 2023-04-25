"""
Tarea: Multiplicación de valores recibidos
Crear una función para multiplicar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función y regresar
como resultado el resultado de todos los valores pasados como argumentos.
"""


def multNumeros(*numeros):
    mult = 1
    for numero in numeros:
        mult *= numero
    return mult


print(multNumeros(1, 2, 3, 4, 5))

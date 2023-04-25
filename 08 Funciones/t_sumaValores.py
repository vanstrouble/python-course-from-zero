"""
Tarea: Suma de valores recibidos
Crear una función para sumar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función y regresar 
como resultado la suma de todos los valores pasados como argumentos.
"""

def sumaValores(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

print(sumaValores(1, 2, 3, 4, 5))

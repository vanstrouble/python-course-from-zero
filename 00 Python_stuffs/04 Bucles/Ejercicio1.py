""" Ejercicio 1
Llenar una lista con los números del 1 al 50, luego mostrar la
lista con un bucle for, los elementos deben mostrarse de la siguiente forma:
1-2-3-4-5-…-50
"""
# Agregando elementos a la lista
lista = list(range(1, 51))

# Imprimiendo los elementos de la lista
for i in lista:
    print(i, end='-')

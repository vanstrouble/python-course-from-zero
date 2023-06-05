'''
Ejercicio 1
Eliminar elementos repetidos de una lista
'''
lista = [1, 2, 3, 'Aideé', 2, 4, 2, 'Aideé', 'Berenice', 3]

lista = list(set(lista))

print(lista)

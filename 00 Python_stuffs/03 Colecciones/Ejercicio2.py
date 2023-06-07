'''
Ejercicio 2
Escriba un programa que tenga dos lista y que, a continuación, cree las siguientes 
listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de los elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de los elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de los elementos que aparecen en ambas listas.
'''
lista1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,10,15]
lista2 = [4,9,12,78,6,2,1,15,26,74,32,0,1,89]

# Elimine los elementos repetidos
a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f'Lista de elementos que aparecen en las dos listas: {union}')
print(f'Lista de los elementos que aparecen en la primera lista, pero no en la segunda: {soloA}')
print(f'Lista de los elementos que aparecen en la segunda lista, pero no en la primera: {soloB}')
print(f'Lista de los elementos que aparecen en ambas listas: {interseccion}')

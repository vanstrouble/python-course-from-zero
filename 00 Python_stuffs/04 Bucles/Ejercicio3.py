"""
Ejercicio 3
Pide números y mételos en una lista, cuando el usuario meta un 0
dejamos de insertar. Por último, muestra los números ordenados de menor a mayor
"""
lista = []

salir = False

while not salir:
    numero = float(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort()

print(f'\nLista ordenada: \n{lista}')

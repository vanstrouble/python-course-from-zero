"""
Ejercicio 2
Llenar una lista con los números del 1 al 10, luego modificar los elementos
de la lista multiplicándolos por un valor que el usuario digite
"""
# Creamos la lista y la llenamos
lista = list(range(1, 11))

# Mostramos lista original
print('Esta es la lista original: ')

for i in lista:
    print(i, end=' - ')

valor = int(input('\n¿Por cuál valor quiere que los multiplique? R: '))

# Imprimir valores multiplicados
print(f'\nNúmeros multiplicados por el valor {valor}')
for i in lista:
    print(i * valor, end=' - ')

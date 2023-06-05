"""
Ejercicio 10
Hacer un programa que pida una cadena por teclado, luego meta los caracteres
en una lista son repetir caracteres
"""
lista = []

cadena = input('Escriba algo: ')
cadena = cadena.lower()

for i in cadena:
    if i not in lista:
        lista.append(i)

print(f'\nLista sin repetir caracteres: \n{lista}')

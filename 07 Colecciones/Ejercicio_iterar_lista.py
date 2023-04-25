'''
Tarea: Iterar una lista de 0 a 10 e imprimir números divisibles entre 3
Iterar una lista de 0 a 10 e imprimir sólo los números divisibles entre 3
'''

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in lista:
    if n % 3 == 0:
        print(n)

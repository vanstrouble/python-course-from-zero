# Ejercicio 7 - Juego de adivinar el número

import random

aleatorio = random.randint(0, 100)  # Generamos un número aleatorio

print('\t.:ADIVINA EL NÚMERO:.\n')

cont = 0
while True:
    numero = int(input('Digite un número: '))
    cont += 1
    if numero > aleatorio:
        print('\tChale, digita un número MENOR')
    elif numero < aleatorio:
        print('\tChale, digita un número MAYOR')
    else:
        print(f'\n\t¡FELICIDADES! Adivinaste el número {aleatorio} en {cont} intentos')
        break

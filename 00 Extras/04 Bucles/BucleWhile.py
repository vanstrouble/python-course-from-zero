# Bucle While

import math

numero = int(input('Digite un número: '))

while numero < 0:
    print('Error. Digite un número entero positivo')
    numero = int(input('Digite un número: '))

print(f'\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}')

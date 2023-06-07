"""
Hacer un programa para calcular el factorial de un número entero positivo
"""
numero = int(input('Digite el número: '))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f'El factorial de {numero} es: {factorial}')

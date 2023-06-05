"""
Ejercicio 4
Desarrollar un programa para calcular el factorial de un número con ayuda de
una función recursiva
"""
def factorial(numero):
    if numero > 0:
        resultado = numero * factorial(numero - 1)
    else: 
        resultado = 1
    return resultado

numero = int(input("Digite el número: "))
print(factorial(numero))

"""
Ejercicio 5
Desarrollar un programa que permita sumar los dígitos de un número con 
ayuda de una función recursiva
"""

def sumRecursiva(n):
    if len(n) > 0:
        suma = int(n[0]) + sumRecursiva(n[1:])
        return suma
    else:
        return 0

numero = input("Digite un número: ")
print(f"La suma de su digitos es: {sumRecursiva(numero)}")

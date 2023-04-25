# Factorial de un número con funciones recursivas. 

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


numero = int(input('Digita un número: '))
print(f'El factorial de {numero} es {factorial(numero)}')

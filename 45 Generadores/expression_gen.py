mult = (value * value for value in range(4))
print(mult)
print(type(mult))
print(next(mult))
print(next(mult))
print(next(mult))
print(next(mult))

# También se puede pasar una expresión generadora a una función (sin parentesis)
import math

sumary = sum(value*value  for value in range(4))
print(f'Result: {sumary}')

# Podemos usar una lista o cualquier otro iterador
names = ['Juan', 'Pablo',]
generator = (value for value in names)
print(next(generator))
print(next(generator))

# Crear un string a partir de un generador creado a partir de una lista
data = ['Berenice', 'Correa', 24]
cont = 0

def increment():
    global cont
    cont += 1
    return cont

# La primera parte es el yield del generator y la sefunda parte es el generador
generator = (f'{increment()}. {value}' for value in data)
list_gen = list(generator)
print(list_gen)
string = '. '.join(list_gen)
print(f'String generated: {string}')

# Multiplicar un número sin utilizar el signo de multiplicar
a = 4
b = 8
resultado = 0
for x in range(a):
    resultado += b

print(resultado)

# Ingresar nombre y apellido e imprimirlas al revés
nombre = 'Aideé'
apellido = 'Correa'
concatenacion = nombre + ' ' + apellido
print(concatenacion)
print(concatenacion[::-1])

# Escribir una función que encuentre el menor número de una lista
lista = [1, 2, 4, 6, 7, -2, 9, -21]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor 

print('Número menor:', menor)

# Escribir la función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
def calcular_volumen(radio):
    return 4 / 3 * 3.14 * radio ** 3

resultado = calcular_volumen(6)
print(resultado)

# Escribir una función que indique si el usuario es mayor de edad
def mayor_edad(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad) -> None:
        self.edad = edad
    
usuario = Usuario(15)
usuario2 = Usuario(21)

res1 = mayor_edad(usuario)
res2 = mayor_edad(usuario2)

print(res1, res2)

# Escribir una función que indique si un número es par o impar
def par_impar(num):
    if num % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')

par_impar(2)
par_impar(7)

# Escribir una función que indique cuántas vocales tiene una palabra
palabra = 'ChanchitoFeliz'
palabra = palabra.lower()

vocales = 0

for x in palabra:
    vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print(vocales)

# Escribir una app que reciba una cantidad infinita de números hasta 
# decir basta, luego que devuelva la suma de los números ingresados
lista = []

print('Ingrese números y para salir escriba "basta"')
while True:
    valor = input('Ingrese valor: ')
    valor = valor.lower()
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato inválido')
            exit()

resultado = 0
for x in lista:
    resultado += x

print(resultado)

# Escribir una función que reciba nombre y apellido y los vaya agregando
# a un archivo
def agrega_archivo(nombre, apellido):
    archivo = open('nombres.txt', 'a')
    archivo.write(nombre + ' ' + apellido + '\n')
    archivo.close()

agrega_archivo('Aideé', 'Berenice')
agrega_archivo('Pedro', 'Antonio')

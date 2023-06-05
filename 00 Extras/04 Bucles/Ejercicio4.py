"""
Ejercicio 4
Hacer un programa para sumar números pares dentro de un rango
"""

a = int(input('Digite el inicio del rango: '))
b = int(input('Digite el fin del rango: '))

suma = 0

for i in range(a, b + 1):
    if i % 2 != 0:
        continue
    else:
        suma += i

print(f'La suma de los números pares dentro del rango {a} al {b} es: {suma}')


'''
Forma alternativa sin bucles

n1= int(input("Digite el primer número: "))
 
n2= int(input("Digite el segundo número: "))
  
tupla = tuple(range(n1,n2+1,2))
 
suma = sum(tupla)
 
print(suma)
'''
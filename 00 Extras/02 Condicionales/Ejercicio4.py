'''
Ejercicio 4
Construir un programa que simule el funcionamiento de una calculadora que 
puede realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación, 
división). El usuario debe especificar la operación con el primer carácter del nombre 
de la operación.
S, s - Suma
R, r - Resta
P, p, M, m - Multiplicación
D, d - División
'''

print("\t.:CALCULADORA CONDICIONALES:.\n")

numero1 = float(input("Digite el PRIMER número: "))
numero2 = float(input("Digite el SEGUNDO número: "))

print('\nOperaciones disponibles')
print('S, s - Suma \nR, r - Resta \nP, p, M, m - Multiplicación \nD, d - División')
operacion = input('\nDigite la operación a realizar: ')
operacion = operacion.lower();

resultado = 0
variable = 'vacia'

if operacion == 's':
    variable = 'suma'
    resultado = numero1 + numero2
elif operacion == 'r':
    variable = 'resta'
    resultado = numero1 - numero2
elif operacion == 'p' or operacion == 'm':
    variable = 'multiplicación'
    resultado = numero1 * numero2
elif operacion == 'd':
    variable = 'división'
    if numero2 == 0:
        resultado = 'Error. Operación indefinida'
    else:
        resultado = numero1 / numero2
else:
    print("No presionó una opción correcta")

print(f'\nEl resultado de la {variable} es: {resultado:.2f}')

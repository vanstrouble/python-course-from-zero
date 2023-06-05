'''
Ejercicio 1
Hacer un programa que pida 2 números y se de cuenta cuál es par o impar
'''

numero1 = int(input("Digite un número: "))
numero2 = int(input("Digite otro número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f"El número {numero1} es par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"El número {numero2} es par")
else: 
    print("Ambos son impares")
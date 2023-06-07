'''
Ejercicio 2
Hacer un programa que pida 3 números y determine cuál es el mayor.
'''

print("\tDETERMINAR EL NÚMERO MAYOR\n")

num1 = float(input("Digite el PRIMER número: "))
num2 = float(input("Digite el SEGUNDO número: "))
num3 = float(input("Digite el TERCER número: "))

if num3 < num1 > num2:
    if num2 > num3:
        print(f"\nEl numero mayor es: {num1}")
        print(f"{num1} > {num2} > {num3}")
    else:
        print(f"\nEl numero mayor es: {num1}")
        print(f"{num1} > {num3} > {num2}")
elif num3 < num2 > num1:
    if num1 > num3:
        print(f"\nEl numero mayor es: {num2}")
        print(f"{num2} > {num1} > {num3}")
    else:
        print(f"\nEl numero mayor es: {num2}")
        print(f"{num2} > {num3} > {num1}")
elif num1 < num3 > num2: 
    if num1 > num2:
        print(f"\nEl numero mayor es: {num3}")
        print(f"{num3} > {num1} > {num2}")
    else:
        print(f"\nEl numero mayor es: {num3}")
        print(f"{num3} > {num2} > {num1}")
else: 
    print("\nTodos son iguales")
'''
Ejercicio 5
Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y 
tendrá el siguiente menú de opciones:
    1. Ingresar dinero en la cuenta
    2. Retirar dinero de la cuenta
    3. Mostrar dinero disponible
    4. Salir
'''
saldo = 1000

print('\t.:BANCO PARA MOVER DINERO:.\n')

print('---- Menú ----')
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero de la cuenta')
print('3. Mostrar dinero disponible')
print('4. Salir')
opcion = input('Digite la opción: ')

if opcion == '1':
    monto = float(input('\nDigite el monto a ingresar: '))
    saldo += monto
    print('\nDinero ingresador correctamente')
    print(f'El saldo actual es de: ${saldo}')
elif opcion == '2':
    monto = float(input('\nDigite el monto a retirar: '))
    if monto > saldo:
        print('\nNo cuenta con saldo suficiente')
    else:
        saldo -= monto
        print('\nDinero retirado correctamente')
        print(f'El saldo actual es de: ${saldo}')
elif opcion == '3':
    print(f'\nSu saldo es de: ${saldo}')
elif opcion == '4': 
    print('\nGracias por usar el servicio')
    exit()
else:
    print('\nOpción no válida')
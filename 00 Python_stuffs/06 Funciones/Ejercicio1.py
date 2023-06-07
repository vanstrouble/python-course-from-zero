"""
Ejercicio 1
Desarrollar un programa que pueda calcular el valor de cambio de moneda.
"""
def cambioMXN_Dolares(mxn):
    return mxn / 20.19

def cambioDolares_MXN(dolares):
    return dolares * 20.19

while True:
    print('''\t.:MENú:.
1. MXN a Dólares
2. Dólares a MXN
3. Salir''')
    opcion = int(input('Digite una opción: '))

    print()

    if opcion == 1:
        mxn = float(input('Digite la cantidad de pesos (MXN): '))
        print(f'\nDólares -> ${cambioMXN_Dolares(mxn):.2f}\n')

    elif opcion == 2:
        dolares = float(input('Digite la cantidad de dólares: '))
        print(f'\nPeso MXN -> ${cambioDolares_MXN(dolares):.2f}\n')
    
    elif opcion == 3:
        break

    else:
        print('\nDigite una opción válida\n')

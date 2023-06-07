"""
Ejercicio 1
Hacer un programa donde se deberá imprimir por consola la palabra con más caracteres 
de dos palabras dadas. En el caso de que ambas palabras tengan la misma cantidad de 
caracteres, deberás mostrar el mensaje "Son iguales"
"""
print('\nCOMPARACIÓN DE CADENAS\n')
cadena1 = input('Escribe algo: ')
cadena2 = input('Escribe otra cosa: ')

if len(cadena1) > len(cadena2):
    print(f'\nLa cadena más larga es: {cadena1}')
elif len(cadena1) < len(cadena2):
    print(f'\nLa cadena más larga es: {cadena2}')
else:
    print(f'\nAmbas cadenas son iguales')

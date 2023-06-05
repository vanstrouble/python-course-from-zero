"""
Ejercicio 3
Hacer un programa que determine si una palabra o frase es palíndroma.
Una cadena palíndroma se lee igual de izquierda a derecha que de derecha a izquierda. 
Ejemplos:
    - oso
    - reconocer
    - anita lava la tina
"""
print('\t.:POLÍNDROTA O NO:.\n')
palabra = input('Escribe una palabra: ')
palabra = palabra.lower() # Defino las letras en minuscula para trabajar seguro
palabra = palabra.replace(' ', '') # Elimino los espacios que pueda tener

invertida = palabra[::-1] # Invierto la cadena

if invertida == palabra:    
    print(f'\nLa palabra {palabra} es políndroma')
    print(f'{palabra} = {invertida}')
else:
    palabra = palabra.capitalize()
    print(f'\n{palabra} NO es políndroma')
    print(f'{palabra} != {invertida}')

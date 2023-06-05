"""
Ejercicio 9
Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma frase pero sin
espacios en blanco y además un contador de cuántos caracteres tiene la frase (sin contar los espacios
en blanco).
"""
frase = input('Escriba algo: ')
frase2 = ''
for i in frase:
    if i == ' ':
        continue
    frase2 += i

print(f'\nFrase final: {frase2} \nNº de caracteres: {len(frase2)}')

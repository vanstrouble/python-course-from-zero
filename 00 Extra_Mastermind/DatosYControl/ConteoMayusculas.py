# Conteode mayusculas en String

import string

texto = input("Introduzca el texto: ")

letras_mayusculas = 0

for letra in texto:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print(f"El número de mayúsculas son: {letras_mayusculas}")

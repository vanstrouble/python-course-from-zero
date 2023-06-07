# Contra letras y espacios

texto_usuario = input("Introduzca el texto: ")

espacios = 0
puntos = 0
comas = 0

for caracter in texto_usuario:
    if caracter == " ":
        espacios += 1
    elif caracter == ".":
        puntos += 1
    elif caracter == ",":
        comas += 1

print(f"Espacios: {espacios}\nPuntos: {puntos}\nComas: {comas}")

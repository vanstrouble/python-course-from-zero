# Nuemro usuario
numeros = []
numero = None

while numero != -1:
    numero = int(input("Digite un número: "))
    if numero != -1:
        numeros.append(numero)
    else:
        break

print(numeros)

pequenio = numeros[0]
grande = numeros[0]

for numero in numeros[1:]:
    if pequenio > numero:
        pequenio = numero
    if grande < numero:
        grande = numero

print(f"Numero grande: {grande}\nNumero pequeño: {pequenio}")

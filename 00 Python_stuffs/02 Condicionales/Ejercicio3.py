# Ejercicio 3
# Hacer un programa que pida un caracter e indique si es una vocal o no

print("\t.:DETERMINAR SI ES VOCAL O NO:.\n")

letra = input("Digite una letra: ")
letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")
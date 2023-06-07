# Condicionales combinados

edad = int(input("Digite su edad: "))

if 0 < edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("\tMayor de edad")
    else:
        print("\tNo es mayor de edad")
else:
    print("Edad incorrecta")
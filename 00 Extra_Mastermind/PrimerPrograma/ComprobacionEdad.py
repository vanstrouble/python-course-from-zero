edad = int(input("Digite su edad: "))
carnet = input("Tipo de carnet… \nE - estudiante \nP - pensionista \nF - familia \nN - nada \nOpción: ")
carnet = carnet.lower()

if (edad <= 35 and edad >= 25 and carnet == "E") or edad <= 10 or (edad >= 65 and carnet == "P") or (carnet == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento")

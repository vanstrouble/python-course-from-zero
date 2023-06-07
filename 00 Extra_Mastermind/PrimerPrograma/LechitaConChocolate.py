# Ejemplo de condicionales - Preparar una lechita con chocolate

print("Voy camino a la cocina")
print("Abro el refrigerador")

hay_leche = input("¿Hay leche? (S/N): ")
hay_chocolate = input("¿Hay chocolate? (S/N):")

if hay_leche != "S" or hay_chocolate != "S":
    print("Voy a comprar al super >:c")
    if hay_leche != "S":
        print("Compro leche")
    elif hay_chocolate != "S":
        print("Compro chocolate :3")

print("Ponemos la leche en el vaso")
print("Ponemos el chocolate en el vaso")
print("Lo mezclamos tratando de no dejar grumos >:)")
print("Bebemos del nectar de la vida")

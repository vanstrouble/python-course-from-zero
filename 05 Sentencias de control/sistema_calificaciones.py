print("\nSistema de ecuaciones\n")

cal = float(input("Proporcione un valor de 0 a 10: "))

if cal >= 9 and cal <= 10:
    print("A")
elif cal < 9 and cal >= 8:
    print("B")
elif cal < 8 and cal >= 7:
    print("C")
elif cal <= 6 and cal >= 0:
    print("F")
else:
    print("Valor desconocido")

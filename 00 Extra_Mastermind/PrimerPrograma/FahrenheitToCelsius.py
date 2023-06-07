# Programa para convertir grados Fahrenheit a Celsius
# (x - 32) * 5 / 9 = y

print("Bienvenido a mi conversor de Fahrenheit a Celsius\n")

fahr = float(input("Digita los grados Fahrenheit: "))

celsius = (fahr - 32) * 5 / 9

print(f"{fahr} Fahrenheit equivale a {celsius:.2} Celsius")

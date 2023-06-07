#Tabla de multiplicar por el usuario

numero = int(input("Digite el número de la tabla: "))

for i in range(0, 11):
    print(f"{numero} * {i} = {numero * i}")

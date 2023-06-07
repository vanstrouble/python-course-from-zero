# Adivina el número

import random
numGanador = random.randint(0, 10)

numUsuario = int(input("Digita tu numero: "))

if numUsuario == numGanador:
    print(f"\nFelicidades!!\nAdvininaste el número {numGanador}")
else:
    print(f"El número ganador era {numGanador}")
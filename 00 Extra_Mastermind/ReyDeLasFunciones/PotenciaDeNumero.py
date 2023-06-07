# Hacer una función para calcular la potencia de un número

def potencia(n, base=2):
    resultado = n
    for a in range(1, base):
        resultado *= n
    return resultado


def PotenciaDeNumero():
    print("\nCalcular potencias")

    numero = int(input("\nDigite un número: "))
    pot = int(input("Digita la potencia: "))

    print(f"\n{numero} a la potencia {pot} = {potencia(numero, pot)}")


if __name__ == '__main__':
    PotenciaDeNumero()

# Secuencia de Fibonacci usando recursividad

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("\nSerie de Fibonacci con Recursividad en Python")

    numero_elementos = int(input("\nDigita el número de elementos: "))

    for a in range(1, numero_elementos + 1):
        print("{}, ".format(fibonacci(a)), end="")


if __name__ == '__main__':
    main()

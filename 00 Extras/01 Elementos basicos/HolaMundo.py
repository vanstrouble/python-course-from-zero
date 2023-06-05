# Hola mi bello mundo
print("\tHola mi pequeña Aideé <3\n")

# Python permite el tipado dinámico
valor = 10
print(valor)
valor = "Aidecita hermosa"
print(valor)

'''
    El tipado dinámico es que una misma variable puede contener diferentes
    tipos de datos en un mismo programa.
'''

# Operadores aritméticos
n1 = 10
n2 = 4.7
resultado = n1 + n2
print(resultado)

n1 = 10
n2 = 4.7
resultado = n1 - n2
print(resultado)

n1 = 10
n2 = 3
resultado = n1 * n2
print(resultado)

n1 = 10     # División de toda la vida
n2 = 3
resultado = n1 / n2
print(resultado)

n1 = 10     # División de enteros
n2 = 3
resultado = n1 // n2
print(resultado)

n1 = 10
n2 = 3
resultado = n1 % n2
print(resultado)

n1 = 2      # Exponencial (2 a la quinta potencia)
n2 = 5
resultado = n1 ** n2
print(resultado)

resultado = 3 ** 3 * (13 / 5 - (2 * 4))
print(resultado)

# Operadores relacionales
'''
    Los operadores relacionales son los mismos que en otros lenguiajes: 
    > < >= <= = == != 
'''
a = 10
b = 20
c = 30
resultado = a + b == c
print(resultado)

# Operadores lógicos
a = 10
b = 15
c = 20

resultado = ((a < b) and (b < c))
print(resultado)
resultado = ((a > b) or (b < c))
print(resultado)
resultado = not ((a > b) or (b < c))
print(resultado)

# Operadores de asignación
'''
    Los operadores de asignación son los mismos que en otros lenguajes: 
    += -= /= *= **=
'''
a = 0

a **= 2
print(a)

a %= 2
print(a)

# Salidas o impresiones de pantalla
nombre = 'Pedro'
edad = 22

print("Hola", nombre, "tienes", edad, "años")
print("Hola {} tienes {} años".format(nombre, edad))
print(f"Hola {nombre} tienes {edad} años")

# Entrada de datos
nombre1 = input("\nDigite su nombre: ")
nombre2 = input("Digite el nombre de la persona que le gusta: ")
print(f"{nombre2} y {nombre1} son novios, se quieren, se besan…")

numero = int(input("\nDigite un número: "))
print(f"Hace {numero} días que no te bañas")

# Funciones integradas
n = bin(numero)
print(f"\nEl número de días en binario es {n}")

n = len(nombre2)
print(f"\nEl nombre de la persona que te gusta tiene {n} letras")

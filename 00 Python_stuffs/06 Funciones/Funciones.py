# Funciones
# Funciones sin retorno de valor
def felizAidee():
    print('Feliz San Valentín mi pequeña Aideé bebé')

def saludar(nombre):
    print(f'Hola, Feliz San Valentín {nombre}')

def tablaMultiplicar(num):
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')

# Funciones con retorno de valor
def multiplicar(num1, num2):
    mult = num1 * num2
    return mult

saludar('Aideé')
felizAidee()
tablaMultiplicar(5)

print(multiplicar(5, 5))
from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

print('Creación objeto Cuadrado'.center(60, '-'))
cuadrado1 = Cuadrado(lado=25, color='Rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
# print(cuadrado1.color)
print(cuadrado1)
print(f'Calculo área: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
# print(Cuadrado.mro())

print('Creación objeto Rectangulo'.center(60, '-'))
rectangulo1 = Rectangulo(ancho=2, alto=5, color='Azul')
print(rectangulo1)
print(f'Calculo área: {rectangulo1.calcular_area()}')

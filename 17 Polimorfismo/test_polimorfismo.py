from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

empleado = Empleado('Pedro', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Aideé', 6000, 'Ambiental')
imprimir_detalles(gerente)
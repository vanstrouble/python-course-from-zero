'''
Abrir un documento sin usar el try exception
'''

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
#     print(archivo.read())

from manejo import ManejoArchivos


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

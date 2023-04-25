# Pasar diccionarios como argumentos de una función.

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE = 'Integrated Development Enviroment') # Podemos incluso no agregar nada sin error
listarTerminos(PK = 'Primary Key') 
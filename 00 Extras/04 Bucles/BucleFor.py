# Bucle for
"""
Sirve más que nada para recorrer arreglos, listas, etc.
"""

coleccion = {"Aideé": 23, "Pedro": 22, "Juan": 24}

for i in [1, 2, 3, 4, 5]:
    print(f'Elemento: {i}')

for clave, valor in coleccion.items():
    print(f'{clave} -> {valor}')

coleccion = 'Aideé Berenice'

for i in coleccion:
    print(f'{i}', end=' ')

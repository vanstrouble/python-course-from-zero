# Creación y eliminación de archivos
# c = open('chanchito.txt', 'a')

# c.write('\nAgregaremos una nueva lineal al archivo')

# c.close()

## Eliminar archivos o carpetas
import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
    print('Archivo eliminado')
else:
    print('El archivo no existe')
try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # Leer todo el archivo
    print(archivo.read())
except Exception as e:
    print('Hubo un erro {e}')
finally:
    archivo.close()

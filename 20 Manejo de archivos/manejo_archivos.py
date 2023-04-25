try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # El encoding es para que soporte los acentos
    archivo.write('Agregamos información al archivo:')
    archivo.write('\nAdiée es la niña más linda del mundo')
    archivo.write('\nEsta es una linea más')
    archivo.write('\nFinalizamos la últinma linea que quiero')
except Exception as e:
    print(e)
else:
    print('Archivo editado correctamente')
finally:
    archivo.close()

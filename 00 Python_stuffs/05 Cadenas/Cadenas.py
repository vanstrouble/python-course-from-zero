# Cadenas

cadena = 'Extraño a Aideé'

print(cadena)

cadena = 'Estoy \'estudiando\'' # Para usar las mismas comillas dentro de la cadena
print(cadena)

cadena = r"D:\nombre\trabajos"
print(cadena)

# Escritura multilinea, se utiliza también en el print
cadena = '''Hola
que tal? 
mi nombre es Pedro'''
print(cadena)

# Cadena de caracteres
cadena = 'Aideé Berenice'
print()
print(cadena)
print(cadena[0])
print(cadena[0:7])  # Slicing
print(len(cadena))

cadena = 'Hola mundo'.upper()
print('\n' + cadena)

cadena = 'Hola mundo'.lower()
print(cadena)

cadena = 'hola mundo'.capitalize()  # Poner la primera letra en mayuscula
print(cadena)

cadena = 'hola mundo'.title()   # Poner cada letra inicial en mayuscula
print(cadena)

cadena = 'hola mundo'.count('o')    # COntar caracteres
print(cadena)

cadena = 'hola mundo'.find('a') # Encontrar indice de caracteres o palabras
print(cadena)

cadena = 'hola mundo'.rfind('o') # Encontrar el último indice
print(cadena)

cadena = '1000'.isdigit()   # Comprobar si la cadena tiene solo digitos numericos
print(cadena)

cadena = 'AsbshUFb'.isalpha()   # Comproibar si solo son letras
print(cadena)

cadena = 'AHdbhjhsbjfwq1'.isalnum() # Comprobar si es alfanumerico
print(cadena)

cadena = 'hola mundo'.islower() # Verificar que todo este en minuscula
print(cadena)

cadena = 'hola mundo'.isupper() # Verificar si todo está en mayuscula
print(cadena)

cadena = 'hola mundo'.istitle() # Verificar si cada letra de inicio es mayuscula
print(cadena)

cadena = ' '.isspace() # Verificar si la cadena se compone de espacios
print(cadena)

cadena = 'hola mundo'.startswith('h') # Verificar si comienza con cierto caracter o palabra
print(cadena)

cadena = 'hola mundo'.endswith('o') # Verifica si termina con cierto caracter cadena
print(cadena)

cadena = 'hola mundo'.split() # Retorna una lista con los elementos de la cadena
print(cadena)

cadena = ','.join('Aideé') # Separar elementos d ela cadena con lo que indiquemos
print(cadena)

cadena = '   hola   '.strip() # Eliminar estacios o caracteres que indiquemos
print(cadena)

cadena = 'hola mundo'.replace('o', '0') # Remplazar caracteres o cadenas por lo que le indiquemos
print(cadena)

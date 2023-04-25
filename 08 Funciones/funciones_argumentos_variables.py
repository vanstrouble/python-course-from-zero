# Recorrer tuplas

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Aideé', 'Antonio', 'Berenice', 'Pedro')
listarNombres('Correa', 'Vázquez') # Tiene la ventaja de agregar argumentos
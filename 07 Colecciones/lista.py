nombres = ["Aideé", "Berenice", "Pedro", "Antonio"]
print(nombres)

# Conocer el largo de la lista
print(f"Numero de elemntos de la lista: {len(nombres)}")

# Acceder al elemento 0 o el primer elemento
print(nombres[0])

# Navegación inversa
print(nombres[-1])

# Imprimir rango de la lista
print(nombres[0:2]) # Menor que el elemento número 2

# Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3])

# Imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

# Cambiar los elementos
nombres[2] = "Correa"
print(nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)

# Revisar si un elemento de la lista existe
if "Pedro" in nombres:
    print("Pedro si existe en la lista")
else:
    print("El elemento buscado no existe en la lista")

# Agregar un nuevo elemento a la lista
nombres.append("Pedro")
print(nombres)

# Insertar un elemento en el indice proporcionado
nombres.insert(3, "Villegas")
print(nombres)

# Remover un elemento de la lista
nombres.remove("Antonio")
print(nombres)

# Remover el último elemento de la lista
nombres.pop()
print(nombres)

# Remover el índice indicado de la lista
del nombres[1]
print(nombres)

# Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar toda la lista
# del nombres
# print(nombres) # Da error porque no existe

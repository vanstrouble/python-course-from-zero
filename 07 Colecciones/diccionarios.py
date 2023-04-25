# Un diccionario está compuesto por una llave y un valor

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)

# Largo del diccionario
print(len(diccionario))

# Acceder a un elemento de un diccionario
print(diccionario["IDE"])
# Otra forma de acceder a los elementos
print(diccionario.get("IDE"))

# Modificando valores
diccionario["IDE"] = "Integrated development enviroment"
print(diccionario)

# Iterar los elementos
for termino in diccionario: # Obteniendo las llaves
    print(termino)
for termino in diccionario: # Obteniendo los valores
    print(diccionario[termino])

for valor in diccionario.values(): # Otra forma de acceder a los valores sin usar las llaves
    print(valor)

# Comprobar si un elemento existe en el diccionario
print("IDE" in diccionario)

# Agregar elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

# Remover elementos del diccionario
diccionario.pop("IDE")
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario

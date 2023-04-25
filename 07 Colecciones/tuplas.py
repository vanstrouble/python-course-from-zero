# Una tupla mantiene el orden , pero ya no se puede modificar
frutas = ("Mango", "Plátano", "Melon", "Sandía")
print(frutas)

# Largo de la tupla
print(f"Número de elementos de la lista: {len(frutas)}")

# Acceder a un elemento
print(frutas[0])

# Navegación inversa
print(frutas[-1]) # Último elemento de la tupla

# Rangos
print(frutas[0:2]) # Excluye el número 2

# Modificar tupla
frutasLista = list(frutas) # Convertimos la tupla en una lista
frutasLista[1] = "Manzana" # Modificamoes el elemento que queremos
frutas = tuple(frutasLista) # Volvemos a convertirla en tupla
print(frutas)

# Iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")

# No podemos agregar o eliminar elementos de una tupla
# Pero podemos eliminar la tupla completa
del frutas

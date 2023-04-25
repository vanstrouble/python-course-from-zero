# Set es una colección sin orden y sin índices, no permite elementos repetidos y los elementos no se 
# pueden modificar, pero si agregar nuevos o eliminar

planetas = {"Mercurio", "Venus", "Tierra", "Marte", "Júpiter"}
print(planetas)

# Largo del set
print(len(planetas))

# Revisar si hay un elemento dentro del set
print("Marte" in planetas)

# Agregar elementos | No se pueden egregar elementos duplicados
planetas.add("Saturno")
print(planetas)

# Eliminar elementos
planetas.remove("Tierra")
print(planetas)

# Eliminar con discard para no arrojar una excepción
planetas.discard("Neptuno")
print(planetas)

# Limpiar el set
planetas.clear()
print(planetas)

# Eliminar el set
del planetas

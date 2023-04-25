# Las funciones también pueden devolver valores
def suma(a = 0, b = 0): # Podemos agregar valores por defecto en caso de que no lo hagamos al llamar la funcion
    return a + b

print("El resultado es:", suma())
print("El resultado es:", suma(5, 4))

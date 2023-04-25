class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Modificar valores
Persona.nombre = "Aideé"
Persona.edad = 23

# Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

# Creación de un objeto
persona = Persona("Pedro", 22)

print(persona.nombre)
print(persona.edad)
print(id(persona))

# Creación de un segundo objeto
persona2 = Persona("José", 50)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))

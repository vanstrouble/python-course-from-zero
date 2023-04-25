class Persona:
    contador_persona = 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona
    
    def __init__(self, nombre, edad) -> None:
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self) -> str:
        return f'Persona [{self.id_persona} - {self.nombre}, {self.edad} años]'
    
persona1 = Persona('Aideé', 23)
print(persona1)
persona2 = Persona('Francis', 50)
print(persona2)
persona3 = Persona('José', 50)
print(persona3)

print(f'\nValor Contador Personas: {Persona.contador_persona}')
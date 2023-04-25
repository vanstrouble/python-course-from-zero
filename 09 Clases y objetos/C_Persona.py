class C_Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self.nombre} {self.apellido}, {self.edad} años')


persona1 = C_Persona('Aideé', 'Correa', 23)
persona1.mostrar_detalles()

persona2 = C_Persona('Pedro', 'Vázquez', 22)
persona2.mostrar_detalles()
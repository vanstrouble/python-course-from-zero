class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    """ Métodos Getter y Setter de los atributos de la clase"""
    # Método Getter
    @property
    def nombre(self): 
        return self._nombre

    # Método Setter     # Modo lectura: se debe eliminar el método Set
    @nombre.setter
    def nombre(self, nombre): 
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido}, {self._edad} años')

    def __del__(self):
        print(f'Persona eliminada: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('Aideé', 'Correa', 23)
    persona1.mostrar_detalles()

    persona1.nombre = 'Pedro'
    persona1.apellido = 'Vázquez'
    persona1.edad = 22
    persona1.mostrar_detalles()

    print(__name__)

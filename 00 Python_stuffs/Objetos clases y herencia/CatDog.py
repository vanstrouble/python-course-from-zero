class Animal:
    def __init__(self, nombre, onomatopeya) -> None:
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo,'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya) -> None:
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya) -> None:
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Gati', 'maullido')
gato.saludo()

perro = Perro('Smally', 'ladrido')
perro.saludo()

canario = Canario('Felipe', 'silvido')
canario.saludo()

class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def __str__(self) -> str:
        return f'Vehiculo: {self.marca}, {self.color}'

class Coche(Vehiculo):
    def __init__(self, marca, color, tipo, km):
        super().__init__(marca, color)
        self.tipo = tipo
        self.km = km

    def __str__(self):
        return f'{super().__str__()}, {self.tipo}, {self.km} KM recorridos'

class Bicicleta(Vehiculo):
    def __init__(self, marca, color, rodada):
        super().__init__(marca, color)
        self.rodada = rodada

    def __str__(self):
        return f'{super().__str__()}, {self.rodada} rodada'

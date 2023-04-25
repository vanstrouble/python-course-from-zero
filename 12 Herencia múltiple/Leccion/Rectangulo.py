from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color) -> None:
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
        
    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self) -> str:
        return f'Rectangulo {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

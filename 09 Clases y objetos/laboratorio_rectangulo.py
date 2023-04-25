class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
# Pedimos al usuario los datos correspondientes
base = float(input("Digite la base: "))
altura = float(input("Digite la altura: "))
# Creación del objeto con los datos del usuario
rectangulo = Rectangulo(base, altura)
# Visualización del resultado
print("El área del rectángulo es:", rectangulo.area())

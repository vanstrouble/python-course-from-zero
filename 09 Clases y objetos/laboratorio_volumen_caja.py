class Caja():
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    
    def calcular_volumen(self):
        return self.largo * self.ancho * self.alto
    
largo = float(input("Digite el largo de la caja: "))
ancho = float(input("Digite el ancho de la caja: "))
alto = float(input("Digite el alto de la caja: "))

caja = Caja(largo, ancho, alto)

print("El volumen de la caja es de: {} m^3".format(caja.calcular_volumen()))

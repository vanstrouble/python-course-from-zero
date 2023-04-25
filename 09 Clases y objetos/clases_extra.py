class Persona():
    def __init__(self, n, e, *v, **d): # Self es el equivalente a this
        self.nombre = n
        self.edad = e
        self.valores = v
        self.diccionario = d
        
    def desplegar(self): # No se puede mezclar self y this. Solo usa uno
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Valores (Tupla):", self.valores)
        print("Diccionario", self.diccionario)
        
p1 = Persona("Aideé", 22)
p1.desplegar()

p2 = Persona("Berenice", 22, 1, 3, 4)
p2.desplegar()

p3 = Persona("Pedro", 22, 1, 3, 4, m = "Manzana", p = "Pera", j = "Jicama")
p3.desplegar()
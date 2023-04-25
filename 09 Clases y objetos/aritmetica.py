class Aritmetica():
    """ Clase Aritmetica para realizar las operaciones básicas """
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self): 
        """ Se realiza la operación con los atributos de la clase """
        return self.operando1 + self.operando2
    
    def restar(self): 
        """ Se realiza la operación con los atributos de la clase """
        return self.operando1 - self.operando2
    
    def multiplicar(self): 
        """ Se realiza la operación con los atributos de la clase """
        return self.operando1 * self.operando2
    
    def dividir(self): 
        """ Se realiza la operación con los atributos de la clase """
        return self.operando1 / self.operando2
        
# Creación de un nuevo objeto
aritmetica = Aritmetica(2, 4)
aritmetica2 = Aritmetica(4, 2)
aritmetica3 = Aritmetica(9, 5)
# Visualización de las operaciones
print("Resultado de la suma:", aritmetica.sumar())
print("Resultado de la resta:", aritmetica.restar())
print("Resultado de la multiplicación:", aritmetica3.multiplicar())
print("Resultado de la división:", aritmetica2.dividir())

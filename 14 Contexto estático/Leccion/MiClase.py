class MiClase:
    
    variable_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
        
    # Metodo estático
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
  
    # Metodo de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
        
MiClase.metodo_estatico()
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

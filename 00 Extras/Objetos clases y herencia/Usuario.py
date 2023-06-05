class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola! Mi nombre es", self.nombre, self.apellido)


class Admin(Usuario):
    def superSaludo(self):
        print("Hola! Me llamo", self.nombre, 'soy administrador' )

usuario = Usuario('Aideé', 'Correa')
usuario.saludo()

usuario.nombre = 'Berenice'
usuario.saludo()

admin = Admin('Aideé', 'Virgen')
admin.saludo()
admin.superSaludo()

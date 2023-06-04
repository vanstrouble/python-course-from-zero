# Atributos públicos, protegidos y privados

class My_Class:
    def __init__(self, publico, protegido, privado) -> None:
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = My_Class('Valor Público', 'Valor Protegido', 'Valor Privado', )

# Acceso al atributo público
print(objeto.publico)
# Modificar el atributo público
objeto.publico = 'Nuevo valor público'
print(objeto.publico)

# Acceso valor protegido
print(objeto._protegido)
# Modificar el atributo protegido
objeto._protegido = 'Nuevo valor protegido'
print(objeto._protegido)

# Atributo privado
# print(objeto.__privado)  # No se puede acceder
# Pero se puede acceder de la siguiente manera
print(objeto._My_Class__privado)
# Modificar el atributo privado
objeto._My_Class__privado = 'Nuevo valor privado'
print(objeto._My_Class__privado)

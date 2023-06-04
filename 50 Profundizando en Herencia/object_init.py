# Orden de inicialización de objetos
class Father:
    def __init__(self) -> None:
        print('Inicializador Padre')

    def class_method(self):
        print('Método Padre')


class Children(Father):
    # Se llama el método init de la clase padre
    # siempre y cuando la clase hija no defina su propio init
    def __init__(self) -> None:
        super().__init__()  # Inicializar de la clase padre
        print('Inicializando hijo')

    def class_method(self):
        super().class_method()
        print('Método hijo')


# father1 = Father()
# father1.class_method()
child1 = Children()
child1.class_method()

#  Ejemplo de herencia simple
class Simple_List(object):
    def __init__(self, elements) -> None:
        self._elements = list(elements)

    def add(self, element):
        self._elements.append(element)

    def __getitem__(self, index):
        return self._elements[index]

    def order(self):
        self._elements.sort()

    def __len__(self):
        return len(self._elements)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._elements!r})'


class Sorted_List(Simple_List):
    def __init__(self, elements=[]) -> None:
        super().__init__(elements)
        # Ordenamos siempre los elementos una vez inicializados
        self.order()

    def add(self, element):
        super().add(element)
        # Ordenamos el nuevo elemento
        self.order()


class Integer_List(Simple_List):
    def __init__(self, elements) -> None:
        [self._validate(element) for element in elements]
        # Validados los elementos podemos agregarlos
        super().__init__(elements)

    def _validate(self, element):
        # Validamos que el elemento sea de tipo entero
        if not isinstance(element, int):
            raise ValueError(f'No es un valor entero: {element}')

    # Sobreescribimos el método agregar de la clase padre
    def add(self, element):
        self._validate(element)
        # Una vez validado, lo agregamos
        super().add(element)


class IntegerOrderedSet(Integer_List, Sorted_List):
    pass



# Lista simple
simple_list = Simple_List([10, 9, 12, 4, 5, 20, 22, 1])
print(simple_list)
# Lista ordenada
sorted_list = Sorted_List([4, 2, 7, 1, 16, 20, 3, 6, 9])
print(sorted_list)
sorted_list.add(-14)
print(sorted_list)
print(len(sorted_list))

# Lista de enteros
int_list = Integer_List([10, 1, 2, -17, 4, -3])
print(int_list)
int_list.add(8)
print(int_list)

# Lista de enteros ordenada
int_sort_list = IntegerOrderedSet([1, 5, 10, 23, 4, 7, 0, -1, -37])
print(int_sort_list)
int_sort_list.add(-22)
print(int_sort_list)

# Saber las clases padre y su orden
print(IntegerOrderedSet.__bases__)

# MRO - Method Resolution Order
print(IntegerOrderedSet.__mro__)

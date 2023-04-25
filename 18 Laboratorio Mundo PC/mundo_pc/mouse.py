from dispositivo_entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    cont_mouse = 0
    def __init__(self, marca, tipo_entrada) -> None:
        Mouse.cont_mouse += 1
        self._id_mouse = Mouse.cont_mouse
        super().__init__(marca, tipo_entrada)

    def __str__(self) -> str:
        return f'\nID: {self._id_mouse} \nMarca: {self._marca} \nEntrada: {self._tipo_entrada}\n'


if __name__ == '__main__':
    mouse = Mouse('RAZER', 'USB')
    print(mouse)

    mouse2 = Mouse('LOGITECH', 'USB')
    print(mouse2)

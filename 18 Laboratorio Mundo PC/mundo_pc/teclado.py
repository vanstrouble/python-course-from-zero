from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    cont_teclado = 0
    def __init__(self, marca, tipo_entrada) -> None:
        Teclado.cont_teclado += 1
        self._id_teclado = Teclado.cont_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self) -> str:
        return f'\nID: {self._id_teclado} \nMarca: {self._marca} \nEntrada: {self._tipo_entrada}\n'


if __name__ == '__main__':
    teclado1 = Teclado('Apple', 'Inalambrico')
    teclado2 = Teclado('LOGITECH', 'USB')
    print(teclado1, teclado2)

from teclado import Teclado
from monitor import Monitor
from mouse import Mouse


class Computadora:
    cont_computadora = 0

    def __init__(self, nombre, monitor, teclado, mouse) -> None:
        Computadora.cont_computadora += 1
        self._id_computadora = Computadora.cont_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    def __str__(self) -> str:
        return f'''
        {self._id_computadora}: {self._nombre}\n
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Mouse: {self._mouse}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('RAZER', 'Bluetooth')
    monitor1 = Monitor('SAMSUNG', 27)
    mouse1 = Mouse('LOGITECH', 'USB')
    computadora1 = Computadora('La mamalona', monitor1, teclado1, mouse1)
    print(computadora1)

    teclado2 = Teclado('LOGITECH', 'USB C')
    monitor2 = Monitor('BENQ', 32)
    mouse2 = Mouse('RAZER', 'USB')
    computadora2 = Computadora(
        'Destructora de mundos',
        monitor2,
        teclado2,
        mouse2)
    print(computadora2)

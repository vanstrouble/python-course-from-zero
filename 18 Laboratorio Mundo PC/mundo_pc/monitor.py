class Monitor:
    cont_monitor = 0

    def __init__(self, marca, size) -> None:
        Monitor.cont_monitor += 1
        self._id_monitor = Monitor.cont_monitor
        self._marca = marca
        self._tamanio = size

    def __str__(self) -> str:
        return f'\nID: {self._id_monitor} \nMarca: {self._marca} \nTamaño: {self._tamanio} pulgadas\n'


if __name__ == '__main__':
    monitor1 = Monitor('SAMSUNG', 27)
    monitor2 = Monitor('BENQ', 32)
    print(monitor1, monitor2)

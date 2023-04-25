from orden import Orden
from computadora import Computadora
from mouse import Mouse
from monitor import Monitor
from teclado import Teclado


teclado1 = Teclado('RAZER', 'Bluetooth')
monitor1 = Monitor('SAMSUNG', 27)
mouse1 = Mouse('LOGITECH', 'USB')
computadora1 = Computadora('La mamalona', monitor1, teclado1, mouse1)

teclado2 = Teclado('LOGITECH', 'USB C')
monitor2 = Monitor('BENQ', 32)
mouse2 = Mouse('RAZER', 'USB')
computadora2 = Computadora('Destructora de mundos', monitor2, teclado2, mouse2)


teclado3 = Teclado('LOGITECH', 'USB')
monitor3 = Monitor('BENQ', 27)
mouse3 = Mouse('RAZER', 'USB')
computadora3 = Computadora('Tu mamá', monitor3, teclado3, mouse3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

computadoras1 = [computadora2, computadora3]
orden2 = Orden(computadoras1)

print(orden1)

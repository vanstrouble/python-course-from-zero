'''
Ejercicio 4
Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia
'''
import math

print("\t.:CALCULAR ÁREA Y LONGITUD DE UN CIRCULO CON SU RADIO:.\n")

radio = float(input("Digite el radio del circulo: "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"\nÁrea del circulo: {area:.2f}")
print(f"Longitud de la circunferencia: {longitud:.2f}")

# ¿Cuánto te gusta el queso

titulo = "Bienvenido al Test del Queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Qué haces cuando ves una tabla de quesos?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos e incluso varios\n"
               "C - No puedo evitar devorarla\n"
               "Opcion: ")

opcion = opcion.lower()

if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 2: ¿Cómo te gustan las hamburguesas?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n"
               "Opción: ")

opcion = opcion.lower()

if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n"
               "Opción: ")

opcion = opcion.lower()

if opcion == "a":
    puntuacion += 0
elif opcion == "b":
    puntuacion += 5
elif opcion == "c":
    puntuacion += 10
else:
    print("Las opciones posibles son A, B y C")
    exit()

if puntuacion >= 25:
    print("Resultado: ¡¡ Felicidades, eres fanático de los quesos :D !!")
elif puntuacion >= 15:
    print("Resultado: Felicidades, eres una persona que le gusta el queso :)")
else:
    print("Resultado: Lástima, no te gusta el queso")

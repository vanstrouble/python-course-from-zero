from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 95

TAMAÑO_BARRA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Empiezan los turnos del combate

    # Turno de pikachu
    print("\nTurno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("\nPikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("\nPikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    # print(f"\nLa vida de Pikachu es: {vida_pikachu}\nLa vida de Squirtle es: {vida_squirtle}")

    barra_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print(f"\nPikachu:    [{'*' * barra_vida_pikachu}{' ' * (TAMAÑO_BARRA_VIDA - barra_vida_pikachu)}] ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")

    barra_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print(f"Squirtle:    [{'*' * barra_vida_squirtle}{' ' * (TAMAÑO_BARRA_VIDA - barra_vida_squirtle)}] ({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})")

    # input("Enter para continuar\n\n")
    os.system("clear")

    # Turno Squirtle
    print("\nTurno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["a", "b", "c", "d"]:
        ataque_squirtle = input("\n¿Qué ataque te gustaria realizar?\n"
                                "[A] - Placaje\t"
                                "[B] - Pistola Agua\t"
                                "[C] - Burbuja\t"
                                "[D] - No hacer nada\n"
                                "Opción: ")
        ataque_squirtle = ataque_squirtle.lower()

    if ataque_squirtle == "a":
        print("\nSquirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "b":
        print("\nSquirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "c":
        print("\nSquirtle ataca con Busbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "d":
        print("\nSquirtle no hace nada")

    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

    # print(f"\nLa vida de Pikachu es: {vida_pikachu}\nLa vida de Squirtle es: {vida_squirtle}")
    barra_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
    print(f"\nPikachu:    [{'*' * barra_vida_pikachu}{' ' * (TAMAÑO_BARRA_VIDA - barra_vida_pikachu)}] ({vida_pikachu}/{VIDA_INICIAL_PIKACHU})")

    barra_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print(f"Squirtle:    [{'*' * barra_vida_squirtle}{' ' * (TAMAÑO_BARRA_VIDA - barra_vida_squirtle)}] ({vida_squirtle}/{VIDA_INICIAL_SQUIRTLE})")

    # input("Enter para continuar\n\n")
    os.system("clear")

if vida_pikachu > vida_squirtle:
    print("\n¡Pikachu gana!")
else:
    print("\n¡Squirtle gana!")

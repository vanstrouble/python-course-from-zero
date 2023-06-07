print("\nTe ayudaré a elegir un móvil nuevo\n"
      "Empecemos...\n")

opcion = input("¿Te gusta más Android o IOS?\n"
               "A - Android\n"
               "B - IOS\n"
               "Opción: ")
opcion = opcion.lower()

if opcion == "a":
    opcion = input("¿Tienes dinero?\n"
                   "S - Si\n"
                   "N - No\n"
                   "Opción: ")
    opcion = opcion.lower()

    if opcion == "s":
        opcion = input("¿Te importa la cámara del móvil?\n"
                       "S - Si\n"
                       "N - No\n"
                       "Opción: ")
        opcion = opcion.lower()

        if opcion == "s":
            print("\nTu mejor opción es: Google Pixel Supercamara")

        elif opcion == "n":
            print("\nTu mejor opción es: Android calidad - precio")

        else:
            print("\nNo digitó una opción válida")

    elif opcion == "n":
        print("\nTu mejor opción es: Android del OXXO")

    else:
        print("\nNo digitó una opción válida")

elif opcion == "b":
    opcion = input("¿Tienes dinero?\n"
                   "S - Si\n"
                   "N - No\n"
                   "Opción: ")
    opcion = opcion.lower()

    if opcion == "s":
        print("\nTu mejor opción es: iPhone Ultra Pro")

    elif opcion == "n":
        print("\nTu mejor opción es: iPhone de segunda mano")

    else:
        print("\nNo digitó una opción válida")

else:
    print("\nNo digitó una opción válida")

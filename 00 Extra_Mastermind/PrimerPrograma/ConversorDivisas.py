# Conversor de euros a pesos mexicanos

dolar_euro = 0.84
dolar_peso = 20.67

opc = input("Elija la conversión\n"
            "A - Convertir de dolar a euro\n"
            "B - Convertir de euro a dolar\n"
            "C - Convertir de dolar a peso mexicano\n"
            "D - Convertir de peso mexicano a dolar\n"
            "Opción: ")
opc = opc.lower()

texto_usuario = "Digite la cantidad de {} a convertir: "

if opc == "a":
    cantidad_dinero = float(input(texto_usuario.format("dolares")))
    print(f"La cantidad en euros es: {cantidad_dinero * dolar_euro}")
elif opc == "b":
    cantidad_dinero = float(input(texto_usuario.format("euros")))
    print(f"La cantidad en dolares es: {cantidad_dinero / dolar_euro}")
elif opc == "c":
    cantidad_dinero = float(input(texto_usuario.format("dolares")))
    print(f"La cantidad en pesos es: {cantidad_dinero * dolar_peso}")
elif opc == "d":
    cantidad_dinero = float(input(texto_usuario.format("pesos")))
    print(f"La cantidad en dolares es: {cantidad_dinero / dolar_peso}")
else:
    print("\nLas opciones válidas son A, B, C y D")

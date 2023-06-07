# Lista de la compra

producto = None
lista_compra = []

print("Programa lista de la compra\n")

while True:
    producto = input("¿Qué desea comprar? ([Q] para salir): ")
    if producto == "Q" or producto == "q":
        break
    elif producto in lista_compra:
        print(f"{producto} ya está en la lista.")
    else:
        if input(f"¿Seguro que quieres añadir {producto} a la lista? [S/N]: ") == "S":
            lista_compra.append(producto)

print("La lista de la compra es:")
for producto in lista_compra:
    print(producto)

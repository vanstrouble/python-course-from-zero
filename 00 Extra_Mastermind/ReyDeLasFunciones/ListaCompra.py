ARCHIVO_LISTA = "Lista compra.txt"


def ask_user():
    return input(f"Introduce un producto [Salir parta terminar]: ")


def save_list(lista_compra):
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def save_item_list(lista_compra, item_to_save):
    if item_to_save.lower() in [a.lower() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(item_to_save)


def load_or_create_archive():
    lista_compra = []
    if input("¿Quieres cargar la última lista de la compra? [S/N]: ") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo de la compra no encontrado")
    return lista_compra


def show_list(lista_compra):
    print("\n".join(lista_compra))


def main():
    lista_compra = load_or_create_archive()
    producto = ask_user()

    while producto != "Salir":
        save_item_list(lista_compra, producto)
        print("\n".join(lista_compra))
        producto = ask_user()
    show_list(lista_compra)
    save_list(lista_compra)


if __name__ == '__main__':
    main()

print("Proporcione los siguientes datos del libro:\n")
nombre_libro = input("Introduzca el nombre: ")
id_libro = int(input("Digita el ID: "))
precio_libro = float(input("Digita el precio: "))
envio_gratuito = input("Indica si el envio es gratuito (S/N): ")

if envio_gratuito == "S" or envio_gratuito == "s":
    envio_gratuito = True
elif envio_gratuito == "N" or envio_gratuito == "n":
    envio_gratuito = False
else:
    envio_gratuito = "Valor incorrecto. Debe ser True o False"

print(f"\nNombre: {nombre_libro}\n"
      f"ID: {id_libro}\n"
      f"Precio: {precio_libro}\n"
      f"Envío gratuito: {envio_gratuito}")

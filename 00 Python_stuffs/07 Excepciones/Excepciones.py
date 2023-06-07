# Excepciones

# while True:
#     try:
#         numero = int(input("Digite un número: "))
#         print(f"La suma es: {numero + 10}")
#     except:
#         print("\nHa ocurrido un error. Digite un valor númerico\n") # En caso de que salga un error
#     else:
#         print("Programa finalizado correctamente") # Si se ejecuta correctamente el try le sigue el else
#         break
#     finally:
#         print("\t\tIteración finalizada") # Se ejecuta siempre después de cada iteración

# print("___________________________________")



# def dividir():
#     while True:
#         try:
#             num1 = float(input("Digite un número: "))
#             num2 = float(input("Digite un número: "))
#             resultado = num1 / num2
#             print(f"El resultado de la división es: {resultado:.2f}")
#         except ValueError:
#             print("Error. Digite únicamente valores numéricos")
#         except ZeroDivisionError:
#         else:
#             break

# dividir()



# Lanzar nuestras propias excepciones
def verificarEdad(edad):
    if edad < 0: # Si la edad es negativa
        raise ValueError ("La edad no puede ser negativa")
    elif edad < 18:
        print("Eres ilegal")
    elif edad < 30:
        print("Eres un jovén")
    elif edad < 50:
        print("Osos maduros")

edad = int(input("Digite su edad: "))

try:
    verificarEdad(edad)
except ValueError as EdadNegativa:
    print(EdadNegativa)

print("\nPrograma terminado")

# Profundizando listas

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# sorted built-in
# help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
# ordenar de manera descendente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
# Ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1, key=len)
print(nombres1)
# built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))

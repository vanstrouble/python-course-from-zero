numbers = range(10)
pairs_list = []

# Crearmos una nueva lista con los valores pares multiplicados por sí mismos
for number in numbers:
    if number % 2 == 0:
        pairs_list.append(number*number)

print(f'Pairs list: {pairs_list}')

# Hacemos lo mismo con list comprehensions
# [empression for variable in collection in condition]
# La condición de if es opcional
pairs_list = [number*number for number in numbers if number % 2 == 0]
print(f'Pairs list with List comprehensions: {pairs_list}')

# Ejemplo con 2 condiciones (opcionales)
# Debe de ser un número divisible entre 2 y 6
pairs_list = [number for number in numbers if number % 2 == 0 and number % 6 == 0]
print(f'Pairs list with List comprehensions (divisible by 2 and 6): {pairs_list}')

# Agregando if else
pairs_list = []
odds_list = []

for number in range(10):
    if number % 2 == 0:
        pairs_list.append(number)
    else:
        odds_list.append(number)

print(f'Pairs: {pairs_list}')
print(f'Odds: {odds_list}')

# El mismo ejercicio con list comprehesions
pairs_list = []
odds_list = []
[pairs_list.append(number) if number % 2 == 0 else odds_list.append(number) for number in numbers]

print(f'Pairs with list comprehensions: {pairs_list}')
print(f'Odds with list comprehensions: {odds_list}')

# Listas de listas a lista simple con list comprehensions
list_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

simple_list = [value for sublist in list_list for value in sublist]
print(f'Sublist: {simple_list}')

# Creamos una lista de pares a partir de la lista de listas
# Sin list comprehensions (for anidados)
pairs_list = []
for sublist in list_list:
    for value in sublist:
        if value % 2 == 0:
            pairs_list.append(value)
print(f'Pairs: {pairs_list}')

# Usando list comprehensions
pairs_list = [value for sublist in list_list for value in sublist if value % 2 == 0]
print(f'Pairs with list comprehensions: {pairs_list}')

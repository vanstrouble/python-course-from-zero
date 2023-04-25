# Generador de números del 1 al 5
def numeric_generator():
    for number in range(1, 6):
        yield number
        print('Se reanuda la ejecución')

# Utilizamos el generador
gen = numeric_generator()
print(f'Objeto generador: {gen}, tipo: {type(gen)}\n')

# Consumimos los valores del generador
for value in gen:
    print(f'Número producido: {value}')

# Consumir a demanda 
gen = numeric_generator()
try:
    
    print(f'\nConsumimos a demanda: {next(gen)}')
    print(f'\nConsumimos a demanda: {next(gen)}')
    print(f'\nConsumimos a demanda: {next(gen)}')
    print(f'\nConsumimos a demanda: {next(gen)}')
    print(f'\nConsumimos a demanda: {next(gen)}')
    print(f'\nConsumimos a demanda: {next(gen)}')
except StopIteration as e:
    print(f'Error al consumir generador: {e}')

# otra forma de consumir un generador
gen = numeric_generator()
print()
while True:    
    try:
        value = next(gen)
        print(f'Valor generador: {value}')
    except Exception as e:
        print('Se terminó de iterar el generador')
        break

# Generators
# Es una función especial en Python que retorna una secuencia de valores 
# suspende la ejecución de la función yield (producir) (no se puede usar return)

def generator():
    yield 1
    print('Se reanuda la ejecución')
    yield 2    
    print('Se reanuda la ejecución')
    yield 3    

# Consumimos el generador a demanda
gen = generator()
# Con cada llamda consumimos un valor 
print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir más valores de los que produce el generador 
# lanza un error de StopIteration
print()
# Consumiendo los valores con un ciclo for
for value in generator():
    print(f'Número generado: {value}')

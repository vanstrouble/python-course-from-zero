# Funciones Recursivas

def cuentaRegresiva(num):
    if num > 0:
        print(num)
        cuentaRegresiva(num - 1)
    else:
        print('Boooom!!! Todos han muerto')

num = int(input('Digite el número: '))
cuentaRegresiva(num)

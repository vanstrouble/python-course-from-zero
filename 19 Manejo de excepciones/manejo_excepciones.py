from NumerosIdenticosException import NumerosIdenticosException


resultado = None

try:
    a = int(input('Digite el primer digito: '))
    b = int(input('Digite el primer digito: '))

    if a == b:
        raise NumerosIdenticosException('Números Identicos')

    resultado = a / b
except Exception as e:  # Exception es la clase padre y con ello capturamos todos los errores
    print(f'Ocurrio un error: {e}, {type(e)}')
else:
    print('Cálculo sin errores')


print(f'Resultado = {resultado}')
print('Programa finalizado correctamente')

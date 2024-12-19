from contextlib import contextmanager

# Esta es la forma correcta de crear un archivo y escribir en él
with open('55 Tips/testing.txt', 'w') as file:
    file.write('Hello from Python!')


# Manejo de context manager en clases
# 1. Implementar protocolo con las funciones __enter__ y __exit__
# 2. Usar la clase contextlib.contextmanager

# Opcion 1
class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'a')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


@contextmanager
def file_manager(name):
    try:
        file = open(name, 'a')
        yield file
    finally:
        file.close()


if __name__ == '__main__':
    # Test opcion 1
    with MyContextManager('55 Tips/testing.txt') as file:
        file.write('\nHello from Class!')

    # Test opcion 2
    with file_manager('55 Tips/testing.txt') as file:
        file.write('\nHello from Function!')

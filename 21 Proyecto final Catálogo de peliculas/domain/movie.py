class Movie:
    def __init__(self, name) -> None:
        self._name = name

    def __str__(self):
        return f'Pelicula: {self._name}'

    # Get method
    @property
    def name(self):
        return self._name

    # Set method
    @name.setter
    def name(self, name):
        self._name = name

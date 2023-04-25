import os


class MovieCatalog:
    path = '21 Proyecto final Catálogo de peliculas/movies.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.path, 'a', encoding='utf-8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def get_movies(cls):
        with open(cls.path, 'r', encoding='utf-8') as file:
            print('')
            print('Catalogo de películas'.center(50, '-'))
            print(file.read())

    @classmethod
    def drop_movies(cls):
        os.remove(cls.path)
        print(f'Archivo eliminado {cls.path}')

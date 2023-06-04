from domain.movie import Movie
from service.movie_catalog import MovieCatalog as mc


option = None
while option != 4:
    try:
        print('MENÚ DE OPCIONES'.center(50, '-'))
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar archivo de Películas')
        print('4. Salir')
        option = int(input('Opción (1-4): '))

        if option == 1:
            movie_name = input('\nIngresa el nombre de la película: ')
            movie = Movie(movie_name)
            mc.add_movie(movie)
        elif option == 2:
            mc.get_movies()
        elif option == 3:
            mc.drop_movies()

    except Exception as e:
        print(f'\nError: {e}')
else:
    print('\nSaliendo… No vuelva pronto')

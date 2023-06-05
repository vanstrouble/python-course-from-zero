def print_triangle(rows):
    for i in range(1, rows + 1, 2):
        spaces = (rows - i) // 2
        for _ in range(0, spaces):
            print('', end='')
        for _ in range(0, i):
            print('*', end='')
        print('\n')


def triangle(rows):
    for i in range(1, rows * 2, 2):
        print(('*' * i).center(rows * 2))


triangle(5)

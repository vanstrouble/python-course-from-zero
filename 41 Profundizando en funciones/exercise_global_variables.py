# Definimos variable global

count = 0


def show_count():
    print(count)


def update_count(c):
    global count
    count = c


update_count(5)
show_count()

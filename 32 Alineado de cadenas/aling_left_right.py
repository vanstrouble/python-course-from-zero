# Alinear cadenas

# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(10,'*'))
# print(len(titulo.center(50,'*')))
print(titulo.center(len(titulo) + 10, '-'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo) + 10, '-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo) + 10, '-'))

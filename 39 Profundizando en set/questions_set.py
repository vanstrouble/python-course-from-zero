# Profundizar en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables

# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'María'}
# Todos con ojos_cafe y pelo rubio (Union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# (intersetion) Sólo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# (difference) Pelo negro sin ojos cafe (no es conmutativa)
# las personas que se encuentran en el primer set pero NO en el segundo
print(pelo_negro.difference(ojos_cafe))

# (diferencia simétrica) Pelo negro u ojos cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set está contenido en otro (subset)
# revismos si los elementos del primer set están contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set están contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))

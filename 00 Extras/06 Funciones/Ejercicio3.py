"""
Ejercicio 3
Crear un programa que tenga una lista de clientes, cada cliente tiene su 
Nombre, Apellido y DNI. El programa tendrá el siguiente menú de opciones: 
1. Agregar nuevo cliente
2. Mostrar todos los clientes 
3. Mostrar cliente por DNI
4. Eliminar cliente 
5. Salir
"""
def agregarCliente(clientes, nombre, apellido, dni):
    cliente = {}
    if {'Nombre':nombre,'Apellido':apellido,'DNI':dni} not in clientes:
        cliente['Nombre'] = nombre
        cliente['Apellido'] = apellido
        cliente['DNI'] = dni
        clientes.append(cliente)
        print('\nCliente agregado con éxito')
    elif {'Nombre':nombre,'Apellido':apellido,'DNI':dni} in clientes:
        print("\nCliente ya existe en la lista. Digite otro DNI\n")

def mostrarClientes(clientes):
    for i in clientes:
        print(f'Nombre: {i["Nombre"]}, Apellido: {i["Apellido"]}, DNI: {i["DNI"]}')

def mostrarCliente(clientes, dni):
    for i in clientes:
        if i['DNI'] == dni:
            print(f'Nombre: {i["Nombre"]}, Apellido: {i["Apellido"]}, DNI: {i["DNI"]}')
            return True
    return False

def eliminarCliente(clientes, dno):
    for i in clientes:
        if i['DNI'] == dni:
            clientes.remove(i)
            return True
    return False

clientes = [] 

while True:
    print("""\t.:MENÚ:.
1. Agregar nuevo cliente
2. Mostrar todos los clientes 
3. Mostrar cliente por DNI
4. Eliminar cliente 
5. Salir
""")
    opcion = int(input('Opción: '))

    print()

    if opcion == 1:
        nombre = input('\tNombre del cliente: ')
        apellido = input('\tApellido del cliente: ')
        dni = input('\tDNI del cliente: ')
        agregarCliente(clientes, nombre, apellido, dni)
    elif opcion == 2:
        if len(clientes) == 0:
            print("\n\tLa lista de clientes esta vacía")
        elif len(clientes) != 0:
            mostrarClientes(clientes)
        print()
    elif opcion == 3:
        dni = input('\tDNI del cliente: ')
        if mostrarCliente(clientes, dni):
            print('\nCliente encontrado')
        else:
            print('\nCliente NO encontrado')
    elif opcion == 4:
        dni = input('\tDNI del cliente: ')
        if eliminarCliente(clientes, dni):
            print('\nCliente eliminado')
        else: 
            print('\nCliente NO encontrado')
    elif opcion == 5:
        break
    else:
        print('\nDigite una opción válida\n')

    print()

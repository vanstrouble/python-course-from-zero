"""
Ejercicio 10
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave
sea el nombre del usuario y el valor sea el teléfono, el programa tendrá el siguiente
menú de opciones:
    1. nuevo contacto
    2. Borrar contacto
    3. Ver contactos existentes
    4. Salir
"""
agenda = {}

print('\t.::AGENDA DE CONTACTOS::.')
while True:
    print('\n\t.:MENÚ:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opc = int(input('Digite la opción: '))

    if opc == 1:
        nombre = input('\nNombre del contacto: ')
        telefono = input('Número de telefono: ')

        if nombre not in agenda:
            agenda[nombre] = telefono
            print('\n\tContacto agregado correctamente')
        else:
            print('\n\tContacto ya existente')
    elif opc == 2:
        nombre = input('\nNombre del contacto: ')
        if nombre in agenda:
            del(agenda[nombre])
            print('\n\tContacto eliminado correctamente')
        else:
            print('El contacto no existe')
    elif opc == 3:
        print('\n\tAgenda de contactos: ')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')
    elif opc == 4:
        print('\nGracias por usar su agenda de contactos')
        break
    else:
        print('\nElija una opción válida')

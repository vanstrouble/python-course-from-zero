from dao_user import DAO_User
from user import User
from logger import log


opt = None
while opt != 5:
    print('\n\t.:MENÚ:.')
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Insertar usuarios')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opt = int(input('Digita la opción [1-5]: '))

    if opt == 1:
        print('\nLISTADO DE USUARIOS')
        users = DAO_User.select()
        for user in users:
            log.info(user)
    elif opt == 2:
        print('\nREGISTRO DE USUARIO')
        username = input('Username: ')
        password = input('Password: ')
        user = User(username=username, password=password)
        inserted_users = DAO_User.insert(user)
        log.info(f'Usuarios insertados: {inserted_users}')
    elif opt == 3:
        print('\nMODIFICACIÓN DE USUARIO')
        id_user = int(input('Digita el id_user a modificar: '))
        username = input('Username: ')
        password = input('Password: ')
        user = User(id_user=id_user, username=username, password=password)
        updated_users = DAO_User.update(user)
        log.info(f'Usuarios actualizados: {updated_users}')
    elif opt == 4:
        print('\nELIMINACIÓN DE USUARIO')
        id_user = int(input('Digita el id_user a eliminar: '))
        user = User(id_user=id_user)
        deleted_users = DAO_User.delete(user)
        log.info(f'Usuarios eliminados: {deleted_users}')
else:
    print('\n')
    log.info('Saliendo de la aplicación…')

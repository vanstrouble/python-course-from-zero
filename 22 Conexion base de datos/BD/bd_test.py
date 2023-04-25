import psycopg2


connection = psycopg2.connect(
    user='vanstrouble',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
)

# print(connection)  # Connection test

# Retrieve all records from database
try:
    with connection:
        with connection.cursor() as cursor:
            sentence = 'SELECT * FROM users'
            cursor.execute(sentence)
            records = cursor.fetchall()
            print(records)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    connection.close()

# # Retrieve one record
# try:
#     with connection:
#         with connection.cursor() as cursor:
#             sentence = 'SELECT * FROM users WHERE id_user = %s'
#             entry = input('Proporciona el ID: ')  # noqa: E501
#             cursor.execute(sentence, (entry,))
#             records = cursor.fetchone()
#             print(records)
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     connection.close()

# # Return multiple records
# try:
#     with connection:
#         with connection.cursor() as cursor:
#             sentence = 'SELECT name, last_name FROM users WHERE id_user IN %s'  # noqa: E501
#             entry = input('Proporciona los id\'s a buscar (separado por comas): ')  # noqa: E501
#             primary_keys = (tuple(entry.split(',')),)  # Must be a tuple of tuple  # noqa: E501
#             cursor.execute(sentence, primary_keys)
#             records = cursor.fetchall()
#             print(records)
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     connection.close()

# # Add multiple records
# try:
#     with connection:
#         with connection.cursor() as cursor:
#             count = 0
#             while True:
#                 sentence = 'INSERT INTO users (fist_name, sec_name, last_name, birthdate) VALUES (%s, %s, %s)'  # noqa: E501
#                 first_name = input('Primer nombre: ')
#                 sec_name = input('Segundo nombre: ')
#                 last_name = input('Apellido: ')
#                 birthday = input('Día de nacimiento (dd): ')
#                 birthmonth = input('Mes de nacimiento (MM): ')
#                 birthyear = input('Año de nacimiento (yyyy): ')

#                 birthdate = f'{birthyear}-{birthmonth}-{birthday}'
#                 values = (first_name, sec_name, last_name, birthdate)  # Must be a tuple of tuple # noqa: E501
#                 cursor.execute(sentence, values)
#                 count += 1
#                 o = input('¿Añadir otro registro? (Y/N): ')
#                 if o == 'y' or o == 'Y':
#                     print('')
#                 elif (o == 'n') or (o == 'N'):
#                     break
#                 else:
#                     print('Error. Digite una opción válidad')
#             print(f'\nRegistros insertados: {count}')
# except Exception as e:
#     print(f'Error: {e}')
# finally:
#     connection.close()

import psycopg2 as db


connection = db.connect(
    user='vanstrouble',
    password='admin',
    host='localhost',
    port='5432',
    database='test'
)

'''
Manual way to manage the transactions
Note: Using "with" prevents us from doing all this
'''
try:
    connection.autocommit = False

    cur = connection.cursor()
    sentence = 'INSERT INTO users (first_name, sec_name, last_name, birthdate) VALUES (%s, %s, %s, %s)'  # noqa: E501
    values = ('Pedro', '', 'Vázquez', '1972-04-16')
    cur.execute(sentence, values)

    sentence = 'UPDATE users SET first_name = %s, last_name =%s WHERE id_user = %s'  # noqa: E501
    values = ('Ma', 'González', 5)
    cur.execute(sentence, values)

    connection.commit()
    print('Termina la transacción')
except Exception as e:
    connection.rollback()
    print(f"Ocurrió un error: {e}")
finally:
    connection.close()

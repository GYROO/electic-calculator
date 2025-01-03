import psycopg2

database_creator = 'CREATE DATABASE electric_load'

table_creator = 'CREATE TABLE main_load ()'


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
    conn.autocommit = True
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')

cursor = conn.cursor()

#cursor.execute(database_creator)
cursor.execute(table_creator)
cursor.close() # закрываем курсор
conn.close()

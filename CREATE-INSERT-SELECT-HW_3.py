import psycopg2
conn = psycopg2.connect(database = 'netology_db', user = 'postgres', password = 'Zxc25532335dd.')


#Задание №1
def del_create_dbs(cursor: str):
    cursor.execute('''
    DROP TABLE client CASCADE;
    DROP TABLE number;
    ''')
    cursor.execute('''
    CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE);
    ''')
    cursor.execute('''
    CREATE TABLE number (
    id SERIAL PRIMARY KEY,
    title VARCHAR(12) NOT NULL UNIQUE,
    client_id INTEGER NOT NULL REFERENCES client(id));
    ''')
    conn.commit()
    return print('DB created(client, number)')


#Задание №2
def uppend_client(cursor, id: int, name: str, surname: str, email: str, number: str, n_id: int):
    cursor.execute('''
    INSERT INTO client(id, name, surname, email) VALUES(%s, %s, %s, %s);
    ''', (id, name, surname, email))
    cursor.execute('''
    INSERT INTO number(id, title, client_id) VALUES(%s, %s, %s);
    ''', (n_id, number, id))
    cursor.execute("""
    SELECT * FROM client;
    """)
    return print(cursor.fetchall())

#Задание №3
def upend_number(cursor, id: int, n_id: int, number: str):
    cursor.execute('''
    INSERT INTO number(id, title, client_id) VALUES(%s, %s, %s);
    ''', (n_id, number, id))
    cursor.execute("""
    SELECT * FROM number;
    """)
    return print(cursor.fetchall())

#Задание №4
def client_data_updater(command: str, cursor: str):
    id = int(input('Input id: '))
    if command == 'n':
        up_name = str(input('Input name: '))
        cursor.execute('''
        UPDATE client SET name=%s WHERE id=%s;
        ''', (up_name, id))
        cursor.execute('''
        SELECT * FROM client;
        ''')
        return print(cursor.fetchall())

    elif command == 's':
        up_surname = str(input('Input surname: '))
        cursor.execute('''
        UPDATE client SET surname=%s WHERE id=%s;
        ''', (up_surname, id))
        cursor.execute('''
        SELECT * FROM client;
        ''')
        return print(cursor.fetchall())

    elif command == 'e':
        up_email = str(input('Input email: '))
        cursor.execute('''
        UPDATE client SET email=%s WHERE id=%s;
        ''', (up_email, id))
        cursor.execute('''
        SELECT * FROM client;
        ''')
        return print(cursor.fetchall())
    elif command == 'num':
        up_number = str(input('Input number: '))
        cursor.execute('''
        UPDATE number SET title=%s WHERE id=%s;
        ''', (up_number, id))
        cursor.execute('''
        SELECT * FROM number;
        ''')
        return print(cursor.fetchall())
    else:
        return print('Error')

#Задание №5
def del_number(cursor: str, id: int):
    cursor.execute('''
    DELETE FROM number WHERE id=%s;
    ''', (id,))
    cursor.execute('''
    SELECT * FROM number;
    ''')
    return print(cursor.fetchall())

#Задание №6
def del_client(cursor: str, id: int):
    cursor.execute('''
    DELETE FROM number WHERE client_id=%s;
    ''', (id,))
    cursor.execute('''
    DELETE FROM client WHERE id=%s;
    ''', (id,))
    cursor.execute('''
    SELECT * FROM client;
    ''')
    return print(cursor.fetchall())

#Задание №7
def client_finder(cursor: str, name: str, surname: str, email: str, number: str):
    cursor.execute('''
    SELECT client_id FROM number WHERE title=%s;
    ''', (number,))
    cursor.execute('''
    SELECT * FROM client WHERE name=%s OR surname=%s OR email=%s OR id= %s;
    ''', (name, surname, email, cursor.fetchone()))
    return print(cursor.fetchone())




with conn.cursor() as cur:
    del_create_dbs(cur)

    uppend_client(cur, 1, 'Tim', 'Big', 'netologgy_tb@gmail.com', '+79985675623', 1)
    uppend_client(cur, 2, 'Sam', 'Small', 'netologgy_ss@gmail.com', '+79985675663', 2)

    upend_number(cur, 2, 3, '+79985565623')

    client_data_updater('n', cur)

    del_number(cur, 1)

    del_client(cur, 1)

    client_finder(cur, 'Ken', 'All', 'netolhggy_ss@gmail.com', '+79985675623')

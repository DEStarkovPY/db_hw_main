import psycopg2

conn = psycopg2.connect(database = 'netology_db', user = 'postgres', password = 'Zxc25532335dd.') #Объект подключения
#cun = conn.cursor() # Первый способ ведения базы данных
#cun.execute('')
#cun.close()

with conn.cursor() as cur: #C помощью контекстного менеджера
    cur.execute('''
    DROP TABLE test;
    ''') # Удаление всех таблиц в начале для удобства
    cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
    #conn.rollback() #ВСЕ описанные выше курсоры будут проигнорированы

    cur.execute('''
    INSERT INTO test(id)
    VALUES(1);
    ''') #Заполнение отношения без фиксирования

    conn.commit() #Сохранение изменений

    cur.execute('''
    INSERT INTO test(id)
    VALUES(2) RETURNING id;
    ''')
    #print(cur.fetchone()) #Заполнение отношения, фиксация и запрос, команда feth one

    cur.execute('''
    SELECT * FROM test;
    ''')
    #print(cur.fetchall()) #Извлечь все строки из отношения(значения выходят из состава таблицы)
    #print(cur.fetchone()) #Извлечь первую строку из отношения
    #print(cur.fetchmany(2)) #Извлечь первые 2 строки
conn.close() #По завершении работы



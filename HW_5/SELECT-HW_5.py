import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker #Функция, создающая сессии - способ подключения к бд(как cursor)
from Models_HW_5 import * # Импортировать всё

driver = 'postgresql'
login = 'postgres'
password = 'Zxc25532335dd'
server_name = 'localhost'
port = '5432'
DSN = f'{driver}://{login}:{password}.@{server_name}:{port}' #драйвер_подключения:/логин:пароль@Название_сервера:порт(5432)
engine = sq.create_engine(DSN) #Создание движка engine - объект подключения к бд

Session = sessionmaker(bind=engine) #Класс, создающий сессии
ses = Session() #Создание сессии

if __name__ == '__main__':

    create_tables(engine)
    p_id = int(input('Enter first publisher id: '))
    publisher_1 = Publisher(id=p_id, name='Sam') #INSERT INTO Publisher
    ses.add(publisher_1)
    ses.commit()

    print(publisher_1)

    ses.close() #Закрытие сессии


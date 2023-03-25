import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship # Базовый класс,
#регистрирующий всех наследников, функция для создания связей

Base = declarative_base() #Создание базового класса

class Publisher(Base): #Создание наследника Base
    __tablename__ = 'publisher' #Присваивание имя таблице

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False)

    #books = relationship("Book", back_populates="publisher")

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60), nullable=False, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)
    # Создание внешнего ключа, отсылающегося на таблицу Publisher

    #publisher = relationship(Publisher, back_populates='books')
    publisher = relationship(Publisher, backref='books') #Связь таблиц без изменениий в обоих


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False, unique=True)

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    data_sale = sq.Column(sq.Integer, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sales')


def create_tables(engine):
    Base.metadata.drop_all(engine) #У класса Base вызывается свойство metadata, а у него вызыв. метод
    Base.metadata.create_all(engine)#Создаёт все таблицы, кроме существующих







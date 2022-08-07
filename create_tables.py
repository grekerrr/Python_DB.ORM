from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from connecting_db import connecting_DB

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    id_publisher = Column(Integer, ForeignKey(Publisher.id))


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_book = Column(Integer, ForeignKey(Book.id))
    id_shop = Column(Integer, ForeignKey(Shop.id))
    count = Column(Integer)


class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    # возможно, дату лучше так: date_sale = Column(DateTime, nullable=False)
    date_sale = Column(DateTime.date('%d/%m/%Y'), nullable=False)
    id_stock = Column(Integer, ForeignKey(Stock.id))
    count = Column(Integer)


def create_tables():
    connecting = connecting_DB.engine
    # Base.metadata.drop_all(connecting) #очистка
    Base.metadata.create_all(connecting)

import json

from connecting_db import connecting_DB
from create_tables import Publisher, Book, Shop, Stock, Sale


session = connecting_DB.session


def insert_tables():
    with open("fixtures/tests_data.json", "r") as f:
        data = json.load(f)

    publishers = ({'id':i['pk'], 'fields':i['fields']} for i in data if i['model'] == 'publisher')
    books = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'book')
    shops = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'shop')
    stocks = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'stock')
    sales = ({'id': i['pk'], 'fields': i['fields']} for i in data if i['model'] == 'sale')

    for publisher in publishers:
        adding = Publisher(id = publisher['id'], name = publisher['fields']['name'])
        session.add(adding)
        session.commit()

    for book in books:
        adding = Book(id = book['id'],
                      title = book['fields']['title'],
                      id_publisher = book['fields']['publisher']
                      )
        session.add(adding)
        session.commit()

    for shop in shops:
        adding = Shop(id = shop['id'], name = shop['fields']['name'])
        session.add(adding)
        session.commit()

    for stock in stocks:
        adding = Stock(id = stock['id'],
                       id_book = stock['fields']['book'],
                       id_shop = stock['fields']['shop'],
                       count = stock['fields']['count']
                       )
        session.add(adding)
        session.commit()

    for sale in sales:
        adding = Sale(id = sale['id'],
                      price = sale['fields']['price'],
                      date_sale = sale['fields']['date_sale'],
                      id_stock = sale['fields']['stock'],
                      count = sale['fields']['count']
                      )
        session.add(adding)
        session.commit()

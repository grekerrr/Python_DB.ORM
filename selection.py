from connecting_db import connecting_DB
from create_tables import Publisher, Book, Shop, Stock, Sale, create_tables
from insert_file import insert_tables


session = connecting_DB.session


def user_input(user_input):
    publishers_id = list(map(lambda x: str(x[0]), session.query(Publisher.id).all()))
    publishers_name = list(map(lambda x: x[0], session.query(Publisher.name).all()))
    if user_input in publishers_id:
        return Publisher.id
    elif user_input.title() in publishers_name:
        return Publisher.name
    else:
        return False


def books_by_publisher(publisher):
    query_param = user_input(publisher)
    if not query_param:
        print("По Вашему запросу издатель не найден!")
        return
    else:
        query = session.query(Book.title, Shop.name, Sale.price, Sale.count).join(Publisher, Stock, Shop, Sale).filter(
            query_param == publisher.title()).order_by(Book.title).all()
        print(session.query(Publisher.name).filter(query_param == publisher.title()).first()[0])
        for book, shop, price, count in query:
            print(f'Книга {book} продаётся в магазине {shop}, в наличии {count} штук по цене {price}')
        return query


if __name__ == 'main':
    create_tables()
    insert_tables()

    while True:
        text = input("Введите id или имя издателя (publisher) или break для отмены: ").strip()
        if text == 'break':
            break
        else:
            books_by_publisher(text)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class connecting_DB:
    login_db = input("Введите логин для подключения к БД: ")
    pass_db = input("Введите пароль для подключения к БД: ")
    name_db = input("Введите название БД: ")
    DSN = f'postgresql://{login_db}:{pass_db}@localhost:5432/{name_db}'
    engine = create_engine(DSN)
    Session = sessionmaker(bind=engine)
    print(f'Вы успешно подключились к БД "{name_db}"')

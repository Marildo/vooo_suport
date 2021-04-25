import logging

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from settings.settings import Settings


class DBConnection:

    def __init__(self):
        self.__session: sessionmaker = None

    def connect(self, settings: Settings):
        url = self.__get_url(settings)
        engine = create_engine(url, pool_timeout=settings.get_database_timeout(), echo=settings.get_debug())
        self.__session = sessionmaker(bind=engine)
        logging.info(f'Conectado ao banco de dados...')

    @property
    def session(self) -> sessionmaker:
        return self.__session

    def __get_url(self, settings) -> str:
        user = settings.get_database_user()
        password = settings.get_database_password()
        port = settings.get_database_port()
        host = settings.get_database_host()
        database = settings.get_database_name()
        charset = settings.get_database_charset()
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session


from settings.settings import Settings
from decorators.singleton import singleton


#TODO - Melhor opção seria ultilizar flask_sqlalchemy, mas por enquanto vamos aprender sqlAlchemy

@singleton
class DBConnection:

    def __init__(self, settings: Settings):
        self.__session: Session = None
        self.connect(settings)

    def connect(self, settings: Settings):
        url = self.__get_url(settings)
        engine = create_engine(url, pool_timeout=settings.get_database_timeout(), echo=settings.get_debug())
        self.__session = sessionmaker(bind=engine)()
        logging.info(f'Conectado ao banco de dados...')

    @property
    def session(self) -> Session:
        return self.__session

    @staticmethod
    def __get_url(settings) -> str:
        user = settings.get_database_user()
        password = settings.get_database_password()
        port = settings.get_database_port()
        host = settings.get_database_host()
        database = settings.get_database_name()
        charset = settings.get_database_charset()
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'

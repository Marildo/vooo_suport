from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def __load_value(name, default=None):
        return os.environ[name] if name in os.environ else default

    def get_port(self):
        return self.__load_value('PORT', 3100)

    def get_debug(self):
        return self.__load_value('DEBUG', False)

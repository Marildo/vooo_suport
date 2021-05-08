from abc import ABC, abstractmethod
from model.tables import Client, Document, ClientConnector


class ClientFilterFactory:
    def __init__(self, params: dict):
        self.__type_search = int(params['type'] if 'type' in params else 0)
        self.__search = params['search'] if 'search' in params else None
        self.__active = self.__search is not None

    class ClientFilter(ABC):
        @staticmethod
        @abstractmethod
        def get_filter(search: str):
            pass

    class FilterNome(ClientFilter):
        @staticmethod
        def get_filter(search: str):
            return True

    class FilterById(ClientFilter):
        @staticmethod
        def get_filter(search: str):
            return Client.id == search

    class FilterByName(ClientFilter):
        @staticmethod
        def get_filter(search: str):
            return Client.name.ilike(f'%{ search }%')

    class FilterByDocument(ClientFilter):
        @staticmethod
        def get_filter(search: str):
            return Document.number == search

    class FilterByEC(ClientFilter):
        @staticmethod
        def get_filter(search: str):
            return ClientConnector.contract_code == search

    __map_class = {
        0: FilterNome,
        1: FilterById,
        2: FilterByName,
        3: FilterByDocument,
        4: FilterByEC,
    }

    def get_filter(self):
        filter_class = self.__map_class[self.__type_search]
        return filter_class().get_filter(self.__search)

    @property
    def active(self):
        return self.__active

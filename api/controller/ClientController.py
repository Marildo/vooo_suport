from model.DBConnection import DBConnection
from model.schemas import ClientSchema
from model.tables import Client
from settings.Settings import Settings


class ClientController:

    def __init__(self):
        self.__connection = DBConnection(Settings())

    def read_all(self, limit: int = 500, offset: int = 0):
        total = self.__connection.session.query(Client).count()
        clients = self.__connection.session.query(Client).limit(limit).offset(offset).all()
        cs = ClientSchema(many=True)
        data = cs.dump(clients)
        return {'total': total, 'data': data}

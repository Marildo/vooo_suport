from model.connection import DBConnection
from model.schemas import ClientSchema
from model.tables import Client


class ClientController:

    def __init__(self, connection: DBConnection):
        self.__connection = connection

    def read_all(self, limit: int = 500) -> list:
        clients = self.__connection.session.query(Client).limit(limit).all()
        cs = ClientSchema(many=True)
        return cs.jsonify(clients)

from werkzeug.datastructures import ImmutableMultiDict

from model.db_connection import DBConnection
from model.schemas import ConnectorSchema
from model.tables import Connector
from settings.settings import Settings



class ConnectorController:
    def __init__(self):
        self.__connection = DBConnection(Settings())

    def read_all(self, params: ImmutableMultiDict):
        connectors = self.__connection.session.query(Connector).all()
        schema = ConnectorSchema(many=True)
        return schema.jsonify(connectors)

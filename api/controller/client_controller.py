from werkzeug.datastructures import ImmutableMultiDict

from model.db_connection import DBConnection
from model.schemas import ClientSchema
from model.tables import Client, Document, ClientConnector
from settings.settings import Settings
from controller.client_filter import ClientFilterFactory


class ClientController:

    def __init__(self):
        self.__connection = DBConnection(Settings())

    def read_all(self, params: ImmutableMultiDict):
        page = int(params['page'] if 'page' in params else 1)
        limit = int(params['limit'] if 'limit' in params else 10)
        offset = page * limit

        client_filter = ClientFilterFactory(params)
        _filter = client_filter.get_filter()
        if client_filter.active:
            limit = None
            offset = None

        def builder_query(_filter):
            return self.__connection.session \
                .query(Client).filter(_filter) \
                .join(Document, Document.id == Client.id_document) \
                .outerjoin(ClientConnector, ClientConnector.client_id == Client.id) \
                .group_by(Client.id)

        query = builder_query(_filter).limit(limit).offset(offset)
        clients = query.all()
        cs = ClientSchema(many=True)
        data = cs.dump(clients)

        if client_filter.active:
            total = len(data)
        else:
            total = builder_query(_filter).count()

        return {'total': total, 'data': data}

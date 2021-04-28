from model.marshmallowConfig import marsh
from model.tables import Client


class ClientSchema(marsh.Schema):
    class Meta:
        model = Client
        fields = ('id', 'name', 'trand')

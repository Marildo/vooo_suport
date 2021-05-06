from model.marshmallow_config import marsh
from marshmallow import fields


class DocumentSchema(marsh.Schema):
    type = fields.Str()
    number = fields.Str()


class ClientSchema(marsh.Schema):
    id = fields.Integer(required=True)
    name = fields.Str()
    document = fields.Nested('DocumentSchema')





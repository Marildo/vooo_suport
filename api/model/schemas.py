from model.marshmallow_config import marsh
from marshmallow import fields


class BaseSchema(marsh.Schema):
    id = fields.Integer(required=True)


class ClientSchema(BaseSchema):
    name = fields.Str()
    document = fields.Nested('DocumentSchema')
    aggregator = fields.Nested('AggregatorSchema')


class DocumentSchema(marsh.Schema):
    type = fields.Str()
    number = fields.Str()


class AggregatorSchema(BaseSchema):
    name = fields.Str()






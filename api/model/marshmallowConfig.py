from flask_marshmallow import Marshmallow

marsh = Marshmallow()


def init_marshmallow(app):
    marsh.init_app(app)

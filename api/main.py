from datetime import datetime

from flask import Flask, jsonify, make_response

from controller.ClientController import ClientController
from model.connection import DBConnection
from model.marshmallowConfig import init_marshmallow
from settings.settings import Settings

app = Flask('Api-vooo-suport')


@app.route('/')
def index():
    return jsonify(msg='Server is running', data=datetime.now())


@app.route('/client/')
def client():
    client_controller = ClientController(connection)
    return make_response(client_controller.read_all(), 200)


if __name__ == '__main__':
    settings = Settings()
    init_marshmallow(app)
    connection = DBConnection()
    connection.connect(settings)
    app.run(debug=settings.get_debug(), port=settings.get_api_port())

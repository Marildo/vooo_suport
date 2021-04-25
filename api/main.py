from datetime import datetime

from flask import Flask, jsonify

from settings.settings import Settings
from model.Connection import DBConnection

app = Flask('Api-vooo-suport')


@app.route('/')
def index():
    return jsonify(msg='Server is running', data=datetime.now())


if __name__ == '__main__':
    settings = Settings()
    connection = DBConnection()
    connection.connect(settings)
    app.run(debug=settings.get_debug(), port=settings.get_api_port())

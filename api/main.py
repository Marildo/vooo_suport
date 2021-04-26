from datetime import datetime
from flask import Flask, jsonify, make_response
from model.marshmallowConfig import init_marshmallow
from settings.settings import Settings
from routers.clientRouter import client_router


app = Flask('Api-vooo-suport')
app.register_blueprint(client_router)


@app.route('/')
def index():
    return jsonify(msg='Server is running', data=datetime.now())


if __name__ == '__main__':
    init_marshmallow(app)

    settings = Settings()
    app.run(debug=settings.get_debug(), port=settings.get_api_port())
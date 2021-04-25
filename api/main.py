from datetime import datetime

from flask import Flask, jsonify

from settings.settings import Settings

app = Flask('Api-vooo-suport')


@app.route('/')
def index():
    return jsonify(msg='Server is running', data=datetime.now())


if __name__ == '__main__':
    settings = Settings()
    app.run(debug=settings.get_debug(),
            port=settings.get_port())

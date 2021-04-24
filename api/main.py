from flask import  Flask, jsonify
from datetime import datetime

app = Flask('Api-vooo-suport')

@app.route('/')
def index():
    return jsonify(msg='Server is running', data=datetime.now())

if __name__ == '__main__':
    app.run(debug=True, port=4000)


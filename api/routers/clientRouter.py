from flask import Blueprint, make_response, abort

from controller.ClientController import ClientController

client_router = Blueprint('client_router', __name__)


@client_router.route('/client/')
def client():
    try:
        client_controller = ClientController()
        return make_response(client_controller.read_all(), 200)
    except:
        abort(500)

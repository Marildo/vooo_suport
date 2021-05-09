from flask import Blueprint, make_response, request, abort

from controller.client_controller import ClientController

client_router = Blueprint('client_router', __name__)


@client_router.route('/client/', methods=['GET'])
def client():
    try:
        client_controller = ClientController()
        response = client_controller.read_all(request.args)
        return make_response(response, 200)
    except Exception as error:
        print(error)
        abort(500)

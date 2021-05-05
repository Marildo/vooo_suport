from flask import Blueprint, make_response, request, abort

from controller.ClientController import ClientController

client_router = Blueprint('client_router', __name__)


@client_router.route('/client/', methods=['GET'])
def client():
    try:
        offset = request.args['offset']
        limit = request.args['limit']
        client_controller = ClientController()
        return make_response(client_controller.read_all(limit,offset), 200)
    except:
        abort(500)

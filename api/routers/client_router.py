from flask import Blueprint, make_response, request, abort

from controller.client_controller import ClientController

client_router = Blueprint('client_router', __name__)


@client_router.route('/client/', methods=['GET'])
def client():
    try:
        page = int(request.args['page'] if 'page' in request.args else 1)
        limit = int(request.args['limit'] if 'limit' in request.args else 10)
        offset = page * limit
        client_controller = ClientController()
        response = client_controller.read_all(limit, offset)
        return make_response(response, 200)
    except Exception as error:
        print(error)
        abort(500)

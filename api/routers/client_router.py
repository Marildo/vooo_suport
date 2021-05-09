from flask import Blueprint, make_response, request, abort

from controller.client_controller import ClientController

client_router = Blueprint(name=__name__, import_name=__name__, url_prefix='/client')


# TODO criar um decorator para tratar execoes nos endpoints

@client_router.route('/', methods=['GET'])
def clients():
    try:
        client_controller = ClientController()
        response = client_controller.read_all(request.args)
        return make_response(response, 200)
    except Exception as error:
        print(error)
        abort(500)

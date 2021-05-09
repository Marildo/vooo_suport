from flask import Blueprint, make_response, request, abort

from controller.connector_controller import ConnectorController

connector_router = Blueprint(name=__name__, import_name=__name__, url_prefix='/connector')


@connector_router.route('/', methods=['GET'])
def connectores():
    try:
        client_controller = ConnectorController()
        response = client_controller.read_all(request.args)
        return make_response(response, 200)
    except Exception as error:
        print(error)
        abort(500)

from http import HTTPStatus
import json
from flask import Blueprint, Response


example_api = Blueprint('root', __name__, url_prefix='/example')

@example_api.route('/', methods=['GET'])
def handle_home():
    data = {
        "hallo": "world"
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.OK, mimetype='application/json')
    return response


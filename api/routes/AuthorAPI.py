from http import HTTPStatus
import json
from flask import Blueprint, Response, abort, request

from api.services import AuthorService

author_api = Blueprint('author_api', __name__, url_prefix='/author')

@author_api.route('/<id>', methods=['GET'])
def handle_get_author(id: int):
    author_data = AuthorService.get_author(id)

    if 'empty' in author_data:
        abort(404, {"message": "author not found"})
    
    data = {
        "status": HTTPStatus.OK,
        "message": "Success",
        "data": author_data
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.OK, mimetype='application/json')
    return response

@author_api.route('/add', methods=['POST'])
def handle_create_author():
    request_body = request.get_json()
    has_username = True if 'username' in request_body else False
    has_fullname = True if 'fullname' in request_body else False
    has_email = True if 'email' in request_body else False

    fulfilled_condition = has_username and has_fullname and has_email

    if fulfilled_condition != True:
        abort(400, {'message': 'insufficient body information to create new author'})
    
    try:
        AuthorService.create_new(request_body)
    except Exception as e:
        abort(500, {'message': 'error creating new author'})

    data = {
        "status": HTTPStatus.CREATED,
        "message": "Success Created New Author ",
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.CREATED, mimetype='application/json')
    return response


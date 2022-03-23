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
    
@author_api.route('/all', methods=['GET'])
def handle_get_all_author():
    author_data = AuthorService.get_all_author()

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


@author_api.route('/<id>/update', methods=['PUT'])
def handle_update_author(id):
    request_body = request.get_json()
    has_username = True if 'username' in request_body else False
    has_fullname = True if 'fullname' in request_body else False
    has_email = True if 'email' in request_body else False

    fulfilled_condition = has_username and has_fullname and has_email

    if fulfilled_condition != True:
        abort(HTTPStatus.BAD_REQUEST, {'message': 'insufficient body information to create new author'})
    
    try:
        author_data = AuthorService.update(id, request_body)
    except Exception as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, {'message': str(e)})
    
    if author_data is not None and 'empty' in author_data:
        abort(HTTPStatus.NOT_FOUND, {"message": "author not found"})

    data = {
        "status": HTTPStatus.OK,
        "message": "Success Updated New Author ",
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.CREATED, mimetype='application/json')
    return response

@author_api.route('/<id>/delete', methods=['DELETE'])
def handle_delete_author(id):   
    try:
        author_data = AuthorService.delete(id)
    except Exception as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, {'message': 'error creating new author'})

    if author_data is not None and 'empty' in author_data:
        abort(HTTPStatus.NOT_FOUND, {"message": "author not found"})
    
    data = {
        "status": HTTPStatus.OK,
        "message": "Succeed Delete Author",
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.OK, mimetype='application/json')
    return response

@author_api.route('/<id>/upload', methods=['POST'])
def handle_upload_file(id):
    try:
        author_data = AuthorService.upload(id, request.files)
    except Exception as e:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, {'message': str(e) + ' error uploading file'})

    if author_data is not None and 'empty' in author_data:
        abort(HTTPStatus.NOT_FOUND, {"message": "author not found"})

    data = {
        "status": HTTPStatus.OK,
        "message": "File uploaded",
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.OK, mimetype='application/json')
    return response


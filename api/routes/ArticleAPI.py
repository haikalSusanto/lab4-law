from http import HTTPStatus
import json
from flask import Blueprint, Response, abort
from ..services import ArticleService


article_api = Blueprint('article_api', __name__, url_prefix="/article")

@article_api.route('/<id>', methods=['GET'])
def handle_get_article(id: int):
    author_data = ArticleService.get_article(id)

    if 'empty' in author_data:
        abort(404, {"message": "author not found"})
    
    data = {
        "status": HTTPStatus.OK,
        "message": "Success",
        "data": author_data
    }
    response = Response(response=json.dumps(data), status=HTTPStatus.OK, mimetype='application/json')
    return response

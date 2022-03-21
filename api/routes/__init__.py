from flask import Blueprint

from .AuthorAPI import author_api

root_api = Blueprint('root', __name__, url_prefix='/api/v1')

root_api.register_blueprint(author_api)

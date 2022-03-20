from flask import Blueprint

from .example import example_api

root_api = Blueprint('root', __name__, url_prefix='/api/v1/')

root_api.register_blueprint(example_api)

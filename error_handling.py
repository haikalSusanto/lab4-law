import json

from flask import Response
from werkzeug.exceptions import HTTPException


def error_handling(app):
    app = app

    @app.errorhandler(HTTPException)
    def handle_error(e):
        data = {
            "status": e.code,
            "error": e.name,
        } 
        
        if type(e.description) == dict:
            data['message'] = e.description['message']
        else:
            data['message'] = e.description

        response = Response(response=json.dumps(data), status=e.code, mimetype='application/json')
        return response

 
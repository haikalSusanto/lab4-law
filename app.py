from flask import Flask
from error_handling import error_handling

from api.models import db, migrate
from api.routes import root_api

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(root_api)  

    
    error_handling(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

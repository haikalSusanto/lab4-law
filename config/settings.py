class BaseConfig():
   TESTING = False
   DEBUG = False
   SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class DevConfig(BaseConfig):
   ENV = 'development'
   SECRET_KEY = 'super-secret'
   DEBUG = True
   SERVER_NAME = 'localhost:8000'


class ProductionConfig(BaseConfig):
   ENV = 'production'
   SECRET_KEY = 'super-secret'
   SERVER_NAME = 'localhost:10805'


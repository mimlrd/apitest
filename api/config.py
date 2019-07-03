## config.py

'''
  "Configuration for the app"
  SQLALCHEMY_DATABASE_URI could be different for Development or Production
  2 Different Classes :
  - Development
  - Production
'''

import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #SECRET_KEY = secrets.token_hex(16)
    SECRET_KEY = b'\x83Y\x86\xc4\xc3N\x8c\xc69\xfe\xc6\xce\xc45\x90\xb1'
    if not SECRET_KEY:
        raise ValueError("No secret key set for Flask application")
    ##SECRET_KEY = os.environ.get('SECRET_KEY') or b'_5#y2L"F4Q8z\n\xec]/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    ##SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://firstrep:158%KEuM2RmZs@localhost:5433/eduka_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig
}

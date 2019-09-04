import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object) :
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqllite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(object) :
    DEBUG=True
    SQLALCHEMY_ECHO = True

class ProductionConfig(object) :
    DEBUG = False

app_config={
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}

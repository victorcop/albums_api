import os

from configuration_secrets import SecretConstants


def get_dict_config():
    return {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }


constants = SecretConstants()

user = constants.DB_USER
password = constants.DB_PASS
host = constants.DB_HOST
name = constants.DB_NAME


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DEBUG = True

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = constants.REDIS_HOST
    CACHE_REDIS_PORT = constants.REDIS_PORT
    CACHE_REDIS_DB = constants.REDIS_DB


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{name}'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{name}'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}/{name}'

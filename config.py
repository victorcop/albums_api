import os

from app_secrets import SecretConstants


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


user = SecretConstants.DB_USER
password = SecretConstants.DB_PASS
host = SecretConstants.DB_HOST
port = SecretConstants.DB_PORT
name = SecretConstants.DB_NAME


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg',
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    DEBUG = True

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = SecretConstants.REDIS_HOST
    CACHE_REDIS_PORT = SecretConstants.REDIS_PORT
    CACHE_REDIS_DB = SecretConstants.REDIS_DB


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{name}'

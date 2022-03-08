from logging.config import dictConfig

from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from app.errors import not_found, not_allowed, internal_server
from http import HTTPStatus

from config import get_dict_config

db = SQLAlchemy()
dictConfig(get_dict_config())
cache = Cache()


def init_extensions(app):
    db.init_app(app)
    cache.init_app(app)


def init_errors_handlers(app):
    app.register_error_handler(HTTPStatus.NOT_FOUND, not_found)
    app.register_error_handler(HTTPStatus.METHOD_NOT_ALLOWED, not_allowed)
    app.register_error_handler(HTTPStatus.INTERNAL_SERVER_ERROR, internal_server)

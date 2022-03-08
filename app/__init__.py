from flask import Flask
from flask_migrate import Migrate

from app.extensions import *


def create_app(config_env=''):
    app = Flask(__name__)
    migrate = Migrate(app, db, render_as_batch=True)
    if not config_env:
        config_env = app.env.capitalize()
    app.config.from_object(f"config.{config_env}Config")

    # Initializing extensions
    init_extensions(app)

    from app.albums.http.api import album
    app.register_blueprint(album, url_prefix='/album')

    # Initializing error handlers
    init_errors_handlers(app)

    return app

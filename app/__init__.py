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
    from app.auth.http.api import auth
    app.register_blueprint(album, url_prefix='/api/album')
    app.register_blueprint(auth, url_prefix='/api')

    # Initializing error handlers
    init_errors_handlers(app)

    return app

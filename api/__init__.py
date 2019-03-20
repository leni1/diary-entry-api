from flask import Flask

from . import settings


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings)

    from api.views.entries import diary
    app.register_blueprint(diary, url_prefix='/api/v1')

    return app

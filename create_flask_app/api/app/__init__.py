from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
# blueprints
from app.some_blueprint.routes import api
from app.errors.handlers import errors


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(api)
app.register_blueprint(errors)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if os.environ.get(
        "PRODUCTION").lower() == 'true' else DevelopmentConfig)

    from app.some_blueprint.routes import api
    from app.errors.handlers import errors

    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app

from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
from flask_cors import CORS
# blueprints
from app.errors.handlers import errors
from app.home.routes import home


app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(errors)
app.register_blueprint(home)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if os.environ.get(
        "PRODUCTION").lower() == 'true' else DevelopmentConfig)

    from app.errors.handlers import errors
    from app.home.routes import home

    app.register_blueprint(errors)
    app.register_blueprint(home)

    return app

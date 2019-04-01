from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from app.database import db

from config import Config

migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()


def register_blueprints(app):
    from app.apiv1 import bp as apiv1_bp
    app.register_blueprint(apiv1_bp, url_prefix='/apiv1')


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    register_blueprints(app)

    return app

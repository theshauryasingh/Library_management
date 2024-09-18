import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

load_dotenv()

db = SQLAlchemy()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URL set for SQLAlchemy database.")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    JWTManager(app)

    # Register Blueprints (for routes)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app


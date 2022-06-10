from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blood.sqlite"

    db = SQLAlchemy(app)
    app.config['SECRET_KEY'] = 'ajflseiuroe324803482572oflskdkfjuw45o80wrq80572soufose57o85u3048'

    CORS(app)
    return app, db


app, db = create_app()

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

from app.controllers import establishment_controller, user_controller, category_controller, home_controller


db = SQLAlchemy(app)

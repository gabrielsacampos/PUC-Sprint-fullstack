from flask import Flask, request
from app.database import db
from app.model.category import Category
from app.model.establishment import Establishment
from app.model.user import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
db.init_app(app)

from app.controllers import establishment_controller, user_controller, category_controller, home_controller




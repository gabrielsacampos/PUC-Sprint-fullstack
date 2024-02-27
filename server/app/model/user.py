from .base import Base
from app.database import db
from datetime import datetime
from typing import Union



class User(db.Model):
    __tablename__ = 'user'

    #Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, password, created_at:Union[db.DateTime, None] = None):
        self.username = username
        self.password = password
        if created_at:
            self.created_at = created_at

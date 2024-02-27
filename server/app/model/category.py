from typing import Union
from app.database import db
from datetime import datetime

class Category(db.Model):
    __tablename__='category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name: str, created_at: Union[db.DateTime, None] = None): 
        if created_at:
            self.created_at = created_at

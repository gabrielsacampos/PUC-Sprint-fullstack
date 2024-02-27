from app.database import db
from .base import Base
from typing import Union
from datetime import datetime

class Establishment(db.Model):
    __tablename__ = 'establishment'

    #Columns
    id = db.Column(db.Integer, primary_key=True)
    sponsor = db.Column(db.String(100))
    establishment_address = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    # Foreing keys
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__ (self, sponsor, establishment_address, category, user, created_at:Union[db.DateTime, None] = None):
        self.sponsor = sponsor
        self.establishment_address = establishment_address
        self.category = category
        self.user = user
        if created_at:
            self.created_at = created_at
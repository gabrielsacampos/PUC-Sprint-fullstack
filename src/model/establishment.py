from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from base import Base
from typing import Union
import datetime as datetime

class Establishment(Base):
    __tablename__ = 'establishment'

    #Columns
    id = Column(Integer, primary_key=True)
    sponsor = Column(String(100))
    establishment_address = Column(String(100))
    created_at = Column(DateTime, default=datetime.datetime.now())
    
    # Foreing keys
    category = Column(Integer, ForeignKey('category.id'))
    user = Column(Integer, ForeignKey('user.id'))

    def __init__ (self, sponsor, establishment_address, category, user, created_at:Union[DateTime, None] = None):
        self.sponsor = sponsor
        self.establishment_address = establishment_address
        self.category = category
        self.user = user
        if created_at:
            self.created_at = created_at
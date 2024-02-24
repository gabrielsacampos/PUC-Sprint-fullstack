from base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from typing import Union
import datetime as datetime


class User(Base):
    __tablename__ = 'user'

    #Columns
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, username, password, created_at:Union[DateTime, None] = None):
        self.username = username
        self.password = password
        if created_at:
            self.created_at = created_at

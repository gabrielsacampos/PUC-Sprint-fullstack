from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from typing import Union
from .base import Base

class Category(Base):
    __tablename__='category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __init__(self, name: str, created_at:Union[DateTime, None] = None):
        self.name = name
        if created_at:
            self.created_at = created_at

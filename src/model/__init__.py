from sqlalchemy import create_database, database_exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os 
from model import Base, Category, Establishment, User



engine = create_engine(os.environ.get('DATABASE_URL'), echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

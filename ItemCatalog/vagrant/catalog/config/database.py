import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///item_catalog', echo=True)
Base = declarative_base()
Session = None

def create_schema():
    Base.metadata.create_all(engine)

def connect():
    Session = sessionmaker(bind=engine)

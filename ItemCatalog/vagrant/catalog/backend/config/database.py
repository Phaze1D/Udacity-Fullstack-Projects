import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///item_catalog', echo=True)
Base = declarative_base()
DBSession = scoped_session(sessionmaker(bind=engine))


def create_schema():
    Base.metadata.create_all(engine)

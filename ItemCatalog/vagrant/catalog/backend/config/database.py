import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql+psycopg2://catalog:@/itemscatalogs")
Base = declarative_base()
DBSession = scoped_session(sessionmaker(bind=engine))


def create_schema():
    """ Creates the database schema.
        Should be called after all models are implemented
    """
    Base.metadata.create_all(engine)

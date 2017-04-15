from backend.config import Base, DBSession
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, validates
import logging

class Catalog(Base):
    __tablename__ = 'catalog'

    id          = Column(Integer, primary_key=True)
    name        = Column(String(250), unique=True, nullable=False)
    created     = Column(DateTime, default=func.now())
    items       = relationship("Item", back_populates="catalog")


    @validates('name')
    def validates_name(self, key, name):
        if len(name) < 3:
            raise Exception("Name must be atleast 3 chars")
        return name


    @classmethod
    def create(cls, name):
        catalog = None
        error = None
        try:
            catalog = cls(name=name)
            DBSession.add(catalog)
            DBSession.commit()
        except Exception as e:
            error = str(e)
        return catalog, error

    @classmethod
    def edit(cls, id, name):
        catalog = None
        error = None
        try:
            catalog = cls.find_by_id(id)
            catalog.name = name
            DBSession.commit()
        except Exception as e:
            DBSession.rollback()
            error = str(e)
        return catalog, error

    @classmethod
    def get_all(cls):
        return DBSession.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).first()

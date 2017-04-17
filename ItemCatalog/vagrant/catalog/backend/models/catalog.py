from backend.config import Base, DBSession
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, validates
import logging

class Catalog(Base):
    __tablename__ = 'catalog'

    id      = Column(Integer, primary_key=True)
    name    = Column(String(250), unique=True, nullable=False)
    created = Column(DateTime, default=func.now())
    items   = relationship("Item", back_populates="catalog")


    def to_json(self, show_items=True):
        """Converts Catalog into json

        Args:
            show_items(boolean): Whether to include all the catalogs items

        Returns:
            dict object of the catalog
        """
        json = {
            'id': self.id,
            'name': self.name,
            'created': self.created
        }

        if show_items:
            json['items'] = [ item.to_json(show_catalog=False) for item in self.items]

        return json


    @validates('name')
    def validates_name(self, key, name):
        """Validates the name field before update and create
        Raises:
            Exception: if name length is less the 3 chars
        """
        if len(name) < 3:
            raise Exception("Name must be atleast 3 chars")
        return name


    @classmethod
    def create(cls, name):
        """Creates and saves a new catalog"""
        catalog = None
        error = None
        try:
            catalog = cls(name=name)
            DBSession.add(catalog)
            DBSession.commit()
        except Exception as e:
            DBSession.rollback()
            error = str(e)
        return catalog, error


    @classmethod
    def edit(cls, id, name):
        """Edits and saves a new catalog"""
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
        """Gets all the catalogs"""
        return DBSession.query(cls).all()


    @classmethod
    def find_by_id(cls, id):
        """Finds catalog by id"""
        return DBSession.query(cls).filter(cls.id == id).first()

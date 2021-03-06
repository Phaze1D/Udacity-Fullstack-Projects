from backend.config import Base, DBSession
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, validates


class Item(Base):
    __tablename__ = 'item'

    id          = Column(Integer, primary_key=True)
    name        = Column(String(250), unique=True, nullable=False)
    description = Column(String(250), nullable=False)
    created     = Column(DateTime, default=func.now())
    catalog_id  = Column(Integer, ForeignKey('catalog.id'))
    user_id     = Column(Integer, ForeignKey('users.id'))
    catalog     = relationship("Catalog", back_populates="items", foreign_keys=[catalog_id])
    user        = relationship("User", back_populates="items", foreign_keys=[user_id])


    def to_json(self, show_user=True, show_catalog=True):
        """Converts Catalog into json

        Args:
            show_user(boolean): Whether to include the user
            show_catalog(boolean): Whether to include the catalog

        Returns:
            dict object of the item
        """
        json = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created': self.created,
        }

        if show_user:
            json['user'] = {
                'id': self.user.id,
                'email': self.user.email,
                'created': self.user.created
            }

        if show_catalog:
            json['catalog'] = {
                'id': self.catalog.id,
                'name': self.catalog.name,
                'created': self.catalog.created
            }

        return json


    @validates('name')
    def validates_name(self, key, name):
        """Validates the name field before update and create

        Raises:
            Exception: if name length is less the 3 chars
        """
        if not name or len(name) < 3:
            raise Exception("Name must be atleast 3 chars")
        return name


    @validates('description')
    def validates_description(self, key, description):
        """Validates the description field before update and create

        Raises:
            Exception: if description length is less the 20 chars
        """
        if not description or len(description) < 20:
            raise Exception("Description must be atleast 20 chars")
        return description


    @validates('catalog')
    def validates_catalog(self, key, catalog):
        """Validates the catalog field before update and create

        Raises:
            Exception: if catalog is not found
        """
        if not catalog:
            raise Exception('catalog not found')
        return catalog


    @validates('user')
    def validates_user(self, key, user):
        """Validates the user field before update and create

        Raises:
            Exception: if user is not found
        """
        if not user:
            raise Exception('user not found')
        return user


    @classmethod
    def create(cls, name, description, catalog, user):
        """Creates and saves a new item"""
        item = None
        error = None
        try:
            item = cls( name=name,
                        description=description,
                        catalog=catalog,
                        user=user )
            DBSession.add(item)
            DBSession.commit()
        except Exception as e:
            DBSession.rollback()
            error = str(e)
        return item, error

    @classmethod
    def edit(cls, id, name, description, catalog):
        """Edits and saves a new item"""
        item = None
        error = None
        try:
            item = cls.find_by_id(id)
            item.name = name
            item.description = description
            item.catalog = catalog
            DBSession.commit()
        except Exception as e:
            DBSession.rollback()
            error = str(e)
        return item, error

    @classmethod
    def find_by_id(cls, id):
        """Finds item by id"""
        return DBSession.query(cls).filter(cls.id == id).first()

    @classmethod
    def get_all(cls):
        """Gets all the items"""
        return DBSession.query(cls).all()

    @classmethod
    def delete(cls, item):
        """Deletes an item"""
        DBSession.delete(item)
        DBSession.commit()

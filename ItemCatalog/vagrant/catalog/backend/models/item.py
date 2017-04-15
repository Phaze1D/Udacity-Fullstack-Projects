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
    user_id     = Column(Integer, ForeignKey('user.id'))
    catalog     = relationship("Catalog", back_populates="items", foreign_keys=[catalog_id])
    user        = relationship("User", back_populates="items", foreign_keys=[user_id])


    @validates('name')
    def validates_name(self, key, name):
        if not name or len(name) < 3:
            raise Exception("Name must be atleast 3 chars")
        return name

    @validates('description')
    def validates_description(self, key, description):
        if not description or len(description) < 20:
            raise Exception("Description must be atleast 20 chars")
        return description

    @validates('catalog')
    def validates_catalog(self, key, catalog):
        if not catalog:
            raise Exception('catalog not found')
        return catalog

    @validates('user')
    def validates_user(self, key, user):
        if not user:
            raise Exception('user not found')
        return user

    @classmethod
    def create(cls, name, description, catalog, user):
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

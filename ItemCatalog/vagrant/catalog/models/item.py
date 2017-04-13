from config import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    created = Column(DateTime, default=func.now())
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    catalog = relationship("Catalog", back_populates="items")
    user = relationship("User", back_populates="items")

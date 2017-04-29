from backend.config import Base, DBSession
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    created = Column(DateTime, default=func.now())
    items = relationship("Item", back_populates="user")
    catalogs = relationship("Catalog", back_populates="user")

    @classmethod
    def find_by_email(cls, email):
        return DBSession.query(cls).filter(cls.email == email).first()

    @classmethod
    def find_by_id(cls, id):
        return DBSession.query(cls).filter(cls.id == id).first()

    @classmethod
    def create(cls, email):
        user = cls(email=email)
        DBSession.add(user)
        DBSession.commit()
        return user

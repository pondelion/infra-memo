from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship

from base import Base
from db import engine


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(TEXT)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")


Base.metadata.create_all(engine)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    password = Column(String)


class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

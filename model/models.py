from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "user_info"
    
    id = Column(String(length=255), primary_key=True)  
    name = Column(String(length=255))

class Msg(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    author_id = Column(String(length=255), ForeignKey('user_info.id'))  
    message = Column(String(length=2000))


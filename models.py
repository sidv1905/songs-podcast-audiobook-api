from sqlalchemy import Boolean, Column,DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import datetime
from database import Base
import sqlalchemy

class Song(Base):
    __tablename__="song"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    duration = Column(Integer,nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)



class Podcast(Base):
    __tablename__ = "podcast"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    duration = Column(Integer,nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
    host = Column(String(100))
    participants = Column(sqlalchemy.types.ARRAY(String(100)))

class Audiobook(Base):
    __tablename__ = "audiobook"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    author = Column(String(100),nullable=False)
    narrator = Column(String(100),nullable = False)
    duration = Column(Integer,nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)



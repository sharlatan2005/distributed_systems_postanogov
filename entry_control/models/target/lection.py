from sqlalchemy import Integer, DateTime
from sqlalchemy import Column, ForeignKey
from .base import Base

class Lection(Base):
    __tablename__ = 'lections'

    id = Column(Integer, primary_key=True)
    id_teacher = Column(Integer, ForeignKey('teachers.id'))
    id_subject = Column(Integer, ForeignKey('subjects.id'))
    start_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)
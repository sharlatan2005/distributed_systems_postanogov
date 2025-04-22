from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from .base import Base

class LectionsAttendance(Base):
    __tablename__ = 'lections_attendance'

    id_student = Column(Integer, ForeignKey('students.id'), primary_key=True)
    id_lection = Column(Integer, ForeignKey('lections.id'), primary_key=True)
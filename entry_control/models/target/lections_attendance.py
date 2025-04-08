from sqlalchemy import ForeignKey
from .base import Base

class LectionsAttendance(Base):
    __tablename__ = 'lections_attendance'

    id_student = ForeignKey('students.id', primary_key=True)
    id_lection = ForeignKey('lections.id', primary_key=True)
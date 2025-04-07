from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WideTable(Base):
    __tablename__ = 'lections'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    student_full_name = Column(String)
    faculty_id = Column(Integer)
    faculty_name = Column(String)
    group_id = Column(Integer)
    group_name = Column(String)
    subject_id = Column(Integer)
    subject_name = Column(String)
    teacher_id = Column(Integer)
    teacher_full_name = Column(String)
    start_timestamp = Column(String)
    end_timestamp = Column(String)
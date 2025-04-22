from sqlalchemy import Integer, DateTime, UniqueConstraint
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lection(Base):
    __tablename__ = 'lections'
    __table_args__ = (
        UniqueConstraint('id_teacher', 'id_subject', 'start_timestamp', 
                        name='uq_lection_teacher_subject_time'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_teacher = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    id_subject = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    start_timestamp = Column(DateTime, nullable=False)
    end_timestamp = Column(DateTime)
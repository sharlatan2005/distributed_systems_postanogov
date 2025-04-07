from sqlalchemy import Integer, String, DateTime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    faculty_id = Column(Integer, ForeignKey('faculties.id'))

class Faculty(Base):
    __tablename__ = 'faculties'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Lection(Base):
    __tablename__ = 'lections'

    id = Column(Integer)
    id_teacher = Column(Integer, ForeignKey('teachers.id'))
    id_subject = Column(Integer, ForeignKey('subjects.id'))
    start_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)

class LectionsAttendance(Base):
    __tablename__ = 'lections_attendance'

    id_student = ForeignKey('students.id', primary_key=True)
    id_lection = ForeignKey('lections.id', primary_key=True)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.target.faculty import Faculty
from models.target.group import Group
from models.target.student import Student
from models.target.subject import Subject
from models.target.teacher import Teacher
from models.target.lection import Lection
from models.target.lections_attendance import LectionsAttendance



def create_sqlite_session(sqlite_path):
    engine = create_engine(f'sqlite:///{sqlite_path}')
    Session = sessionmaker(bind=engine)
    return Session()

def create_postgres_session(config, base):
    engine = create_engine(config)
    Session = sessionmaker(bind=engine)

    base.metadata.drop_all(engine)
    tables = [
        Faculty.__table__,
        Group.__table__,
        Student.__table__,
        Subject.__table__,
        Teacher.__table__,
        Lection.__table__,
        LectionsAttendance.__table__
    ]
    base.metadata.create_all(bind=engine, tables=tables)

    return Session()
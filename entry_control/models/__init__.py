from .target.faculty import Faculty
from .target.group import Group
from .target.student import Student
from .target.subject import Subject
from .target.teacher import Teacher
from .target.lection import Lection
from .target.lections_attendance import LectionsAttendance

tables_list = [
    Faculty.__table__,
    Group.__table__,
    Student.__table__,
    Subject.__table__,
    Teacher.__table__,
    Lection.__table__,
    LectionsAttendance.__table__
]
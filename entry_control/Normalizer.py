from models.source.wide_source_table import WideSourceTable
from models.target.student import Student
from models.target.faculty import Faculty

class Normalizer:
    def __init__(self, sqlite_session, postgres_session):
        self.sqlite_session = sqlite_session
        self.postgres_session = postgres_session
    
    def load_students(self):
        students = self.sqlite_session.query(
          WideSourceTable.student_id,
          WideSourceTable.student_full_name,
          WideSourceTable.group_id
        ).group_by(
            WideSourceTable.student_id
        ).all()

        for student in students:
            student_record = Student(
                id=student.student_id,
                full_name=student.student_full_name,
                group_id=student.group_id
            )
            self.postgres_session.add(student_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')

    def load_faculties(self):
        faculties = self.sqlite_session.query(
          WideSourceTable.faculty_id,
          WideSourceTable.faculty_name
        ).group_by(
            WideSourceTable.faculty_id
        ).all()

        for faculty in faculties:
            faculty_record = Faculty(
                id=faculty.faculty_id,
                name=faculty.faculty_name
            )
            self.postgres_session.add(faculty_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')
    
    def normalize(self):
        self.load_faculties()
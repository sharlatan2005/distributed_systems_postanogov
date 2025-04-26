from models.source.wide_source_table import WideSourceTable

from models.target.faculty import Faculty
from models.target.group import Group
from models.target.student import Student
from models.target.subject import Subject
from models.target.teacher import Teacher
from models.target.lection import Lection
from models.target.lections_attendance import LectionsAttendance

class Normalizer:
    def __init__(self, sqlite_session, postgres_session):
        self.sqlite_session = sqlite_session
        self.postgres_session = postgres_session

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

    def load_groups(self):
        groups = self.sqlite_session.query(
          WideSourceTable.group_id,
          WideSourceTable.group_name,
          WideSourceTable.faculty_id
        ).group_by(
            WideSourceTable.group_id
        ).all()

        for group in groups:
            group_record = Group(
                id=group.group_id,
                name=group.group_name,
                faculty_id=group.faculty_id
                
            )
            self.postgres_session.add(group_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')

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

    def load_subjects(self):
        subjects = self.sqlite_session.query(
          WideSourceTable.subject_id,
          WideSourceTable.subject_name
        ).group_by(
            WideSourceTable.subject_id
        ).all()

        for subject in subjects:
            subject_record = Subject(
                id=subject.subject_id,
                name=subject.subject_name
            )
            self.postgres_session.add(subject_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')

    def load_teachers(self):
        teachers = self.sqlite_session.query(
          WideSourceTable.teacher_id,
          WideSourceTable.teacher_full_name
        ).group_by(
            WideSourceTable.teacher_id
        ).all()

        for teacher in teachers:
            teacher_record = Teacher(
                id=teacher.teacher_id,
                full_name=teacher.teacher_full_name
            )
            self.postgres_session.add(teacher_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')
        
    def load_lections(self):
        lections = self.sqlite_session.query(
          WideSourceTable.lection_id,
          WideSourceTable.teacher_id,
          WideSourceTable.subject_id,
          WideSourceTable.start_timestamp,
          WideSourceTable.end_timestamp
        ).all()

        for lection in lections:
            lection_record = Lection(
                id=lection.lection_id,
                id_teacher=lection.teacher_id,
                id_subject=lection.subject_id,
                start_timestamp=lection.start_timestamp,
                end_timestamp=lection.end_timestamp
            )
            self.postgres_session.add(lection_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')

    def load_lections_attendance(self):
        lections_attendance = self.sqlite_session.query(
          WideSourceTable.id,
          WideSourceTable.lection_id,
          WideSourceTable.student_id
        ).all()

        for attendance_item in lections_attendance:
            attendance_record = LectionsAttendance(
                id=attendance_item.id,
                id_lection=attendance_item.lection_id,
                id_student=attendance_item.student_id,
            )
            self.postgres_session.add(attendance_record)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')

    def normalize(self):
        self.load_faculties()
        self.load_groups()
        self.load_students()
        self.load_subjects()
        self.load_teachers()
        self.load_lections()
        self.load_lections_attendance()
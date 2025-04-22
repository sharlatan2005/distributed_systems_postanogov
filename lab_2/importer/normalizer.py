from sqlalchemy.orm import Session
from models import *

class Normalizer:
    def __init__(self, postgres_session: Session):
        self.postgres_session = postgres_session
        # Кэш для хранения уже обработанных данных
        self.cache = {
            'faculties': set(),
            'groups': set(),
            'students': set(),
            'subjects': set(),
            'teachers': set()
        }

    def process_message(self, wide_table_row: dict):
        """Обработка одной строки из широкой таблицы"""
        # 1. Обрабатываем факультет (если ещё не обработан)
        if wide_table_row['faculty_id'] not in self.cache['faculties']:
            faculty = Faculty(
                id=wide_table_row['faculty_id'],
                name=wide_table_row['faculty_name']
            )
            self.postgres_session.add(faculty)
            self.cache['faculties'].add(wide_table_row['faculty_id'])
        
        # 2. Обрабатываем группу
        if wide_table_row['group_id'] not in self.cache['groups']:
            group = Group(
                id=wide_table_row['group_id'],
                name=wide_table_row['group_name'],
                faculty_id=wide_table_row['faculty_id']
            )
            self.postgres_session.add(group)
            self.cache['groups'].add(wide_table_row['group_id'])
        
        # 3. Обрабатываем студента
        if wide_table_row['student_id'] not in self.cache['students']:
            student = Student(
                id=wide_table_row['student_id'],
                full_name=wide_table_row['student_full_name'],
                group_id=wide_table_row['group_id']
            )
            self.postgres_session.add(student)
            self.cache['students'].add(wide_table_row['student_id'])
        
        # 4. Обрабатываем предмет
        if wide_table_row['subject_id'] not in self.cache['subjects']:
            subject = Subject(
                id=wide_table_row['subject_id'],
                name=wide_table_row['subject_name']
            )
            self.postgres_session.add(subject)
            self.cache['subjects'].add(wide_table_row['subject_id'])
        
        # 5. Обрабатываем преподавателя
        if wide_table_row['teacher_id'] not in self.cache['teachers']:
            teacher = Teacher(
                id=wide_table_row['teacher_id'],
                full_name=wide_table_row['teacher_full_name']
            )
            self.postgres_session.add(teacher)
            self.cache['teachers'].add(wide_table_row['teacher_id'])
        
        # 6. Обрабатываем лекцию
        if wide_table_row['id'] not in self.cache['lections']:
            lection = Lection(
                id=wide_table_row['id'],
                id_teacher=wide_table_row['teacher_id'],
                id_subject=wide_table_row['subject_id'],
                start_timestamp=wide_table_row['start_timestamp'],
                end_timestamp=wide_table_row['end_timestamp']
            )
            self.postgres_session.add(lection)
            self.cache['lections'].add(wide_table_row['id'])
        
        # 7. Обрабатываем посещение
        attendance = LectionsAttendance(
            id_lection=wide_table_row['id'],
            id_student=wide_table_row['student_id']
        )
        self.postgres_session.add(attendance)
        
        try:
            self.postgres_session.commit()
        except Exception as e:
            self.postgres_session.rollback()
            print(f'Error: {e}')
            raise
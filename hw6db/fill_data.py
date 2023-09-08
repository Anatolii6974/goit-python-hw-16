from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_TEACHERS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 20

arr_groups = ["A", "B", "C"]  # List of groups
arr_subjects = ["Mathematics", "Physics", "History", "Chemistry", "Geography"]  # List of subjects


def generate_fake_data(number_teachers, number_students) -> tuple():

    fake_teacher_name = []  # Name of teachers
    fake_student_name = []  # Name of students

    fake_data = faker.Faker()

    # Create list of teachers
    for _ in range(number_teachers):
        fake_teacher_name.append(fake_data.name())

    # Create list of students
    for _ in range(number_students):
        fake_student_name.append(fake_data.name())

    return fake_teacher_name, fake_student_name


def prepare_data(name_teachers, name_students) -> tuple():

    for_groups = []  # List of groups
    for group_name in arr_groups:
        for_groups.append((group_name, ))

    for_students = []  # List of students
    for name_student in name_students:
        for_students.append((name_student, randint(1, NUMBER_GROUPS)))

    for_teachers = []
    for name_teacher in name_teachers:
        for_teachers.append((name_teacher, ))

    for_subjects = []
    for subject in arr_subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = []
    for student in range(1, NUMBER_STUDENTS+1):
        for subject in range(1, NUMBER_SUBJECTS+1):
            for _ in range(5):
                grade_date = datetime(2023, randint(1, 5), randint(1, 28)).date()
                for_grades.append((randint(1, 12), student, subject, grade_date))    



    return for_groups, for_students, for_teachers, for_subjects, for_grades


def insert_data_to_db(groups, students, teachers, subjects, grades) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)""" 
        cur.executemany(sql_to_groups, groups)
 
        sql_to_students = """INSERT INTO students(students_name, group_id)
                               VALUES (?, ?)""" 
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)""" 
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject, teacher_id)
                               VALUES (?, ?)""" 
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(grade, student_id, subject_id, date_of)
                               VALUES (?, ?, ?, ?)""" 
        cur.executemany(sql_to_grades, grades)


        con.commit()


if __name__ == "__main__":
    groups, students, teachers, subjects, grades = prepare_data(*generate_fake_data(NUMBER_TEACHERS, NUMBER_STUDENTS))
    insert_data_to_db(groups, students, teachers, subjects, grades)
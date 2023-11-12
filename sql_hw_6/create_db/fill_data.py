from datetime import datetime
from random import randint, choice

from faker import Faker
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 45
NUMBER_SUBJECTS = 7
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

fake_data = Faker()

def fill_groups():
    return ["Gryffindor", "Ravenclaw", "Slytherin"]


def fill_students():
    result = []

    for _ in range(NUMBER_STUDENTS):
        result.append(fake_data.name())

    return result


def fill_subjects():
    return ["Defence Against the Dark Arts", "Astronomy", "Transfiguration", "Charms", "Potions", "History of Magic", "Herbology"]


def fill_teachers():
    result = []

    for _ in range(NUMBER_TEACHERS):
        result.append(fake_data.name())

    return result


def prepare_data():
    data_groups = []
    data_students = []
    data_teachers = []
    data_subjects = []
    data_grades = []

    # groups
    list_gruops = fill_groups()
    for group in list_gruops:
        data_groups.append((group,))

    # students
    list_students = fill_students()
    list_students_copy = list_students.copy()
    while len(list_students_copy):
        for group in list_gruops:
            student = choice(list_students_copy)
            data_students.append((student, list_gruops.index(group) + 1))
            list_students_copy.remove(student)

    # teachers
    list_teachers = fill_teachers()
    for teacher in list_teachers:
        data_teachers.append((teacher,))
    
    # subjects
    list_subjects = fill_subjects()
    count = 1
    for subject in list_subjects:
        count = count if count <= (len(list_teachers)) else 1
        data_subjects.append((subject, count))
        count += 1
    
    # grades
    for student in range(1, NUMBER_STUDENTS + 1):
        count_gr = randint(10, 20)
        while count_gr:
            subject = choice(range(1, NUMBER_SUBJECTS + 1))
            date = datetime(2023, randint(10, 11), randint(1, 30)).date()
            grade = randint(50, 100)
            data_grades.append((student, subject, date, grade))
            count_gr -= 1
    
    return {"groups": data_groups, "students": data_students, "teachers": data_teachers, "subjects": data_subjects, "grades": data_grades}


def insert_data_to_db():
    data = prepare_data()

    with sqlite3.connect('../university.db') as con:
        cur = con.cursor()

        # groups
        sql_groups = """INSERT INTO groups(group_name)
                        VALUES (?)"""
        cur.executemany(sql_groups, data["groups"])

        # students
        sql_students = """INSERT INTO students(student, group_id)
                        VALUES (?, ?)"""
        cur.executemany(sql_students, data["students"])

        # teachers
        sql_teachers = """INSERT INTO teachers(teacher)
                        VALUES (?)"""
        cur.executemany(sql_teachers, data["teachers"])

        # subjects
        sql_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                        VALUES (?, ?)"""
        cur.executemany(sql_subjects, data["subjects"])

        # grades
        sql_grades = """INSERT INTO grades(student_id, subject_id, date_of, grade)
                        VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_grades, data["grades"])

        con.commit()


if __name__ == "__main__":
    insert_data_to_db()

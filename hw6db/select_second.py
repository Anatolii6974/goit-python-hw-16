import sqlite3

# Знайти студента із найвищим середнім балом з певного предмета.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.students_name, sub.subject, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
GROUP BY s.students_name, sub.subject
ORDER BY average_grade DESC
LIMIT 1;
"""

print(execute_query(sql))
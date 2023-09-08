import sqlite3

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.students_name, AVG(g.grade) as average_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.students_name
ORDER BY average_grade DESC
LIMIT 5;
"""

print(execute_query(sql))
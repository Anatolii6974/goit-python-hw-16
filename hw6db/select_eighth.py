import sqlite3

# Знайти середній бал, який ставить певний викладач зі своїх предметів.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.teacher_name, sub.subject, AVG(g.grade) as average_grade
FROM grades g
INNER JOIN subjects sub ON g.subject_id = sub.id
INNER JOIN teachers t ON t.id = sub.teacher_id
GROUP BY t.teacher_name, sub.subject;
"""     

print(execute_query(sql))
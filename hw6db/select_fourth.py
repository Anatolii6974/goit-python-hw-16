import sqlite3

# Знайти середній бал на потоці (по всій таблиці оцінок).

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT AVG(grade) as average_grade
FROM grades;
"""

print(execute_query(sql))
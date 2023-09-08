import sqlite3

# Знайти, які курси читає певний викладач.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.teacher_name, GROUP_CONCAT(s.subject, ', ') as subjects_taught
FROM teachers t
INNER JOIN subjects s ON t.id = s.teacher_id
GROUP BY t.teacher_name;
"""

print(execute_query(sql))
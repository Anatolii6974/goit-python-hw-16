import sqlite3

# Знайти оцінки студентів в окремій групі з певного предмета.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT gr.group_name, sub.subject, GROUP_CONCAT(g.grade, ', ') as GR
FROM students s
INNER JOIN grades g ON s.id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.id
INNER JOIN groups gr ON gr.id = s.group_id
GROUP BY gr.group_name, sub.subject;
"""     

print(execute_query(sql))
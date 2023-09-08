import sqlite3

# Знайти середній бал у групах з певного предмета.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
 
sql = """
SELECT gr.group_name, sub.subject, AVG(g.grade) AS average_grade
FROM students s
JOIN groups gr ON s.group_id = gr.id
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
GROUP BY s.group_id, sub.subject;
"""

print(execute_query(sql))
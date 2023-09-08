import sqlite3

# Знайти список курсів, які відвідує студент.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql1 = """
SELECT st.students_name, GROUP_CONCAT(DISTINCT s.subject)
FROM students st
INNER JOIN grades g ON st.id = g.student_id
INNER JOIN subjects s ON g.subject_id = s.id
GROUP BY st.students_name;
"""
sql = """
SELECT s.students_name, sub.subject
FROM students s
INNER JOIN grades g ON s.id = g.student_id
INNER JOIN subjects sub ON g.subject_id = sub.id
GROUP BY s.students_name, sub.subject;
"""


print(execute_query(sql1))

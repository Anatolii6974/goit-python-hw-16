import sqlite3

# Список курсів, які певному студенту читає певний викладач.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# 'введіть ім'я студента та ім'я викладача
sql1 = """
SELECT s.subject
FROM students st
INNER JOIN grades g ON st.id = g.student_id
INNER JOIN subjects s ON g.subject_id = s.id
INNER JOIN teachers t ON s.teacher_id = t.id
WHERE st.students_name = 'Jennifer Turner' AND t.teacher_name = 'James Wilson';
"""

sql = """
SELECT st.students_name, t.teacher_name, GROUP_CONCAT(DISTINCT s.subject)
FROM students st
INNER JOIN grades g ON st.id = g.student_id
INNER JOIN subjects s ON g.subject_id = s.id
INNER JOIN teachers t ON s.teacher_id = t.id
GROUP BY st.students_name;
"""



print(execute_query(sql))
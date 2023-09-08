import sqlite3

# Знайти список студентів у певній групі.

def execute_query(sql: str) -> list:
    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT gr.group_name, GROUP_CONCAT(s.students_name, ', ') as ST_NAME
FROM students s
INNER JOIN groups gr ON s.group_id = gr.id
GROUP BY gr.group_name;
"""   

print(execute_query(sql))
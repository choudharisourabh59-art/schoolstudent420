import pandas as pd
from database.connection import connect
def student_report():
    with connect() as con: return pd.read_sql_query("SELECT admission_no,name,class_name,section,roll_no,status FROM students",con)
def attendance_report():
    with connect() as con: return pd.read_sql_query("SELECT day,status,COUNT(*) count FROM attendance GROUP BY day,status ORDER BY day",con)

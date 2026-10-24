from database.connection import connect
def save_attendance(student_id,day,status):
    if status not in {"Present","Absent","Late"}: raise ValueError("Invalid attendance status.")
    with connect() as con:
        con.execute("""INSERT INTO attendance(student_id,day,status) VALUES(?,?,?)
        ON CONFLICT(student_id,day) DO UPDATE SET status=excluded.status""",(int(student_id),day,status))

from database.connection import connect
from database.models import validate_marks
def save_mark(student_id,exam_id,marks,maximum):
    marks=validate_marks(marks,maximum)
    with connect() as con:
        con.execute("""INSERT INTO results(student_id,exam_id,marks) VALUES(?,?,?)
        ON CONFLICT(student_id,exam_id) DO UPDATE SET marks=excluded.marks""",(int(student_id),int(exam_id),marks))

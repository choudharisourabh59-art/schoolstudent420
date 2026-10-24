from database.connection import connect
def add_student(admission_no,name,class_name,section="A",roll_no="",guardian="",phone="",email=""):
    if not admission_no.strip() or not name.strip(): raise ValueError("Admission number and name are required.")
    with connect() as con:
        cur=con.execute("""INSERT INTO students(admission_no,name,class_name,section,roll_no,guardian,phone,email)
        VALUES(?,?,?,?,?,?,?,?)""",(admission_no.strip(),name.strip(),str(class_name),section,roll_no,guardian,phone,email))
        return cur.lastrowid
def list_students():
    with connect() as con: return con.execute("SELECT * FROM students ORDER BY class_name,section,roll_no").fetchall()

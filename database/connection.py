import sqlite3
from config.settings import DB_PATH

def connect():
    DB_PATH.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(DB_PATH,timeout=30,check_same_thread=False)
    con.row_factory=sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con

def init_db():
    with connect() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,
          role TEXT NOT NULL CHECK(role IN ('admin','teacher','student','parent')),linked_id INTEGER);
        CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,admission_no TEXT UNIQUE NOT NULL,name TEXT NOT NULL,
          class_name TEXT NOT NULL,section TEXT NOT NULL DEFAULT 'A',roll_no TEXT,guardian TEXT,phone TEXT,email TEXT,
          status TEXT NOT NULL DEFAULT 'Active');
        CREATE TABLE IF NOT EXISTS teachers(id INTEGER PRIMARY KEY,employee_no TEXT UNIQUE NOT NULL,name TEXT NOT NULL,
          subject TEXT,phone TEXT,email TEXT,assigned_class TEXT);
        CREATE TABLE IF NOT EXISTS attendance(id INTEGER PRIMARY KEY,student_id INTEGER NOT NULL REFERENCES students(id),
          day TEXT NOT NULL,status TEXT NOT NULL CHECK(status IN ('Present','Absent','Late')),UNIQUE(student_id,day));
        CREATE TABLE IF NOT EXISTS exams(id INTEGER PRIMARY KEY,title TEXT NOT NULL,class_name TEXT NOT NULL,
          subject TEXT NOT NULL,max_marks REAL NOT NULL CHECK(max_marks>0),exam_day TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS results(id INTEGER PRIMARY KEY,student_id INTEGER NOT NULL REFERENCES students(id),
          exam_id INTEGER NOT NULL REFERENCES exams(id),marks REAL NOT NULL CHECK(marks>=0),UNIQUE(student_id,exam_id));
        CREATE TABLE IF NOT EXISTS enrollments(id INTEGER PRIMARY KEY,student_id INTEGER NOT NULL REFERENCES students(id),
          academic_year TEXT NOT NULL,class_name TEXT NOT NULL,section TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'Current',
          UNIQUE(student_id,academic_year));
        CREATE TABLE IF NOT EXISTS documents(id INTEGER PRIMARY KEY,student_id INTEGER REFERENCES students(id),
          original_name TEXT NOT NULL,stored_name TEXT NOT NULL,uploaded_at TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS audit_log(id INTEGER PRIMARY KEY,username TEXT,action TEXT NOT NULL,detail TEXT,
          created_at TEXT DEFAULT CURRENT_TIMESTAMP);
        """)
        if not con.execute("SELECT COUNT(*) FROM users").fetchone()[0]:
            from services.auth_service import hash_password
            con.execute("INSERT INTO users(username,password_hash,role) VALUES(?,?,?)",
                       ("admin",hash_password("ChangeMe123!"),"admin"))
        if not con.execute("SELECT COUNT(*) FROM students").fetchone()[0]:
            cur=con.execute("INSERT INTO students(admission_no,name,class_name,section,roll_no,guardian) VALUES(?,?,?,?,?,?)",
                           ("DEMO001","Demo Student","9","A","1","Demo Guardian"))
            con.execute("INSERT INTO enrollments(student_id,academic_year,class_name,section) VALUES(?,?,?,?)",
                       (cur.lastrowid,"2026-27","9","A"))

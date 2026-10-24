from database.connection import connect
def promote(class_from,section,year_from,year_to,class_to=None):
    if year_from==year_to: raise ValueError("Academic years must differ.")
    class_to=class_to or str(int(class_from)+1)
    with connect() as con:
        roster=con.execute("SELECT id FROM students WHERE class_name=? AND section=? AND status='Active'",
                           (str(class_from),section)).fetchall()
        count=0
        for r in roster:
            sid=r["id"]
            if con.execute("SELECT 1 FROM enrollments WHERE student_id=? AND academic_year=?",(sid,year_to)).fetchone(): continue
            con.execute("INSERT INTO enrollments(student_id,academic_year,class_name,section,status) VALUES(?,?,?,?,?)",
                       (sid,year_to,class_to,section,"Current"))
            con.execute("UPDATE enrollments SET status='Completed' WHERE student_id=? AND academic_year=?",(sid,year_from))
            con.execute("UPDATE students SET class_name=? WHERE id=?",(class_to,sid)); count+=1
        return count

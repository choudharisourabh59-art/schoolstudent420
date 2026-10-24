import streamlit as st,pandas as pd
from database.connection import connect
def render(user):
    st.title("Student portfolio")
    sid=user.get("linked_id")
    if user["role"]=="admin":
        with connect() as con: roster=pd.read_sql_query("SELECT id,name FROM students",con)
        if roster.empty: st.info("No students."); return
        sid=st.selectbox("Student",roster.id,format_func=lambda x:roster.loc[roster.id==x,"name"].iloc[0])
    if not sid: st.info("Account has no linked student."); return
    with connect() as con:
        s=con.execute("SELECT * FROM students WHERE id=?",(sid,)).fetchone()
        a=pd.read_sql_query("SELECT day,status FROM attendance WHERE student_id=? ORDER BY day DESC",con,params=(sid,))
        r=pd.read_sql_query("""SELECT e.title,e.subject,e.exam_day,x.marks,e.max_marks,
        ROUND(x.marks*100.0/e.max_marks,2) percentage FROM results x JOIN exams e ON e.id=x.exam_id
        WHERE x.student_id=? ORDER BY e.exam_day DESC""",con,params=(sid,))
    if not s: st.error("Student not found."); return
    st.subheader(s["name"]); st.write(f"Admission {s['admission_no']} · Class {s['class_name']}-{s['section']}")
    st.subheader("Attendance"); st.dataframe(a,use_container_width=True,hide_index=True)
    st.subheader("Results"); st.dataframe(r,use_container_width=True,hide_index=True)

import streamlit as st,pandas as pd
from database.connection import connect
from services.grade_service import save_mark
def render(user):
    st.title("Results")
    if user["role"] not in ("admin","teacher"): st.warning("Teacher/admin access only."); return
    with connect() as con: exams=pd.read_sql_query("SELECT * FROM exams",con)
    if exams.empty: st.info("Create an exam first."); return
    eid=st.selectbox("Exam",exams.id,format_func=lambda x:exams.loc[exams.id==x,"title"].iloc[0])
    exam=exams[exams.id==eid].iloc[0]
    with connect() as con: roster=pd.read_sql_query("SELECT id,name FROM students WHERE class_name=?",(con),params=(exam.class_name,))
    with st.form("marks"):
        vals={int(s.id):st.number_input(s.name,min_value=0.0,max_value=float(exam.max_marks),value=0.0,key=f"mark{eid}{s.id}") for _,s in roster.iterrows()}
        submit=st.form_submit_button("Save marks")
    if submit:
        for sid,mark in vals.items(): save_mark(sid,eid,mark,exam.max_marks)
        st.success("Marks saved.")
    with connect() as con:
        result=pd.read_sql_query("""SELECT s.admission_no,s.name,e.subject,r.marks,e.max_marks,
        ROUND(r.marks*100.0/e.max_marks,2) percentage FROM results r JOIN students s ON s.id=r.student_id
        JOIN exams e ON e.id=r.exam_id WHERE e.id=?""",con,params=(int(eid),))
    st.dataframe(result,use_container_width=True,hide_index=True)
    st.download_button("Export results CSV",result.to_csv(index=False).encode(),"results.csv","text/csv")
